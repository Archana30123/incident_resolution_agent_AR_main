#!/usr/bin/env python
from datetime import datetime
import json
import sys
import os
import warnings
from pathlib import Path

from incident_resolution_agent.crew import IncidentResolutionAgent
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """Run the crew."""
    input_dir = Path('input') / 'Apache_2k.logs'
    output_dir = Path('output')
    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year),
        'log_input_path': str(input_dir),
        'output_path': str(output_dir),
    }
    try:
        IncidentResolutionAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
def train():
    """Train the crew for a given number of iterations. """
    inputs = { 
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    
    try:
        IncidentResolutionAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        IncidentResolutionAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        IncidentResolutionAgent().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
    
   
   


