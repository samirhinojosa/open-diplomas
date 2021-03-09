# Open Diplomas
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple **Backend** and **Back-office** application to manage the creation and granting of diplomas and badges through Django framework

## Development and Contributing

Below you can see how to contribute to the project through Docker and Visual Studio Code, always in development environment.

1.  Install Docker and Docker Compose
2.  In the project directory root, run the following command in shell
```docker
docker-compose up
```
3. In another shell run the command below
```docker
docker-compose exec web bash 
```
4.  If it is the first time, then 
    -   In the project directory root, create a file called **".env"** with Django Secret Key
    -   Create the database and database user based on opendiplomasproject.settings.development
	-	Prepare the migrations based on the apps

        ```python
        python manage.py makemigrations --settings=opendiplomasproject.settings.development
        ```
    -  Make the migrations
        ```python
        python manage.py migrate --settings=opendiplomasproject.settings.development
        ```
    -   Create an admin user
        ```python
        python manage.py createsuperuser --settings=opendiplomasproject.settings.development
        ```
    -  Run the command
        ```python
        python manage.py collectstatic --settings=opendiplomasproject.settings.development
        ```

### With Visual Studio Code - Insiders
1.  Install Docker and Docker Compose
2.  Install Visual Studio Code
3.  Install the following extensions
    - Docker
    - Remote – Containers
    - Python
4.  Open the project in Visual Studio Code
5.  If it is the first time, then
    -   In the project directory root, create a file called **".env"** with Django Secret Key
    -   Create the database and database user based on opendiplomasproject.settings.development
    -   In a Terminal, prepare the migrations based on the apps
        ```python
        python manage.py makemigrations --settings=opendiplomasproject.settings.development
        ```
    -   Make the migrations
        ```python
        python manage.py migrate --settings=opendiplomasproject.settings.development
        ```
    -   Create an admin user
        ```python
        python manage.py createsuperuser --settings=opendiplomasproject.settings.development
        ```
    -   Run the command
        ```python
        python manage.py collectstatic --settings=opendiplomasproject.settings.development
        ```
---
**Open Diplomas**  is an open source project, so contributing is as easy as forking the project on either of these sites and committing your enhancements. Please, don't forget include always tests. If you are fixing a bug, add a test that breaks before your patch and works after.