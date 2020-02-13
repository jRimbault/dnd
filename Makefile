.PHONY: lint
lint:
	black dnd dnd_attributes.py tests
	isort --recursive .
	autoflake -r --in-place --remove-unused-variables .
	mypy dnd

.PHONY: lint
check-only:
	black --check dnd dnd_attributes.py tests
	isort --check-only --recursive .
	autoflake --check -r --in-place --remove-unused-variables .
	mypy dnd

.PHONY: tests
tests:
	pytest --cov=dnd --cov-report xml:tests-results/cov.xml tests

.PHONY: tests-show
tests-show:
	pytest --cov=dnd tests

.PHONY: env
env:
	python3.8 -m venv .venv
	pip install -r requirements-dev.txt
	pip install -r requirements.txt
