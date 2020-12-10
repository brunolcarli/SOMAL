run:
	python3 manage.py runserver 0.0.0.0:5042

train:
	python3 manage.py daemons --model train
