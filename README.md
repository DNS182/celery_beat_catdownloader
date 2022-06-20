# DJANGO > CELERY USE ON CAT API TO DOWNLOAD RANDOM CAT IMAGES from **http://thecatapi.com**

# Local Development Setup
 --> Clone this repo git clone git@github.com:DNS182/celery_beat_catdownloader.git
 
 
 # Config
1> Install dependencies for your local environment by running pip install -r requirements.txt
2> Run python manage.py migrate
3> SETUP BROKER_URL FROM SETTINGS 
4> Run python manage.py runserver
 
# Trigger Celery Beat For BackGround Task
 --> Open new cmd in root and use this command celery -A demos.celery beat -l INFO to fire up celery beat
 --> Open new cmd in root and use this command celery -A demos.celery worker --pool=solo -l info to fire up a celery worker(Can be used Only to Download Image when HomePage is Refreshed)

# SOME GLIMPSE OF PAGE : 

![ezgif com-gif-maker](https://user-images.githubusercontent.com/103807395/174466744-b6e16eb5-ed7a-4927-ab3e-0c36d0b45fe0.gif)

# FETCHED CATS IMAGES : 

![cats](https://user-images.githubusercontent.com/103807395/174466762-93d1a931-6b4e-489b-b148-3e3fda44efc7.png)

# ENJOY HAPPY_CODING
