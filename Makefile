.PHONY: clean clean-test clean-pyc clean-build docs help

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/netvis.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ netvis */migrations/*
	$(MAKE) -C docs clean
	$(MAKE) -C docs html