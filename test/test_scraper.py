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

def test_interactive_scraping():
    """Test clicking and waiting for elements."""
    instructions = """
    Go to https://www.python.org
    Click the 'Downloads' link
    Wait for #downloads
    Extract text from #downloads h1
    """
    
    with ScraperAgent(parse_english_instructions(instructions)) as agent:
        result = agent.run()
        print(f"Interactive scraping result: {result}")
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

if __name__ == "__main__":
    print("Running scraper agent tests...")
    print("\n1. Testing basic scraping:")
    test_basic_scraping()
    
    print("\n2. Testing interactive scraping:")
    test_interactive_scraping()
    
    print("\n3. Testing number extraction:")
    test_number_extraction()
    
    print("\nAll tests completed!") 