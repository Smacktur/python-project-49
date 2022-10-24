package-install: build publish
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	poetry build

publish:
	poetry publish --dry-run