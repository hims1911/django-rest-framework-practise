# django-rest-framework-practise

## Installing the virtualenv

```
virtualenv work_env
source virtualenv/bin/activate
```

## Installing the requirements.txt packages

```
pip install -r requirements.txt
```

## Migrate

```
python manage.py migrate
```

## Seed admin data that will print the admin username and password
```
 python manage.py shell < modelSeed.py
```

## Run Server
```
python manage.py runserver
```

## Test API
  Import `django_rest_framework.postman_collection.json` file in your POSTMAN to test the required API's.

## Run Unit Test Cases
  ```
  python manage.py test
  ```


