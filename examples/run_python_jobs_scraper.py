from scraper_agent.parser import parse_english_instructions
from scraper_agent.agent import ScraperAgent

def main():
    # Example instructions for scraping Tesla careers page
    instructions = """
    Go to https://www.tesla.com/careers
    Click the 'Search Jobs' button
    Wait for the job listings to load
    Extract number of job postings from the body
    """
    
    # Parse instructions into steps
    steps = parse_english_instructions(instructions)
    
    # Create and run the agent
    agent = ScraperAgent(steps)
    results = agent.run()
    
    # Print results
    print("Scraping Results:")
    for i, result in enumerate(results, 1):
        print(f"Result {i}: {result}")

if __name__ == "__main__":
    main() 