# list recipes
help:
    just --list

now := `date +"%Y-%m-%d_%H.%M.%S"`
hostname := `uname -n`

PROD_DOCKER_COMPOSE := "docker-compose.prod.yml"

# install the project using pdm
install:
	export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && pip install pdm && pdm install

# lint the code
lint:
	pdm run mypy ./
	pdm run black ./ --check
	pdm run ruff ./

# format the code
format:
	pdm run isort --force-single-line-imports ./
	pdm run ruff --fix ./
	pdm run black ./

# Test app with pytest outside of docker (with fresh data/test.db from tests/conftest.py)
test:
	pdm run pytest -vv tests

pre-commit:
	pre-commit run --all-files

# Format and then run lint and test targets (like CI does)
ci: format lint test pre-commit

# Open the URL for issues
issues:
	open https://github.com/iancleary/fastapi_cors/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc

# Open the URL for pull requests
prs:
	open https://github.com/iancleary/fastapi_cors/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc