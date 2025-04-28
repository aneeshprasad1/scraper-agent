from scraper_agent.parser import parse_english_instructions
from scraper_agent.agent import ScraperAgent

def test_basic_scraping():
    """Test basic text extraction from a simple website."""
    instructions = """
    Go to https://example.com
    Wait for h1
    Extract text from h1
    """
    
    with ScraperAgent(parse_english_instructions(instructions)) as agent:
        result = agent.run()
        print(f"Basic scraping result: {result}")
        assert result == "Example Domain"

def test_click_and_wait():
    """Test clicking and waiting for elements."""
    instructions = """
    Go to https://www.python.org
    Click the 'Downloads' link
    Wait for #downloads
    Extract text from #downloads h1
    """
    
    with ScraperAgent(parse_english_instructions(instructions)) as agent:
        result = agent.run()
        print(f"Click and wait result: {result}")
        assert result is not None

def test_number_extraction():
    """Test extracting numbers from a webpage."""
    instructions = """
    Go to https://www.python.org
    Wait for #downloads
    Extract number from #downloads
    """
    
    with ScraperAgent(parse_english_instructions(instructions)) as agent:
        result = agent.run()
        print(f"Number extraction result: {result}")
        assert result is not None

def test_custom_scraper():
    """Example of creating a custom scraper for any website."""
    # You can modify these instructions for any website
    instructions = """
    Go to https://www.python.org
    Wait for #downloads
    Extract text from #downloads h1
    """
    
    with ScraperAgent(parse_english_instructions(instructions)) as agent:
        result = agent.run()
        print(f"\nCustom scraper result: {result}")

if __name__ == "__main__":
    print("Running scraper agent tests...")
    print("\n1. Testing basic scraping:")
    test_basic_scraping()
    
    print("\n2. Testing click and wait:")
    test_click_and_wait()
    
    print("\n3. Testing number extraction:")
    test_number_extraction()
    
    print("\n4. Testing custom scraper:")
    test_custom_scraper()
    
    print("\nAll tests completed!") 