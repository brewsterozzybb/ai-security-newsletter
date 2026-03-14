import json
import os
from datetime import datetime

# Paths
VAULT_INDEX = '/Users/ozzybrewster/Documents/research/vault-index.json'
NEWSLETTER_DIR = '/Users/ozzybrewster/Documents/research/newsletters/newsletters/2026/03/'
README_PATH = '/Users/ozzybrewster/Documents/research/newsletters/README.md'

def generate_readme():
    # Load stats
    try:
        with open(VAULT_INDEX, 'r') as f:
            vault_data = json.load(f)
            total_entries = len(vault_data)
            tags = {}
            for entry in vault_data:
                for tag in entry.get('tags', []):
                    tags[tag] = tags.get(tag, 0) + 1
            top_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)[:3]
    except:
        total_entries = "N/A"
        top_tags = []

    # Get editions
    editions = sorted([f for f in os.listdir(NEWSLETTER_DIR) if f.endswith('.md')], reverse=True)
    total_editions = len(editions)
    recent = editions[:3]

    tag_line = " ".join([f"`#{t[0]} ({t[1]})`" for t in top_tags])
    
    readme_content = f"""# 🛡️ AI Security Newsletter: Living Dashboard

Operational Dashboard & Intelligence Index for the *brewsterozzybb* primary research stack.

## 📊 Project Pulse

| Vault Entries | Editions Published | Research SLA |
| :--- | :--- | :--- |
| **{total_entries}** | **{total_editions}** | **4 Minutes** |

## 🧠 Current Intelligence Focus
{tag_line}

## 📅 Recent Transmissions

"""
    for ed in recent:
        readme_content += f"- **[{ed}](./newsletters/2026/03/{ed})** — Latest research and technical analysis.\n"

    readme_content += f"\n\n---\n*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ET* / *Runtime: OK*"
    
    with open(README_PATH, 'w') as f:
        f.write(readme_content)

if __name__ == "__main__":
    generate_readme()
