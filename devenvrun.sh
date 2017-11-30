# export ESHOP_ENV=dev
docker-compose run --rm --service-ports python bash
# or docker-compose run --rm --service-ports -e ESHOP_ENV=dev python bash
