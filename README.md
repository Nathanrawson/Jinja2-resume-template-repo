# Jinja2 Template Tester

This project provides a minimal setup for testing Jinja2 HTML templating.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python python render_template.py cv-template.html jsonContext.json > rendered.html
```

The script renders the given template with the provided context (if any) and outputs the result to stdout.
