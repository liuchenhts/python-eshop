docker-compose up -d
# then docker-compose exec python bash, to get the shell

# alternative
# export ESHOP_ENV=dev
# docker-compose run --rm --service-ports python bash
# or docker-compose run --rm --service-ports -e ESHOP_ENV=dev python bash
