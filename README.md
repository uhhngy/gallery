
### 1. Installing
```bash
virtualenv venv
source venv/bin/activate  # win: venv\Scripts\activate
pip install -r requirements.txt 
```
### 2. Running
```bash
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```
### 3. Accessing
```bash
http://127.0.0.1/
```
