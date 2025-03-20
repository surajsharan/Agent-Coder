"""
Example usage of the Agent Coder package.

To run this example:
1. Create a .env file with your OPENAI_API_KEY
2. Run this script with: python example.py
"""

import os
from dotenv import load_dotenv
from src.agent_coder import AgentCoder

# Load environment variables from .env file
load_dotenv()

def main():
    # Ensure API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables or .env file.")
        print("Please set your OpenAI API key before running this example.")
        return
    
    print("Initializing Agent Coder...")
    agent = AgentCoder()
    
    # Example 1: Generate Python code
    prompt = "Create a function to calculate the Fibonacci sequence up to n"
    print(f"\nExample 1: Generating code for: {prompt}")
    code = agent.generate_code(prompt, language="python")
    print("\nGenerated Code:")
    print(code)
    
    # Example 2: Review code
    print("\nExample 2: Reviewing code")
    sample_code = """
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
    """
    print("\nCode to review:")
    print(sample_code)
    
    review = agent.review_code(sample_code)
    print("\nReview results:")
    for comment in review:
        print(f"- {comment['type']}: {comment['message']}")
    
    # Example 3: Generate documentation
    print("\nExample 3: Generating documentation")
    documentation = agent.generate_documentation(sample_code)
    print("\nGenerated documentation:")
    print(documentation)
    
    print("\nAgent Coder examples completed successfully!")

if __name__ == "__main__":
    main()