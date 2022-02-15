import discord 
import aiohttp
import io

from PIL import Image

async def get_image_data(url : str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            img_raw = await response.read()

    return io.BytesIO(img_raw)

def get_image_from_data(data : io.BytesIO):
    return Image.open(data)

def get_average_color(img : Image) -> discord.Color:

    img = img.convert("RGBA")
    pixels = list(img.getdata())

    avg = [0, 0, 0]
    counter = 0
    for pixel in pixels:
        if pixel[3] > 90:
            counter += 1
            for i in range(0, 3):
                avg[i] += pixel[i]

    for i in range(0, 3):
        avg[i] = round(avg[i] / counter)

    img = Image.new('RGB', (300, 200), (avg[0], avg[1], avg[2]))
    rgb_int = avg[0] << 16 | avg[1] << 8 | avg[2]
    return discord.Color(rgb_int)
    