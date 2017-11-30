# python-eshop, 
1. docker-compose run --rm --service-ports python bash
2. the above command will start a container for this one-off python-django development env in a bash shell, the django image is built from the Dockerfile
3. django-admin.py startproject eshop . , run this command in the bash to create a django project skeleton
4. environment variables is defined in .env file or the local env
5. docker-compose up -d, to start the server
