# Estonian Tourism Knowledge Base

This project implements a knowledge base for Estonian tourism using YAGO datasets and a first-order logic reasoner. It explores relationships between cities, cultural figures, and historical places in Estonia.

## Project Structure

```
.
├── data/                              # Directory containing all data files
│   ├── estonia_tourism_knowledge_base.txt    # Main knowledge base file containing all processed data
│   ├── *_reasoner.txt                # Individual processed YAGO data files
├── queries/                           # Directory containing example queries
│   ├── cultural_relations.txt         # Queries about cultural connections
│   ├── city_characteristics.txt       # Queries about city features
│   ├── people_places.txt             # Queries about people and places
├── gkcosx                            # The first-order logic reasoner executable
└── process_yago_data.py              # Script for downloading and processing YAGO data
```

## Getting Started

1. Make sure the reasoner is executable:

   ```bash
   chmod +x gkcosx
   ```

2. Download and process the YAGO data:

   ```bash
   python3 process_yago_data.py
   ```

   This will:

   - Download the latest YAGO data files about Estonia
   - Process and clean the data
   - Create the main knowledge base file `data/estonia_tourism_knowledge_base.txt`

3. Run queries using the reasoner:
   ```bash
   ./gkcosx -mbsize 2000 data/estonia_tourism_knowledge_base.txt queries/your_query.txt
   ```

## Example Queries

1. Cultural Relations (queries/cultural_relations.txt):

   ```bash
   ./gkcosx -mbsize 2000 data/estonia_tourism_knowledge_base.txt queries/cultural_relations.txt
   ```

   Finds connections between cultural figures and academic cities. Example result:

   ```
   result: proof found
   for data/estonia_tourism_knowledge_base.txt queries/cultural_relations.txt

   answer: $ans("Artist and intellectual from same city:","yago:Andres_Koort","and","yago:Edgar_Kant","from","yago:Tallinn") | $ans("Artist and intellectual from same city:","yago:Helju_Rebane","and","yago:Andres_Koort","from","yago:Tallinn").
   proof:
   ...
   ```

2. City Characteristics (queries/city_characteristics.txt):

   ```bash
   ./gkcosx -mbsize 2000 data/estonia_tourism_knowledge_base.txt queries/city_characteristics.txt
   ```

   Identifies city that is historically significant and has university:

   ```
   result: proof found
   for data/estonia_tourism_knowledge_base.txt queries/city_characteristics.txt

   answer: $ans("City with both university and historical significance:","yago:Tartu").
   proof:
   ...
   ```

3. People and Places (queries/people_places.txt):
   ```bash
   ./gkcosx -mbsize 2000 data/estonia_tourism_knowledge_base.txt queries/people_places.txt
   ```
   Shows connections between people and significant places. Example result:
   ```
   "Person born in university city: yago:Kristin_Kuuba in yago:Tartu"
   ```

## Data Processing

The `process_yago_data.py` script:

1. Downloads YAGO data files about Estonia from TalTech's server
2. Cleans and formats the data for the reasoner
3. Combines processed files into a comprehensive knowledge base

The final knowledge base (`estonia_tourism_knowledge_base.txt`) contains:

- People data (birthplaces, professions)
- Location data (cities, landmarks)
- Cultural facts
- Estonian taxonomy
- YAGO schema definitions

## Reasoner Options

The reasoner (`gkcosx`) supports various options:

- `-mbsize 2000`: Allocates 2000MB of memory (adjust if needed)
- `-seconds n`: Limits running time to n seconds
- `-print n`: Controls output verbosity (default: 10)

For more options, run:

```bash
./gkcosx -help
```
