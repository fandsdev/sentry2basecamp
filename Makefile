lint:
	flake8 src
	mypy src

test:
	cd src && pytest
