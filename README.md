# Create the python virtual enviroment
python3 -m venv venv
# Acyivate the python virtual enviroment
source venv/bin/activate
# Install the project requirements
pip install -r requirements.txt

# Install dev dependencies (testing)
pip install -r requirements-dev.txt

## Run the application
PYTHONPATH=src uvicorn app.main:app --reload

## Run the tests
pytest

# Gemini API Key Plataform
https://aistudio.google.com/app/projects
