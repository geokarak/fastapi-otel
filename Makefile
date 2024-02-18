.ONESHELL:

.PHONY: venv
venv: pyproject.toml
	rm -rf ./.venv
	python -m venv .venv
	./.venv/bin/pip install --upgrade pip
	./.venv/bin/python -m pip install -e .