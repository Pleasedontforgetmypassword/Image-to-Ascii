from PIL import Image

#grayscale for 10 characters
Gray10 = "@%#+=-:. "

#grayscale for 70 characters
Gray70 = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """

#returns the characters by using the value
#number is to specify 10 or 70 characters, Value is the brightness of the pixel
def char(number, value):
    if number == 70:
        return Gray70[int(round(value//3.696))]
    else:
        return Gray10[int(round(value//28.34))]

#converts the image to monochrome
def conversion(img):
    return Image.open(img).convert("L")

#checks if the image can be opened
def valid(image):
    try:
        Image.open(image)
        return True
    except:
        return False

#writes the image into ascii
def write(number, image, file):
    
    #define width and height
    width = image.size[0]
    height = image.size[1]
    
    #opens the file in write mode
    with open(file, "w") as key:
        
        #loops over the height of the image
        for i in range(height):
            
            #loops over the width of the image
            for j in range(width):
                
                #returns the brightness at the j'th, i'th pixel
                gray = image.getpixel((j, i))
                
                #writes the ascii character into Image.txt
                key.write(char(number, gray)*2)
                
            #Newline
            key.write("\n")
        
        #closes the file
        key.close()

