import requests as r
import uuid
from celery import shared_task
from django.conf import settings

URL = "http://thecatapi.com/api/images/get?format=src&type=gif"


@shared_task
def download_a_cat():
    resp = r.get(URL)
    file_type = resp.headers.get('Content-Type').split('/')[1]
    #content-type means images/gif as it split / and gif is stored on file_type
    file_name = settings.BASE_DIR / 'static' / 'cats' / (str(uuid.uuid4())+ "." + file_type)
    #file_name = base_dir / cats folder / random uuid.file_type
    with open(file_name, 'wb') as f: #wb means writing on binary mode
        for chunk in resp.iter_content(chunk_size=128):
            f.write(chunk)
    return 'Done Downloaded Will Run On 1-Minute Again..'
