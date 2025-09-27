# DevSecOps FastAPI Demo

![CI](https://github.com/KIRANS420/devsec-fastapi-demo/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/KIRANS420/devsec-fastapi-demo/actions/workflows/codeql-analysis.yml/badge.svg)
<img alt="gitleaks badge" src="https://img.shields.io/badge/protected%20by-gitleaks-blue">

A demonstration project showcasing DevSecOps practices with FastAPI.

## Features

- FastAPI web application
- Security scanning with Bandit
- Code quality checks with Ruff
- Pre-commit hooks for automated checks
- Dependency vulnerability scanning
- GitHub CodeQL analysis
- Secret scanning with gitleaks

## Getting Started

### Prerequisites

- Python 3.11+
- pip or poetry

### Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Unix)
4. Install dependencies: `pip install -r requirements.txt`
5. Install development dependencies: `pip install -r requirements-dev.txt`

### Running the Application

```bash
uvicorn app.main:app --reload
```

### Running Tests

```bash
pytest
```

### Security Scanning

```bash
bandit -r app/
pip-audit
```

## Development

### Pre-commit Hooks

Install pre-commit hooks:

```bash
pre-commit install
```

This will automatically run code quality and security checks before each commit.
