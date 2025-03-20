import unittest
import os
from unittest.mock import patch
import sys
import pytest

# Add the src directory to the path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agent_coder import AgentCoder

class TestAgentCoder(unittest.TestCase):
    """Tests for the AgentCoder class"""
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"})
    def test_init_with_env_var(self):
        """Test initialization with environment variable"""
        agent = AgentCoder()
        self.assertEqual(agent.model, "gpt-4o-mini")
        self.assertEqual(agent.api_key, "test_key")
    
    def test_init_with_param(self):
        """Test initialization with parameter"""
        agent = AgentCoder(model="gpt-4", api_key="custom_key")
        self.assertEqual(agent.model, "gpt-4")
        self.assertEqual(agent.api_key, "custom_key")
    
    def test_init_no_key(self):
        """Test initialization with no key raises error"""
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError):
                AgentCoder()
    
    def test_generate_code(self):
        """Test code generation returns expected format"""
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"}):
            agent = AgentCoder()
            result = agent.generate_code("Sort a list")
            self.assertIn("Sort a list", result)
    
    def test_generate_code_with_language(self):
        """Test code generation with language specification"""
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"}):
            agent = AgentCoder()
            result = agent.generate_code("Sort a list", language="python")
            self.assertIn("python", result.lower())
            self.assertIn("Sort a list", result)
    
    def test_review_code(self):
        """Test code review returns list of comments"""
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"}):
            agent = AgentCoder()
            result = agent.review_code("def example(): pass")
            self.assertIsInstance(result, list)
            self.assertGreater(len(result), 0)
            self.assertIn("type", result[0])
            self.assertIn("message", result[0])
    
    def test_fix_bugs(self):
        """Test bug fixing returns modified code"""
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"}):
            agent = AgentCoder()
            code = "def divide(a, b): return a/b"
            result = agent.fix_bugs(code, "ZeroDivisionError")
            self.assertIn(code, result)
    
    def test_generate_documentation(self):
        """Test documentation generation returns modified code"""
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"}):
            agent = AgentCoder()
            code = "def add(a, b): return a + b"
            result = agent.generate_documentation(code)
            self.assertIn(code, result)
            self.assertIn("google", result.lower())
    
    def test_str_representation(self):
        """Test string representation of the agent"""
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"}):
            agent = AgentCoder(model="custom-model")
            self.assertEqual(str(agent), "AgentCoder(model=custom-model)")

if __name__ == "__main__":
    unittest.main()