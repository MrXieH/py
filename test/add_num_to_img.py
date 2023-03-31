import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# 往图片右下角添加一个字符
def add_num_to_img():
    reponse = requests.get('https://camo.githubusercontent.com/2e637daaedbb872ae5949028a692575d253f84c020b7634f9dc64b786cc0f3f8/687474703a2f2f692e696d6775722e636f6d2f736732646b75592e706e673f31')

    bytesData = BytesIO()
    bytesData.write(reponse.content)

    image = Image.open(bytesData)

    width,height = image.size

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('arial.ttf', 20)

    draw.text((width - 10, height - 20), "hi", fill = (255, 255, 255), font = font)

    image.show()

if __name__ == '__main__':
    add_num_to_img()