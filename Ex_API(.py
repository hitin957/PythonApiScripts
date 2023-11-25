import requests
from PIL import Image
from io import BytesIO
def get_cat_image(tag=None):
    base_url = "https://cataas.com/cat"
    #1234567890
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
        #abs
        print(f'Ошибка {response.status_code}')
#get_cat_image()
get_cat_image()