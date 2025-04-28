from typing import List
from .agent import Step, StepType

def parse_english_instructions(instructions: str) -> List[Step]:
    """
    Parse English instructions into a list of scraping steps.
    
    Args:
        instructions: String containing English instructions, one per line
        
    Returns:
        List of Step objects representing the scraping actions
    """
    steps = []
    for line in instructions.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
            
        if line.lower().startswith('go to'):
            url = line[6:].strip()
            steps.append(Step(type=StepType.GO_TO, target=url))
            
        elif line.lower().startswith('click'):
            # Extract the button/link text between quotes
            import re
            match = re.search(r'[\'"](.*?)[\'"]', line)
            if match:
                target = match.group(1)
                steps.append(Step(type=StepType.CLICK, target=f"text={target}"))
                
        elif line.lower().startswith('wait for'):
            # Extract the element description and remove "to load"
            target = line[9:].strip()
            target = target.replace(' to load', '')
            steps.append(Step(type=StepType.WAIT_FOR, target=target))
            
        elif line.lower().startswith('extract text'):
            # Extract the element description
            target = line[12:].strip()
            if target.startswith('from '):
                target = target[5:]
            steps.append(Step(type=StepType.EXTRACT_TEXT, target=target))
            
        elif line.lower().startswith('extract number'):
            # Extract the element description
            target = line[14:].strip()
            if target.startswith('from '):
                target = target[5:]
            steps.append(Step(type=StepType.EXTRACT_NUMBER, target=target))
            
    return steps 