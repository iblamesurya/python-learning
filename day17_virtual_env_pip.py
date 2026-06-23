# Day 17 - Virtual Environments, pip, and Project Structure
# (this file is mostly notes + runnable examples)

"""
=== Virtual Environments ===

Why? -> keeps project dependencies isolated from system Python

# create a virtual environment
python -m venv myenv

# activate it
# Windows:  myenv\\Scripts\\activate
# Mac/Linux: source myenv/bin/activate

# deactivate
deactivate

=== pip (Python Package Installer) ===

pip install requests         # install a package
pip install requests==2.31.0 # specific version
pip uninstall requests       # remove
pip list                     # see installed packages
pip freeze > requirements.txt  # save dependencies
pip install -r requirements.txt  # install from file

=== Project Structure (best practice) ===

my_project/
├── venv/               # virtual environment (don't commit this!)
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_utils.py
├── .gitignore
├── README.md
└── requirements.txt
"""

# --- practical: working with os and sys ---
import os
import sys
import platform

print("=== System Info ===")
print(f"Python version: {sys.version}")
print(f"Platform: {platform.system()} {platform.release()}")
print(f"Current directory: {os.getcwd()}")
print(f"Python executable: {sys.executable}")

# --- working with paths (os.path and pathlib) ---
from pathlib import Path

print("\n=== pathlib (modern way) ===")
current = Path(".")
print(f"Current: {current.resolve()}")

# list all .py files in current directory
py_files = sorted(current.glob("*.py"))
print(f"\nPython files in this repo:")
for f in py_files:
    size_kb = f.stat().st_size / 1024
    print(f"  {f.name:30s} ({size_kb:.1f} KB)")

print(f"\nTotal .py files: {len(py_files)}")

# --- environment variables ---
print("\n=== Environment Variables ===")
path = os.environ.get("PATH", "not set")
home = os.environ.get("USERPROFILE") or os.environ.get("HOME", "not set")
print(f"Home directory: {home}")
print(f"PATH entries: {len(path.split(os.pathsep))}")

# --- creating a simple .gitignore ---
print("\n=== Common .gitignore entries ===")
gitignore_items = [
    "venv/",
    "__pycache__/",
    "*.pyc",
    ".env",
    "*.egg-info/",
    "dist/",
    "build/",
    ".pytest_cache/",
]
for item in gitignore_items:
    print(f"  {item}")

print("\n✓ Day 17 complete! You now know how to manage Python projects properly.")
