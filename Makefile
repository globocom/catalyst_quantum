clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt

test: clean deps
	@nosetests -sd --verbosity=2 --nologcapture
