import os
from datetime import date
from pathlib import Path

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_project_root() -> Path:
    return os.path.dirname(os.path.abspath(__file__))

def get_today():
    today = date.today()
    ts = today.strftime("%Y%m%d")
    return ts
