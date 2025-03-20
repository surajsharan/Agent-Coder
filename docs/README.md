# Agent Coder Documentation

## Overview

Agent Coder is a powerful AI-powered coding assistant that helps developers write, review, and improve code using advanced language models.

## API Reference

### AgentCoder Class

**Constructor**

```python
AgentCoder(model="gpt-4o-mini", api_key=None)
```

- `model`: The LLM model to use
- `api_key`: Optional API key (will use env var if not provided)

**Methods**

- `generate_code(prompt, language=None)`: Generate code based on the given prompt
- `review_code(code)`: Review code and provide suggestions
- `fix_bugs(code, error_message=None)`: Fix bugs in the provided code
- `generate_documentation(code, doc_style="google")`: Generate documentation for code

## Usage Examples

### Basic Usage

```python
from agent_coder import AgentCoder

# Initialize with API key
agent = AgentCoder()

# Generate code
code = agent.generate_code("Create a function to calculate factorial")
print(code)
```

### Advanced Usage

```python
# Initialize with specific model
agent = AgentCoder(model="gpt-4")

# Generate Python code
python_code = agent.generate_code(
    "Create a function to find prime numbers up to n",
    language="python"
)

# Review code
suggestions = agent.review_code(python_code)
for suggestion in suggestions:
    print(f"{suggestion['type']}: {suggestion['message']}")

# Fix a bug
error_msg = "TypeError: 'int' object is not iterable"
fixed_code = agent.fix_bugs(python_code, error_msg)

# Generate documentation
documented_code = agent.generate_documentation(fixed_code, doc_style="numpy")
```

## Development Guide

See the [main README.md](../README.md) for development setup instructions.