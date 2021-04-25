# Due Gatti: Café & Gelato
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/lucasjaroszewski/Due-Gatti/blob/master/LICENSE) 

## About the project
https://duegatti.pythonanywhere.com/

Due Gatti is a full stack application for web and mobile. It was built to a well-known neighbourhood store. With the beginning of the pandemic, there was a need for innovation as the store had to keep their doors closed. The website was built with Django Framework (Python) as back-end and VueJS (Javascript) as front-end, relying on Stripe for online payments.


## Mobile layout
<p align="center">
  <img src="/assets/mobile-4.png" width="300">
  <img src="/assets/mobile-7.png" width="300">
  <img src="/assets/mobile-6.png" width="300">
</p>

## Web layout
<p align="center">
  <img src="/assets/web-3.png" width="450">
  <img src="/assets/web-4.png" width="450">
</p>

## Technologies
### Back-end
- Django Framework (Python)

### Front-end
- HTML
- Bulma (CSS)
- VueJS (Javascript)

## Deployment
- Back-end: PythonAnyWhere
- Database: SQLite3

## How to execute (Windows)

```bash
# Clone repository
git clone https://github.com/lucasjaroszewski/Due-Gatti

# Go inside Due-Gatti folder
cd Due-Gatti

# Create and activate virtual enviroment
virtualenv myenv
source myenv/Scripts/activate

# Install requirements
pip install -r requirements.txt

# Create .env file and type the secret_key for settings.py
SECRET_KEY = '...secret_key here...'

# Migrate files
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
```

## Author

Lucas Jaroszewski Nunes

https://www.linkedin.com/in/lucasjaroszewski

