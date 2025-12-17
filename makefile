ifeq ($(OS),Windows_NT)
    PYTHON=..\ .venv\Scripts\python
else
    PYTHON=../.venv/bin/python
endif

run:
	cd src && $(PYTHON) -m app.main
