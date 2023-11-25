import requests
from PIL import Image
from io import BytesIO
def get_cat_image(tag=None):
    base_url = "https://cataas.com/cat"
    if tag:
        url = f'{base_url}/{tag}'
    else:
        url = base_url
    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image.show()
    else:
        print(f'Ошибка {response.status_code}')
get_cat_image()