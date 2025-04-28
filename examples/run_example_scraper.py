from scraper_agent.parser import parse_english_instructions
from scraper_agent.agent import ScraperAgent

def main():
    instructions = """
    Go to https://example.com
    Wait for h1
    Extract text from h1
    """

    steps = parse_english_instructions(instructions)
    
    with ScraperAgent(steps) as agent:
        result = agent.run()
        print(f"Example.com title: {result}")

if __name__ == "__main__":
    main() 