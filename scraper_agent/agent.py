from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel
from playwright.sync_api import sync_playwright, Page

class StepType(str, Enum):
    GO_TO = "GO_TO"
    CLICK = "CLICK"
    WAIT_FOR = "WAIT_FOR"
    EXTRACT_TEXT = "EXTRACT_TEXT"
    EXTRACT_NUMBER = "EXTRACT_NUMBER"

class Step(BaseModel):
    type: StepType
    target: str
    value: Optional[str] = None

class ScraperAgent:
    def __init__(self, steps: List[Step]):
        self.steps = steps
        self.page: Optional[Page] = None
        self.playwright = None
        self.browser = None

    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.page = self.browser.new_page()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def run(self) -> Union[str, int, None]:
        if not self.page:
            raise RuntimeError("ScraperAgent must be used as a context manager")

        result = None
        for step in self.steps:
            if step.type == StepType.GO_TO:
                self.page.goto(step.target)
            elif step.type == StepType.CLICK:
                self.page.click(step.target)
            elif step.type == StepType.WAIT_FOR:
                self.page.wait_for_selector(step.target)
            elif step.type == StepType.EXTRACT_TEXT:
                result = self.page.inner_text(step.target)
            elif step.type == StepType.EXTRACT_NUMBER:
                text = self.page.inner_text(step.target)
                # Extract first number found in the text
                import re
                numbers = re.findall(r'\d+', text)
                result = int(numbers[0]) if numbers else None

        return result 