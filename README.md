# Open Diplomas
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple **Backend** and **Back-office** application to manage the creation and granting of diplomas and badges through Django framework

## **Development and Contributing**

Below you can see how to contribute to the project through Docker and Visual Studio Code, always in development environment.

1.  Install Docker and Docker Compose
2. With a **Terminal** 
    - In the project directory root, run the following command in shell
        ```docker
        docker-compose up
        ```
    - In another shell run the command below
        ```docker
        docker-compose exec web bash 
        ```
3. With **Visual Studio Code**
    - Install Visual Studio Code
    - Install the following extensions
        - Docker
        - Remote – Containers
        - Python
    - Open the project in Visual Studio Code
4.  To execute the development server then run the following command
    ```python
    python manage.py runserver 0.0.0.0:8000 --settings=opendiplomasproject.settings.development
    ```
5.  If it is the first time. Consider enabling another terminal to run some following commands. 
    -   In the project directory root, create a file called **".env"** with Django Secret Key, like the following example
        ```python
        SECRET_KEY=HERE_THE_DJANGO_SECRET_KEY
        ```
    -   Create the database and database user based on **opendiplomasproject.settings.development**
        ```python
        'NAME': 'od_db',
        'USER': 'project',
        'PASSWORD': 'project',
        ```
	-	Prepare the migrations based on the apps
        ```python
        python manage.py makemigrations core --settings=opendiplomasproject.settings.development
        ```
    -  Make the migrations
        ```python
        python manage.py migrate core --settings=opendiplomasproject.settings.development
        python manage.py migrate auth --settings=opendiplomasproject.settings.development
        python manage.py migrate contenttypes --settings=opendiplomasproject.settings.development
        python manage.py migrate admin --settings=opendiplomasproject.settings.development
        python manage.py migrate sessions --settings=opendiplomasproject.settings.development
        ```
    -   Create an admin user
        ```python
        python manage.py createsuperuser --settings=opendiplomasproject.settings.development
        ```
    -  Run the command
        ```python
        python manage.py collectstatic --settings=opendiplomasproject.settings.development
        ```

---
**Open Diplomas**  is an open source project, so contributing is as easy as forking the project on either of these sites and committing your enhancements. Please, don't forget include always tests. If you are fixing a bug, add a test that breaks before your patch and works after.