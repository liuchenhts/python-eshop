# python-eshop

1. This is the demo of eshop web application developed by using python, django and postgres.
2. This demo will try to demonstrate the best practices of python web application development.
3. Docker is used for development environment setup and production like environment deployment.


# How to develop and deploy
1. set up dependent postgres database
    1.1 create database eshop
    1.2 python manage.py migrate, which will create tables in the eshop db
2. set up dependent container environment variables, which are saved in the envfiles folder
3. run devenvrun.sh to start development
4. run build.sh to build docker image
    4.1 git push will trigger docker hub to build image automatically
5. run proenvrun.sh to deploy the service to production
