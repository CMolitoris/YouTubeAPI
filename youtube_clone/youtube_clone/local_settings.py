# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dp31un1f7z65ohix*_m#)*57wcluag8q12apvpvzvoi=#4jh91'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_database',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}