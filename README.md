- make sure to run venv to install all requirements from requirements.txt
  -begin by writing: python -m venv venv

  - to activate: - windows: venv\Scripts\activate - macOS: source venv/bin/activate

- setup keys/urls in a .env file

- to run app, cd app, then run uvicorn main:app --reload