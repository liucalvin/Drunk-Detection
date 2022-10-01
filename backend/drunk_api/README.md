# Drunk API

1. Open a terminal in the backend folder

```
cd backend/
```

2. Create and activate a virtual environment

```sh
python3 -m venv env
# Mac:
source env/bin/activate
# Windows (bash):
source env/scripts/activate
```

2. Move into the project folder and install dependencies

```sh
cd drunk_api/
pip install -r requirements.txt
```

3. Add an .env file in the `backend/drunk_api/drunk_api` folder with the following fields:

- SECRET_KEY

4. To run the server:

```sh
python manage.py runserver
```
