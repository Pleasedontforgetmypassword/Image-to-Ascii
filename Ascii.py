from PIL import Image

Gray10 = "@%#+=-:. "
Gray70 = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """

def char(number, value):
    if number == 70:
        return Gray70[int(round(value//3.696))]
    else:
        return Gray10[int(round(value//28.34))]

def conversion(img):
    return Image.open(img).convert("L")

def valid(image):
    try:
        Image.open(image)
        return True
    except:
        return False

def write(number, image, file):
    width = image.size[0]
    height = image.size[1]

    with open(file, "w") as key:
        for i in range(height):
            for j in range(width):
                gray = image.getpixel((j, i))
                key.write(char(number, gray))
            key.write("\n")
        key.close()

