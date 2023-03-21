DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'Jiwon', #2
        'USER': 'root', #3
        'PASSWORD': 'Foutune719$',  #4
        'HOST': 'localhost',   #5
        'PORT': '3306', #6python manage.py migrate
    }
}
SECRET_KEY = 'django-insecure-^t3=f81wds@ypehojbk$zh0a_h+a87k3zi^n^mbgp&=m@ld2y+'