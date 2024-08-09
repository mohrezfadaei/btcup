PYTHON=python3
PIP=pip3

ENV_DIR=venv
ENV_ACTIVATE_PATH=$(ENV_DIR)/source/activate

REQUIREMENTS=requirements.txt
REQUIREMENTS_DEV=requirements.dev.txt

venv:
		$(PYTHON) -m venv $(ENV_DIR)
		source $(ENV_ACTIVATE_PATH)

install:
		$(PIP) install -r $(REQUIREMENTS)

install-dev:
		$(PIP) install -r $(REQUIREMENTS_DEV)

format: install-dev
		isort . && black .

test:
		pytest
