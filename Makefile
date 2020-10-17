files_to_fmt ?= api_keys helpers modules templates app.py log.py main.py
files_to_check ?= api_keys helpers modules templates app.py log.py main.py

build:
	docker build -t mami-webinars .

run:
	docker run --rm --name mami-worker -d mami-webinars

stop:
	docker stop mami-worker

logs:
	docker logs -f mami-worker

## Format all
fmt: format
format: rm_imports isort black docformatter add-trailing-comma


## Check code quality
chk: check
lint: check
check: flake8 black_check docformatter_check safety bandit


## Remove unused imports
rm_imports:
	autoflake -ir --remove-unused-variables \
		--ignore-init-module-imports \
		--remove-all-unused-imports \
		${files_to_fmt}


## Sort imports
isort:
	isort -rc ${files_to_fmt}


## Format code
black:
	black ${files_to_fmt}


## Check code formatting
black_check:
	black --check ${files_to_check}


## Format docstring
docformatter:
	docformatter -ir ${files_to_fmt}


## Check docstring formatting
docformatter_check:
	docformatter -cr ${files_to_check}


## Check pep8
flake8:
	flake8 ${files_to_check}


## Check typing
mypy:
	mypy ${files_to_check}


## Check if all dependencies are secure and do not have any known vulnerabilities
safety:
	safety check --bare --full-report


## Check code security
bandit:
	bandit -r ${files_to_check} -x tests

## Add trailing comma
add-trailing-comma:
	find ${files_to_fmt} -name "*.py" -exec add-trailing-comma '{}' \;