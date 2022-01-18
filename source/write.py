from PIL import Image, ImageDraw
def generate(size, data, path, name):
    im = Image.new('RGB', (size*10, size*10), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    draw.rectangle((0, 0, 10, size*10,), fill=(0, 0, 0), outline=(0, 0, 0)) # left outline
    draw.rectangle((0, size*10, size*10, size*10-(10)), fill=(0, 0, 0), outline=(0, 0, 0)) # bottom outline

    for i in range(size):
        if (i % 2) == 0:
            draw.rectangle((i*10, 0, i*10+10, 10), fill=(0, 0, 0), outline=(0, 0, 0)) # top dashed outline
        else:
            draw.rectangle((size*10-10, i*10, size*10, i*10+10), fill=(0, 0, 0), outline=(0, 0, 0)) # right dashed outline

    if (size % 4) != 0: # No need to use flipped chunks on the right side
        coordinates = [0,0]
        print("Using data: " + str(data))
        for chunk in data:
            print("Using chunk: " + chunk)
            z = 0
            line = 0
            for bit in chunk:
                print("Using bit: " + bit)
                x = ((coordinates[0]*4)+1+z)*10
                y = ((coordinates[1]*2)+1+line)*10
                if bit == "1":
                    print("Set BLACK to " + str(coordinates[0]) + "," + str(coordinates[1]) + " bit: " + str(z) + " line: " + str(line))
                    draw.rectangle((x, y, x+10, y+10), fill=(0, 0, 0), outline=(0, 0, 0))
                else: 
                    print("Set WHITE to " + str(coordinates[0]) + "," + str(coordinates[1]) + " bit: " + str(z) + " line: " + str(line))
                    draw.rectangle((x, y, x+10, y+10), fill=(255, 255, 255), outline=(0, 0, 0))

                if z == 3:
                    z = 0
                    line = 1
                else:
                    z = z + 1  
            
            coordinates[0] = coordinates[0] + 1
            if coordinates[0] == ((size-2)/4):
                coordinates[0] = 0
                coordinates[1] = coordinates[1] + 1
        draw.rectangle(((size-3)*10, (size-3)*10, (size-3)*10+10, (size-3)*10+10), fill=(0, 0, 0), outline=(0, 0, 0))
        draw.rectangle(((size-2)*10, (size-2)*10, (size-2)*10+10, (size-2)*10+10), fill=(0, 0, 0), outline=(0, 0, 0))

    else:
        draw.rectangle(((size-2)*10, (size-3)*10, (size-2)*10+10, (size-3)*10+10), fill=(0, 0, 0), outline=(0, 0, 0))
        draw.rectangle(((size-3)*10, (size-2)*10, (size-3)*10+10, (size-2)*10+10), fill=(0, 0, 0), outline=(0, 0, 0))

    fileName = path + "DataMatrix-" + name + ".jpg"
    im.save(fileName, quality=100)