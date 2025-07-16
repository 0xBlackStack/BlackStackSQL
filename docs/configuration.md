# BlackStackSQL Configuration Guide

## Overview

BlackStackSQL is a highly configurable SQL injection automation tool. This guide covers all configuration options, from basic setup to advanced customization.

## Basic Configuration

### Installation

```bash
git clone https://github.com/yourname/blackstacksql.git
cd blackstacksql
python setup.py install
```

### Running the Tool

```bash
python3 main.py --url http://target.com?id=1 --scan
```

## Configuration Files

### .gitignore

Excludes unnecessary files from version control:

```plaintext
# Python
__pycache__/
*.py[cod]
*.egg
*.egg-info/
*.pyo
*.pyd
*.so
*.log

# Virtual Environment
venv/
env/
ENV/
.venv/

# OS and IDE
.DS_Store
Thumbs.db
.idea/
.vscode/

# BlackStackSQL Runtime
sessions/
*.json
*.csv
*.txt
*.dump
*.output
*.log

# Build/Dist Files
*.exe
*.zip
dist/
build/
*.spec

# Git itself
.gitignore
```

### .gitattributes

Enforces line-ending consistency and file classification:

```plaintext
# top-most EditorConfig file
root = true

# Apply to all files
[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

# Python files
[*.py]
indent_style = space
indent_size = 4

# JSON and config files
[*.json]
indent_style = space
indent_size = 2

# Markdown/README
[*.md]
trim_trailing_whitespace = false

# Shell scripts
[*.sh]
indent_style = space
indent_size = 2
```

### .editorconfig

Ensures consistent code style across editors:

```plaintext
# top-most EditorConfig file
root = true

# Apply to all files
[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

# Python files
[*.py]
indent_style = space
indent_size = 4

# JSON and config files
[*.json]
indent_style = space
indent_size = 2

# Markdown/README
[*.md]
trim_trailing_whitespace = false

# Shell scripts
[*.sh]
indent_style = space
indent_size = 2
```

### .pre-commit-config.yaml

Automated code quality checks:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict

  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks:
      - id: black
        language_version: python3.8

  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        additional_dependencies: [flake8-bugbear]
```

### .flake8

Linting rules:

```ini
[flake8]
max-line-length = 100
exclude = .git,__pycache__,venv,sessions,dist,build
ignore = E203, E266, E501, W503
max-complexity = 10
```

### pyproject.toml

Project metadata and dependencies:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "blackstacksql"
version = "1.0.0"
authors = [
    { name = "Reflex Coder / BlackStack Unit", email = "reflex@blackstack.io" }
]
description = "Advanced Modular SQL Injection Toolkit"
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "requests",
    "colorama"
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]

[tool.black]
line-length = 100
target-version = ['py38']
skip-string-normalization = false
include = '\.pyi?$'
exclude = '''
/(
    \.eggs
  | \.git
  | \.mypy_cache
  | \.pytest_cache
  | build
  | dist
  | sessions
  | venv
)/
'''
```

## Advanced Configuration

### Custom Payloads

Add your own SQL injection payloads in the `payloads/` directory. Each file should contain one payload per line.

### Proxy Configuration

Configure proxies in a text file and pass the file path to the `--proxy` option:

```bash
python3 main.py --url http://target.com?id=1 --proxy /path/to/proxies.txt
```

### Custom Headers and Cookies

Pass custom headers and cookies using the `--header` and `--cookie` options:

```bash
python3 main.py --url http://target.com?id=1 --header "X-Custom-Header: value" --cookie "sessionid=abc123"
```

### WAF Bypass

Enable WAF bypass techniques using the `--waf-bypass` option:

```bash
python3 main.py --url http://target.com?id=1 --waf-bypass
```

### Resuming Sessions

Resume a previous scan using the `--resume` option:

```bash
python3 main.py --resume /path/to/session
```

### Saving Results

Save scan results in JSON or HTML format:

```bash
python3 main.py --url http://target.com?id=1 --save-json
python3 main.py --url http://target.com?id=1 --html-log
```

## Troubleshooting

### Common Issues

- **Proxy Errors**: Ensure the proxy file contains valid proxies and that the proxies are reachable.
- **WAF Detection**: If the tool is blocked by a WAF, try enabling WAF bypass or using a proxy.
- **Timeouts**: Increase the timeout using the `--timeout` option (if implemented).

### Logging

All actions are logged to the console and can be saved to a file using the `--output` option:

```bash
python3 main.py --url http://target.com?id=1 --output /path/to/log.txt
```

## Contributing

Contributions are welcome. Please follow the existing code style and add tests for new features.

### Adding New Modules

1. Create a new file in the `modules/` directory.
2. Implement the required functionality.
3. Add the module to the main.py file.
4. Update the documentation.

### Adding New Payloads

1. Create a new file in the `payloads/` directory.
2. Add your payloads, one per line.
3. Update the documentation to reflect the new payloads.

### Reporting Issues

Please report any issues or feature requests on the GitHub repository.
