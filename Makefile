#-*- coding: utf-8 -*-
all: init test

init:
	pip3 install -r requirements.txt

test:
	pytest .
