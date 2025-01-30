# Backend

Backend is REST API which is build using Python and FastAPI framework.

## Requirements
- Python 3.12.8

## Installation

First create virtual environment:

```bash
python -m venv .venv
```

and then switch to it:
```bash
source .venv/bin/activate
```

After that install all needed packages:
```bash
pip install -r requirements.txt
```

## Usage

Recommended way to run backend for development is using provided `launch.json`. Just go to Run and Debug inside Visual Studio Code and run it. If you want to run it from terminal, you can do so by typing:
```bash
uvicorn src.main:app --reload
```