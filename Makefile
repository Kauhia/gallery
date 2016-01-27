
datet = $(shell date +%Y%m%d%H%M%S)

python_bin = python3.4

ENV: ENV/bin/activate

ENV/bin/activate: requirements.txt
	test -d ENV || virtualenv --python=$(python_bin) --no-site-packages --distribute ENV
	. ENV/bin/activate; pip install -Ur requirements.txt
	touch ENV/bin/activate
	@echo Now you must run: source ENV/bin/activate to activate the virtualenv

clear:
	rm -rf ENV

run:
	python manage.py runserver
.PHONY: run