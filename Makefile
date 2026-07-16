.PHONY: install html serve clean

install:            ## install build dependencies
	pip install -r requirements.txt

html:               ## build the site
	sphinx-build -b html docs docs/_build/html

serve: html         ## build and preview locally at http://localhost:8000
	python -m http.server -d docs/_build/html

clean:
	rm -rf docs/_build
