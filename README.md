# monero.city

Monero.city is a online directory in which you can see the merchants that accepts Monero on a map, rate them and contribute to global adoption.

## Install

Create a virtualenv
```
virtualenv -p python3 env
```

Activate and install requirements:
```
source env/bin/activate
pip install -r requirements.txt
```

Create a .env file:
```
SECRET_KEY=YOUR_SECRET_KEY_HERE
MYSQL_DB=DATABASE_NAME_HERE
MYSQL_USER=DATABASE_USER_HERE
MYSQL_PASSWORD=DATABASE_PASS_HERE
MYSQL_HOST=DATABASE_IP_HERE
```

Run migrations:
```
python manage.py migrate
```

Start
```
python manage.py runserver 8000
```

And go yo ```http://localhost:8000```
