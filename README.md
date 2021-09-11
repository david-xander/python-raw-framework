# A simple python RAW server tested under nginx/gunicorn
The framework will be behind an nginx and will use gunicorn as it's WSGI. 

The Docker composition is provided for the testing.

## Using gunicorn like this in DEV
To be able to modify the python code and reflect the change when it happens.

gunicorn --workers=2 app:app --reload

## In order to build the image
docker-compose build

## To run the image
docker-compose up -d

## To run and build the image
docker-compose up -d --build

## To stop the image
docker-compose down -v

## To check if something goes wrong
docker-compose logs -f

# TESTING
export PYTHONPATH="${PYTHONPATH}:/Users/david/__PYTHON/my_python_frameworks/a_raw_python_framework/rawframework/app/"
