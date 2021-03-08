# Open Diplomas
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple **Backend** and **Back-office** application to manage the creation and granting of diplomas and badges through Django framework

## Development and Contributing

Below you can see how to contribute to the project through Docker and Visual Studio Code, always in development environment.

### With Visual Studio Code - Insiders
1.  Install Docker and Docker Compose
2.  Install Visual Studio Code
3.  Install the following extensions
    - Docker
    - Remote – Containers
    - Python
4.  Open the project in Visual Studio Code
5.  Run the project
```python
python manage.py runserver 0.0.0.0:8000 --settings=opendiplomasproject.settings.development
```
6.  In a new Terminal, do the migrations
```python
python manage.py makemigrations core --settings=opendiplomasproject.settings.development
python manage.py migrate --settings=opendiplomasproject.settings.development
```
7.  Create an admin user
```python
python manage.py createsuperuser
```
8.  Run the command
```python
python manage.py collectstatic --settings=opendiplomasproject.settings.development
```
---
**Open Diplomas**  is an open source project, so contributing is as easy as forking the project on either of these sites and committing your enhancements. Please, don't forget include always tests. If you are fixing a bug, add a test that breaks before your patch and works after.