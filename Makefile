build:
	docker build -t mami-webinars .

run:
	docker run --rm --name mami-worker -d mami-webinars

stop:
	docker stop mami-worker