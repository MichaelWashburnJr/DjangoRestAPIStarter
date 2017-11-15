from setuptools import find_packages, setup

setup(
    name='todo_api',
    version='0.1',
    description='A ToDo List API built with Django Rest Framework',
    author='Michael Washburn Jr',
    author_email='michael@michaelwashburnjr.com',
    url='https://github.com/mdw7326/DjangoRestApiExample',
    packages=find_packages(),
    install_requires=[
        'Django==1.11.7',
        'django-allauth==0.34.0',
        'django-rest-auth==0.9.2',
        'django-rest-swagger==2.1.2',
        'djangorestframework-jwt==1.11.0',
        'djangorestframework==3.7.3',
        'django-rest-swagger==2.1.2',
    ]
)