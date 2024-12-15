install:
	uv sync
brain-games:
	uv run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	uv tool install dist/*.whl
lint:
	poetry run flake8 brain_games
