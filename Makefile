NAME=akhilsadam
PACKAGE=positional-iss
GITHUB=git@github.com:akhilsadam/positional-iss.git
TAG=0.0.1
#PYTESTS=<>

all: kill clean build test run push

rapid: kill clean build run

iterate: kill clean build test run

images:
	docker images | grep ${PACKAGE}

ps:
	docker ps -a | grep ${PACKAGE}

kill:
	- docker stop ${PACKAGE}

clean:
	- docker rm ${PACKAGE}
	- rm __pycache__/ -r
	- rm app/.pytest_cache/ -r

build:
	docker build -t ${NAME}/${PACKAGE}:${TAG} .

test:
	docker run -it --rm ${NAME}/${PACKAGE}:${TAG} pytest ${PYTESTS}

run:
	docker run --name "${PACKAGE}" -p 5026:5026 ${NAME}/${PACKAGE}:${TAG} wsgi.py

push:
	docker login docker.io
	docker push ${NAME}/${PACKAGE}:${TAG}

# [WARNING] The following commands may require unlisted dependencies and are not part of the supported API.

readme:
	git status
	npx @appnest/readme generate
	git status
	git add .
	git commit -am "[auto] update readme"
	git push

commit:
	git status
	git add .
	git commit -am "[glob] ${msg}"
	git push