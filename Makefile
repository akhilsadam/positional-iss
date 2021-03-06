NAME=akhilsadam
PACKAGE=positional-iss
GITHUB=git@github.com:akhilsadam/positional-iss.git
TAG=0.0.2
PYTEST=testall.py
APIFILE=doc/api.md
SEARCH=\\n
REPLACE=\n

rapid: kill clean build run

rapidtest: kill clean build test

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
	- rm doc/r/log_r.txt

build:
	docker build -t ${NAME}/${PACKAGE}:${TAG} .

test:
	docker run -it --rm ${NAME}/${PACKAGE}:${TAG} ${PYTEST}
run:
	docker run --name "${PACKAGE}" -p 5026:5026 ${NAME}/${PACKAGE}:${TAG} wsgi.py

push:
	docker login docker.io
	docker push ${NAME}/${PACKAGE}:${TAG}


# [WARNING] The following commands may require unlisted dependencies and are not part of the supported API.
# Notes for developer convenience:
#	 May need to be done on Windows due to some npm issues.
#	 Requires R and some packages
#	 Some paths will need to be modified (this is due to a path issue on our end).

api:
# container must be running!
	curl -X GET "http://localhost:5026/api/save" -H "accept: application/json" -o "${APIFILE}"

readme:
	git status
	npx @appnest/readme generate
	git status
	git add .
	- git commit -am "[auto] update readme"
	- git push

pdf:
	"C:\Program Files\R\R-4.0.3\bin\Rscript" -e 'pagedown::chrome_print('"'doc/r/article.rmd'"')' > doc/r/log_r.txt
	mv doc/r/article.pdf app/static/doc/article.pdf
	mv doc/r/article.html app/static/doc/article.html

commit:
	git status
	git add .
	git commit -am "[glob] ${msg}"
	git push

all: 
	pytest 
	make kill 
	make clean 
	make build
	make test
	make run 
	# run doc in a win terminal

doc:
	make api
	make pdf
	make readme