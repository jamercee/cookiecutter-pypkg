# ----------------------------------------------------------------------------
# Define system macros
# ----------------------------------------------------------------------------
ifeq ($(OS), Windows_NT)
	OSTYPE := Windows
	PYTHON := C:/Python27/python.exe
	PYLINT := C:/Python27/Scripts/pylint.exe
	FLAKE := C:/Python27/Scripts/flake8.exe
	NOSETESTS := C:/Python27/Scripts/nosetests.exe
else
	OSTYPE := $(shell uname)
	PYTHON := pthon2.7
	PYLINT := pylint
	FLAKE := flake8
	NOSETESTS := nosetests
endif

# ----------------------------------------------------------------------------
# Define $(BROWSER) for reading documentation with web browser
# ----------------------------------------------------------------------------
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

# ----------------------------------------------------------------------------
# Rule to compile python *.py -> *.pyc
# ----------------------------------------------------------------------------
%.pyc:	%.py
	@echo Check $<
	@$(PYLINT) -rn --rcfile pylint.rc $<
	@$(FLAKE) $<
	@$(PYTHON) -c 'import py_compile; py_compile.compile("$<")'

# ----------------------------------------------------------------------------

SRCS := $(wildcard src/{{cookiecutter.project_slug}}/*.py) $(wildcard tests/*.py)
TGTS := $(patsubst %.py, %.pyc,$(SRCS))

.PHONY: clean clean-build clean-docs clean-pyc comp debug docs help 

all: comp

help:
	@echo "comp - perform static analysis (default target)"
	@echo "tests - run unittests"
	@echo "docs - generate html documentation"
	@echo "dist - build package"
	@echo "install - install package to site-packages"
	@echo "viewdocs - generate & view html documentation"
	@echo "clean - remove all built components"
	@echo "clean-build - remove all built outputs"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "debug - generate Makefile diagnostic output"

comp: $(TGTS)

tests: comp
	@$(NOSETESTS)

docs:
	@$(MAKE) -C docs html

viewdocs: docs
	$(BROWSER) docs/_build/html/index.html

dist: tests docs
	@$(PYTHON) setup.py sdist

install: tests docs
	@$(PYTHON) setup.py install

clean: clean-build clean-pyc clean-docs

clean-build:
	-rm -fr build/ dist/ .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc:
	find . -name '*.py[co]' -o -name '*.pln' -o -name '~*' -exec -f {} +
	find . -name '__pycache__' -exec -fr {} +

clean-docs:
	$(MAKE) -C docs clean
	
debug:
	@echo OSTYPE:: $(OSTYPE)
	@echo PYTHON:: $(PYTHON)
	@echo PYLINT:: $(PYLINT)
	@echo FLAKE:: $(FLAKE)
	@echo Source files found::
	@echo $(SRCS)
	@echo Targets to build::
	@echo $(TGTS)
