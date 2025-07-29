#!/usr/bin/env python3
"""Render a Jinja2 HTML template with optional JSON context.

Usage:
    python render_template.py TEMPLATE_FILE [CONTEXT_JSON_FILE]
"""

import sys
import json
from jinja2 import Environment, FileSystemLoader

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    template_path = sys.argv[1]
    context = {}
    if len(sys.argv) == 3:
        with open(sys.argv[2]) as f:
            context = json.load(f)
    loader = FileSystemLoader(searchpath='.')
    env = Environment(loader=loader)
    template = env.get_template(template_path)
    output = template.render(**context)
    print(output)

if __name__ == '__main__':
    main()