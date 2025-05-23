### Create Virtual Environment
```shell
python3 -m venv .venv
source .venv/bin/activate

```
### Install Dependencies
```shell
pip install -r requirements.txt
```

### Apply migrations
```shell
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser
```shell
python manage.py createsuperuser
```

### Run server
```shell
python manage.py runserver
```