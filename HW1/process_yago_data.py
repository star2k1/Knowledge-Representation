import requests
import os
from urllib.parse import urljoin
import re

def download_file(url, local_filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(local_filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded {local_filename}")


def clean_value(value):
    """Clean and format values for the reasoner"""
    # Remove problematic datetime format
    if 'T00:00:00Z"^^xsd:dateTime' in value:
        value = value.split("T")[0].strip('"')

    # Clean up encoded characters
    value = value.replace("_u0028_", "_")
    value = value.replace("_u0029_", "_")

    # Handle special characters and spaces
    value = value.replace('"', '\\"')
    return value


def convert_triple_to_reasoner_format(subject, predicate, obj):
    """Convert RDF triple to reasoner format with sanitizing"""
    subject = clean_value(subject)
    predicate = clean_value(predicate)
    obj = clean_value(obj)

    return f'triple("{subject}","{predicate}","{obj}").'


def process_yago_file(input_file, output_file, filter_predicates=None):
    """Process YAGO data file and convert to reasoner format"""
    print(f"Processing {input_file}...")
    with open(input_file, "r", encoding="utf-8") as f_in, open(
        output_file, "w", encoding="utf-8"
    ) as f_out:
        for line in f_in:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # Split the triple (simple split by tabs)
            parts = line.split("\t")
            if len(parts) < 3:
                continue

            subject, predicate, obj = parts[0:3]

            # Skip language tags and comments if not needed
            if "@" in obj or (filter_predicates and predicate not in filter_predicates):
                continue

            # Convert and write
            reasoner_triple = convert_triple_to_reasoner_format(subject, predicate, obj)
            f_out.write(reasoner_triple + "\n")

    print(f"Processed {input_file} -> {output_file}")


def combine_files(files_to_combine, output_file):
    """Combine multiple files into one"""
    print(f"Combining files into {output_file}...")
    with open(output_file, "w", encoding="utf-8") as f_out:
        for file in files_to_combine:
            if os.path.exists(file):
                with open(file, "r", encoding="utf-8") as f_in:
                    content = f_in.read()
                    if content.strip():  # Only write non-empty content
                        f_out.write(content)
                        f_out.write("\n")  # Add newline between files
    print(f"Combined files into {output_file}")


def main():
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")

    # Base URL for the YAGO Estonian data files
    base_url = "https://cs.taltech.ee/staff/riina.maigre/iti8700/lab1/"

    # List of files to download
    files = [
        "created-in-estonia.txt",
        "estonian_taxonomy.txt",
        "located-in-estonia.txt",
        "people-in-estonia.txt",
        "facts-about-estonia.txt",
        "yago-schema.txt",
    ]

    # Define relevant predicates to keep
    filter_predicates = {
        "rdf:type",
        "schema:birthPlace",
        "yago:flowsInto",
        "schema:birthDate",
        "rdfs:label",
        "schema:containedInPlace",
        "schema:location",
        "yago:hasLatitude",
        "yago:hasLongitude",
        "schema:description",
        "schema:alternateName",
        "yago:hasFacility",
        "yago:hasTransport",
        "yago:directTransportTo",
        "yago:hasPort",
        "yago:activeIn",
        "yago:isModernEra",
    }

    processed_files = []

    # Download and process files
    for file in files:
        url = urljoin(base_url, file.replace("_", "%5F"))
        local_path = os.path.join("data", file)
        processed_file = os.path.join(
            "data", f"{os.path.splitext(file)[0]}_reasoner.txt"
        )

        # Always download fresh copy
        download_file(url, local_path)

        # Process and clean in one step
        process_yago_file(local_path, processed_file, filter_predicates)
        processed_files.append(processed_file)

        # Remove original file
        os.remove(local_path)

    # Combine relevant files for queries
    main_files = [
        os.path.join("data", "people-in-estonia_reasoner.txt"),
        os.path.join("data", "located-in-estonia_reasoner.txt"),
        os.path.join("data", "created-in-estonia_reasoner.txt"),
        os.path.join("data", "facts-about-estonia_reasoner.txt"),
        os.path.join("data", "estonian_taxonomy_reasoner.txt"),
        os.path.join("data", "yago-schema_reasoner.txt"),
    ]
    combine_files(
        main_files, os.path.join("data", "estonia_tourism_knowledge_base.txt")
    )

    print("\nData processing complete! You can now run queries using:")
    print(
        "./gkcosx -mbsize 2000 data/estonia_tourism_knowledge_base.txt queries/your_query.txt"
    )


if __name__ == "__main__":
    main()
