"""
Scraper Agent - A lightweight Python framework for defining website scraping behaviors in English.
"""

from .agent import ScraperAgent
from .parser import parse_english_instructions

__version__ = "0.1.0"
__all__ = ["ScraperAgent", "parse_english_instructions"] 