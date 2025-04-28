# Scraper Agent

## Overview
**Scraper Agent** is a lightweight Python framework that lets you:
- **Define website scraping behaviors in English**
- **Automatically generate agents** that navigate, click, wait, and extract data
- **Run agents headlessly** using Playwright

No need to manually code scraping logic for every website.
Write the steps you want, the agent figures out the rest.

## Features
- Define scrapers with **natural language** (plain English)
- Supports **navigation**, **clicking**, **waiting**, **text extraction**, and **number extraction**
- Modular and **easy to extend**
- Powered by **Playwright** for robust browser automation
- Future-ready: add LLM-based selector generation later!

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/scraper-agent.git
cd scraper-agent
```

2. Set up the virtual environment using mamba:
```bash
# Install mamba if you haven't already
conda install -n base -c conda-forge mamba

# Create and activate the virtual environment
mamba create -n scraper-agent python=3.11
mamba activate scraper-agent

# Install dependencies
pip install -r requirements.txt
playwright install
```

## Quick Start

Write your English instructions:
```text
Go to https://www.tesla.com/careers
Click the 'Search Jobs' button
Wait for the job listings to load
Extract number of job postings from the body
```

Then in Python:
```python
from scraper_agent.parser import parse_english_instructions
from scraper_agent.agent import ScraperAgent

instructions = """
Go to https://www.tesla.com/careers
Click the 'Search Jobs' button
Wait for the job listings to load
Extract number of job postings from the body
"""

steps = parse_english_instructions(instructions)
agent = ScraperAgent(steps)
result = agent.run()
print(result)
```

## Supported Actions
| Action | Description |
|:--|:--|
| `GO_TO` | Navigate to a URL |
| `CLICK` | Click a button or link |
| `WAIT_FOR` | Wait for an element to appear |
| `EXTRACT_TEXT` | Extract full text from an element |
| `EXTRACT_NUMBER` | Extract numeric values from an element |

## Project Structure
```bash
scraper-agent/
├── scraper_agent/
│   ├── __init__.py
│   ├── agent.py         # ScraperAgent and StepType classes
│   ├── parser.py        # English-to-steps parser
│   └── utils.py         # (optional future helpers)
├── examples/
│   ├── run_tesla_scraper.py  # Example run script
├── requirements.txt
├── .gitignore
└── README.md
```

## Future Ideas
- Smarter selector guessing using LLMs
- Multi-step workflows (pagination, form filling)
- Retry and resilience features
- Database and CSV output
- Web UI for non-coders to generate scrapers

## Requirements
- Python 3.11+
- Playwright
- mamba (recommended) or conda for environment management

## License
MIT License

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. 