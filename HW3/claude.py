#!/usr/bin/env python3

import json
import http.client
import time
import readline as _readline

# ===== Configuration =====
claude_secrets_file = "claude_secrets.json"
model_version = "claude-sonnet-4-20250514"
temperature = 0
max_tokens = 1000
sleepseconds = 1

# Load Claude API key
def load_claude_key():
    try:
        with open(claude_secrets_file, "r") as f:
            data = json.load(f)
        return data["claude_key"]
    except Exception as e:
        print("Failed to load Claude API key:", e)
        exit(1)

# Call Claude
def call_claude(prompt, system_prompt=None):
    key = load_claude_key()
    messages = [{"role": "user", "content": prompt}]
    payload = {
        "model": model_version,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    if system_prompt:
        payload["system"] = [{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}]

    calltxt = json.dumps(payload)
    host = "api.anthropic.com"
    conn = http.client.HTTPSConnection(host)

    try:
        conn.request("POST", "/v1/messages", calltxt, headers={
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01",
            "x-api-key": key
        })
        response = conn.getresponse()
        rawdata = response.read()
        if response.status != 200:
            print(f"Error {response.status}: {response.reason}")
            print(rawdata.decode())
            return None
        data = json.loads(rawdata)
        return "".join(part["text"] for part in data.get("content", []))
    except Exception as e:
        print("Error calling Claude:", e)
        return None
    finally:
        conn.close()

# ===== Interactive CLI =====
def main():
    print("Claude CLI (type 'exit' to quit)\n")
    while True:
        prompt = input("You: ").strip()
        if prompt.lower() in {"exit", "quit"}:
            print("Exiting Claude CLI.")
            break
        if not prompt:
            continue
        print("Claude is thinking...")
        response = call_claude(prompt)
        if response:
            print("\nClaude:", response, "\n")
        else:
            print("No response from Claude.\n")
        time.sleep(sleepseconds)

if __name__ == "__main__":
    main()