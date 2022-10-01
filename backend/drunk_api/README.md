# Drunk API

1. Create a virtual environment

```sh
python3 -m venv env
# Mac:
source env/bin/activate
# Windows (bash):
source env/scripts/activate
```

2. Install dependencies

```sh
pip install django
pip install djangorestframework
```

3. Add .env file in the `backend/drunk_api/drunk_api` folder with the following fields:

- SECRET_KEY

4. To run the server:

```sh
python manage.py runserver
```
