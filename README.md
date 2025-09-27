# DevSecOps FastAPI Demo

![CI](https://github.com/KIRANS420/devsec-fastapi-demo/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/KIRANS420/devsec-fastapi-demo/actions/workflows/codeql-analysis.yml/badge.svg)
<img alt="gitleaks badge" src="https://img.shields.io/badge/protected%20by-gitleaks-blue">

## 🚀 Live Demo

> **🌐 Hosted Application**: [https://devsec-fastapi-demo.onrender.com/](https://devsec-fastapi-demo.onrender.com/)
> 
> **📡 API Endpoint**: `GET /` - Returns health status and version information
> 
> **🔍 Repository**: [https://github.com/KIRANS420/devsec-fastapi-demo](https://github.com/KIRANS420/devsec-fastapi-demo)

### Quick Test
```bash
curl https://devsec-fastapi-demo.onrender.com/
# Expected: {"ok":true,"msg":"hello from devsec-fastapi-demo","version":"1.0.0"}
```

A comprehensive demonstration project showcasing **DevSecOps** (Development Security Operations) practices with FastAPI. This project implements a complete security-first development pipeline with automated testing, security scanning, and deployment.

## 🎯 What This Project Demonstrates

This repository serves as a **complete example** of modern DevSecOps practices, including:

### ✅ Complete DevSecOps Stack

- **🔧 FastAPI Web Application**: Production-ready REST API with health checks
- **🛡️ Local Quality Gates**: Pre-commit hooks for code quality and security
- **🚀 CI/CD Pipeline**: Automated testing, security scanning, and deployment
- **🔍 Security Scanning**: Multiple layers of security analysis
- **📋 Compliance**: Branch protection and required status checks
- **☁️ Production Deployment**: Live application on Render

### 🔒 Security Features

- **Code Quality**: Ruff linting and formatting
- **Security Scanning**: Bandit for Python security vulnerabilities
- **Secret Detection**: Gitleaks and detect-secrets for credential scanning
- **Dependency Auditing**: pip-audit for known vulnerabilities
- **Advanced Analysis**: GitHub CodeQL for comprehensive security scanning
- **Branch Protection**: Prevents insecure code from reaching production

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **Git**
- **pip** or **poetry**

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/KIRANS420/devsec-fastapi-demo.git
cd devsec-fastapi-demo

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 2. Run the Application

```bash
# Start the development server
uvicorn app.main:app --reload

# Test the API
curl http://localhost:8000/
# Expected: {"ok":true,"msg":"hello from devsec-fastapi-demo","version":"1.0.1","status":"workflows-tested"}
```

### 3. Run Tests and Security Scans

```bash
# Run tests
pytest

# Run security scans
bandit -r app/
pip-audit -r requirements.txt
detect-secrets audit .secrets.baseline

# Run linting
ruff check .
ruff format .
```

### 4. Setup Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Test by making a change
echo "# Test" >> test.md
git add test.md
git commit -m "test: verify pre-commit hooks"
```

## 🏗️ Project Structure

```
devsec-fastapi-demo/
├── app/
│   └── main.py              # FastAPI application
├── tests/
│   └── test_main.py         # Test suite
├── .github/
│   └── workflows/
│       ├── ci.yml           # CI/CD pipeline
│       ├── codeql-analysis.yml  # CodeQL security analysis
│       └── secret-scan.yml  # Secret scanning
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
├── pyproject.toml          # Ruff configuration
├── .pre-commit-config.yaml # Pre-commit hooks
├── .secrets.baseline       # Secret detection baseline
└── README.md               # This file
```

## 🔧 DevSecOps Pipeline

### 1. **Local Development**
- Pre-commit hooks run automatically on every commit
- Code formatting with Ruff
- Security scanning with Bandit
- Secret detection with detect-secrets

### 2. **CI/CD Pipeline** (GitHub Actions)
- **CI Workflow**: Runs on every push and PR
  - Code linting and formatting
  - Unit tests with pytest
  - Security scanning with Bandit
  - Dependency vulnerability scanning with pip-audit
- **CodeQL Analysis**: Advanced security analysis
- **Secret Scanning**: Gitleaks for credential detection

### 3. **Branch Protection**
- Requires all status checks to pass
- Prevents direct pushes to main branch
- Enforces pull request reviews

### 4. **Production Deployment**
- Automated deployment to Render
- Live application monitoring

## 🧪 Testing the Application

### Local Testing

```bash
# Test the API endpoint
curl http://localhost:8000/

# Run the test suite
pytest -v

# Check code coverage (if pytest-cov is installed)
pytest --cov=app
```

### Live Application Testing

```bash
# Test the live application
curl https://devsec-fastapi-demo.onrender.com/

# Expected response:
# {
#   "ok": true,
#   "msg": "hello from devsec-fastapi-demo",
#   "version": "1.0.1",
#   "status": "workflows-tested"
# }
```

### Security Testing

```bash
# Run all security scans
bandit -r app/ --severity-level medium
pip-audit -r requirements.txt --format table
detect-secrets audit .secrets.baseline

# Check for security alerts in GitHub
# Visit: https://github.com/KIRANS420/devsec-fastapi-demo/security
```

## 📊 Monitoring and Verification

### GitHub Actions Status
- **All Workflows**: [Actions Dashboard](https://github.com/KIRANS420/devsec-fastapi-demo/actions)
- **CI Workflow**: [CI Pipeline](https://github.com/KIRANS420/devsec-fastapi-demo/actions/workflows/ci.yml)
- **CodeQL Analysis**: [Security Analysis](https://github.com/KIRANS420/devsec-fastapi-demo/actions/workflows/codeql-analysis.yml)
- **Secret Scanning**: [Secret Detection](https://github.com/KIRANS420/devsec-fastapi-demo/actions/workflows/secret-scan.yml)

### Security Dashboard
- **Security Tab**: [Security Overview](https://github.com/KIRANS420/devsec-fastapi-demo/security)
- **CodeQL Alerts**: Should show clean scan results
- **Dependabot**: Dependency update notifications

### Application Monitoring
- **Live Application**: [https://devsec-fastapi-demo.onrender.com/](https://devsec-fastapi-demo.onrender.com/)
- **Health Check**: `GET /` endpoint for monitoring

## 🛠️ Development Workflow

### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code following the project standards
   - Add tests for new functionality
   - Update documentation as needed

3. **Test locally**
   ```bash
   pytest
   ruff check .
   bandit -r app/
   ```

4. **Commit with pre-commit hooks**
   ```bash
   git add .
   git commit -m "feat: add your feature"
   ```

5. **Push and create PR**
   ```bash
   git push -u origin feature/your-feature-name
   # Create PR on GitHub
   ```

6. **Merge after all checks pass**
   - All CI/CD checks must pass
   - Code review approval required
   - No security alerts

## 🔍 Troubleshooting

### Common Issues

**Pre-commit hooks failing:**
```bash
# Skip hooks temporarily
git commit -m "your message" --no-verify

# Update pre-commit hooks
pre-commit autoupdate
```

**Security scans finding issues:**
```bash
# Review Bandit findings
bandit -r app/ -f json -o bandit-report.json

# Update secret baseline
detect-secrets scan > .secrets.baseline
```

**Workflow failures:**
- Check the [Actions tab](https://github.com/KIRANS420/devsec-fastapi-demo/actions) for detailed logs
- Ensure all dependencies are properly listed in requirements files
- Verify branch protection rules are correctly configured

## 📚 Learning Resources

### DevSecOps Concepts
- **Shift Left Security**: Security checks in development phase
- **Infrastructure as Code**: All configurations in version control
- **Continuous Security**: Ongoing vulnerability scanning
- **Automated Compliance**: Enforced security policies

### Tools Used
- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern Python web framework
- **[Ruff](https://docs.astral.sh/ruff/)**: Fast Python linter and formatter
- **[Bandit](https://bandit.readthedocs.io/)**: Python security linter
- **[CodeQL](https://codeql.github.com/)**: GitHub's semantic code analysis
- **[Gitleaks](https://github.com/gitleaks/gitleaks)**: Secret scanning
- **[Render](https://render.com/)**: Cloud deployment platform

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests and security scans pass
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Success Indicators

When everything is working correctly, you should see:

- ✅ **Green badges** in the README
- ✅ **Passing workflows** in GitHub Actions
- ✅ **No security alerts** in the Security tab
- ✅ **Live application** responding correctly
- ✅ **All tests passing** locally and in CI
- ✅ **Branch protection** preventing unsafe merges

## 📝 Project Reflection

This DevSecOps FastAPI demo project provided valuable insights into modern secure software development practices. The most challenging aspect was configuring the pre-commit hooks with detect-secrets and bandit, which required careful environment setup and dependency management. However, the most rewarding part was seeing the complete security pipeline in action - from local development with pre-commit hooks to automated CI/CD workflows and live deployment, demonstrating how security can be seamlessly integrated into every stage of the development lifecycle.

## 🤖 AI Tools and Development Process

This project was developed using **GitHub Student Developer Pack** resources and AI-assisted development tools:

### GitHub Copilot Integration
- **Code Generation**: Used GitHub Copilot for generating boilerplate FastAPI code, test cases, and configuration files
- **Documentation**: Leveraged Copilot's suggestions for writing comprehensive README sections and inline comments
- **Debugging**: Utilized Copilot's code analysis capabilities to identify and fix workflow configuration issues
- **Best Practices**: Applied Copilot's suggestions for following Python and FastAPI best practices

### Development Workflow with AI
1. **Initial Setup**: Copilot helped generate the basic FastAPI application structure and test framework
2. **Security Configuration**: AI assistance in setting up pre-commit hooks, GitHub Actions workflows, and security scanning tools
3. **Documentation**: Copilot provided templates and suggestions for comprehensive documentation
4. **Troubleshooting**: Used AI to debug workflow failures and configuration issues

### Tools and Resources Used
- **GitHub Student Developer Pack**: Access to premium GitHub features and tools
- **GitHub Copilot**: AI pair programming assistant for code generation and suggestions
- **Cursor AI**: AI-powered code editor for enhanced development experience
- **GitHub Actions**: Free CI/CD with student pack benefits
- **Render**: Free hosting for the live demo application

The combination of AI tools and the GitHub Student Developer Pack made it possible to rapidly prototype and deploy a production-ready DevSecOps pipeline, demonstrating how modern development tools can accelerate secure software delivery.

---

**Built with ❤️ using AI-assisted development and GitHub Student Developer Pack**
