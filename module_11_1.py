import requests
from PIL import Image, ImageFilter


def test_requests(url):

    response = requests.get(url)
    response.raise_for_status()
    print("Заголовки ответа:", response.headers)
    print("Содержимое ответа (первые 500 символов):")
    print(response.text[:500])


url = 'https://google.com'
test_requests(url)


def test_pillow(input, output):

    img = Image.open(input)
    resized_img = img.resize((200, 200))
    print("Размер изменен")
    rgb_img = resized_img.convert("RGB")
    blurred_img = rgb_img.filter(ImageFilter.BLUR)
    print("Эффект применен")
    blurred_img.save(output, format="JPEG")
    print(f"Изображение сохранено как {output}.")


input = "test.png"
output = "edited.jpg"
test_pillow(input, output)
