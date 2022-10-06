# docker build settings
IMAGE_LABEL="msa_{{cookiecutter.app_name}}"
BRANCHNAME="$([ -z "$1"] && echo localhost || echo $1)"
LATEST_TAG="${BRANCHNAME}-latest"
IMAGE_LABEL_LATEST="${IMAGE_LABEL}:${LATEST_TAG}"
rm -f ../devops/.env
echo "Building Docker image -> ${IMAGE_LABEL} ...."
docker build -t ${IMAGE_LABEL_LATEST} -f ../devops/service.Dockerfile ../.

export IMAGE_LABEL_LATEST