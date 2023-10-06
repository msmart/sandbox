push:
	echo ${CR_PAT} | docker login ghcr.io -u ${GITHUB_USER} --password-stdin
	docker build . -t ghcr.io/${GITHUB_USER}/${GITHUB_PROJECT}:$(git rev-parse HEAD)
	docker push ghcr.io/${GITHUB_USER}/${GITHUB_PROJECT}:$(git rev-parse HEAD)
