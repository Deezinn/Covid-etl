ifeq ($(OS),Windows_NT)
    PYTHON=python
    ACTIVATE=call .venv\Scripts\activate
else
    PYTHON=python3
    ACTIVATE=. .venv/bin/activate
endif

run:
	$(ACTIVATE) && $(PYTHON) -m src.pipeline
