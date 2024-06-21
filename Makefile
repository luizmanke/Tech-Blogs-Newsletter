DOCKER_IMAGE := tech-blogs-newsletter
DOCKER_RUN := docker run --rm --tty

build:
	docker build -t $(DOCKER_IMAGE) .

run: build
	$(DOCKER_RUN) \
		-e RECEIVER_EMAILS \
		-e SENDER_EMAIL \
		-e SENDER_PASSWORD \
		$(DOCKER_IMAGE)

unit-tests: build
	$(DOCKER_RUN) -v $(PWD)/tests/unit:/app/tests/unit $(DOCKER_IMAGE) pytest

system-tests: build
	$(DOCKER_RUN) -v $(PWD)/tests/system:/app/tests/system $(DOCKER_IMAGE) pytest

tests: unit-tests system-tests
