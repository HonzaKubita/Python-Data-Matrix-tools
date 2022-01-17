from PIL import Image, ImageDraw
def write(size, data, path):
    im = Image.new('RGB', (size*10, size*10), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.rectangle((0, 0, 10, size*10,), fill=(0, 0, 0), outline=(0, 0, 0)) # left outline
    draw.rectangle((0, size*10, size*10, size*10-(10)), fill=(0, 0, 0), outline=(0, 0, 0)) # bottom outline
    for i in range(size):
        if (i % 2) == 0:
            draw.rectangle((i*10, 0, i*10+10, 10), fill=(0, 0, 0), outline=(0, 0, 0)) # bottom outline
    for i in range(size):
        if (i % 2) != 0:
            draw.rectangle((size*10-10, i*10, size*10, i*10+10), fill=(0, 0, 0), outline=(0, 0, 0)) # bottom outline
    fileName = path + "DataMatrix-" + str(data) + ".jpg"
    im.save(fileName, quality=100)