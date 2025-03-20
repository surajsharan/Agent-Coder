from setuptools import setup, find_packages

setup(
    name="agent-coder",
    version="0.1.0",
    description="AI-powered coding assistant that helps developers write, review, and improve code",
    author="Agent Coder Team",
    author_email="your-email@example.com",
    url="https://github.com/surajsharan/Agent-Coder",
    packages=find_packages(include=["src", "src.*"]),
    package_dir={"agent_coder": "src"},
    install_requires=[
        "autogen-agentchat>=0.1.0",
        "autogen-core>=0.1.0",
        "autogen-ext>=0.1.0",
        "python-dotenv>=0.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)