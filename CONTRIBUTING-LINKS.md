## About link validation (automated CI)

This repo runs an automated workflow that checks Markdown links.

### Run locally

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

pip install requests
python scripts/check_links.py
```
