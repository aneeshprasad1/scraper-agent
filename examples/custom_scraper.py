from scraper_agent.parser import parse_english_instructions
from scraper_agent.agent import ScraperAgent

def scrape_website(url, element_to_wait_for, element_to_extract):
    """
    Generic function to scrape text from any website.
    
    Args:
        url: The website URL to scrape
        element_to_wait_for: CSS selector for element to wait for
        element_to_extract: CSS selector for element to extract text from
    """
    instructions = f"""
    Go to {url}
    Wait for {element_to_wait_for}
    Extract text from {element_to_extract}
    """
    
    with ScraperAgent(parse_english_instructions(instructions)) as agent:
        result = agent.run()
        return result

def main():
    # Example 1: Scrape example.com title
    print("\nScraping example.com:")
    result = scrape_website(
        url="https://example.com",
        element_to_wait_for="h1",
        element_to_extract="h1"
    )
    print(f"Title: {result}")
    
    # Example 2: Scrape MDN Web Docs title
    print("\nScraping MDN Web Docs:")
    result = scrape_website(
        url="https://developer.mozilla.org/en-US/",
        element_to_wait_for="#content",
        element_to_extract="h1"
    )
    print(f"Title: {result}")

if __name__ == "__main__":
    main() 