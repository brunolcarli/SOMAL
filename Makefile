run:
	python3 manage.py runserver 0.0.0.0:5042 --settings=somal.settings.common

train:
	python3 manage.py daemons --model train --settings=somal.settings.common

install:
	pip3 install -r somal/requirements/common.txt

replit:
	make install
	make run
