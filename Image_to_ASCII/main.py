import PIL.Image

ASCII = ["@","#","&","%","$","*","/",";",":",",","."]

#Resizing the image to be o
def resize(image, new_width=130):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width*ratio-60*ratio)
    
    return image.resize((new_width,new_height))  

def greyscale(image):

    return image.convert("L")

def pixel_ascii(image):

    pixels = image.getdata()

    characters  = "".join([ASCII[pixel//25] for pixel in pixels])

    return characters

def main(new_width = 130):

    path = input("Enter path of the image (relative or absolute): \n")
    try:
        image = PIL.Image.open(path)
    except:
        print("Invalid Path")
        return

    image_data = pixel_ascii(greyscale(resize(image)))

    pixel_count = len(image_data)

    ascii_image = "\n".join(image_data[i:(i+new_width)] for i in range(0,pixel_count,new_width))

    print(ascii_image)

    with  open("output.txt",'w') as _:
        _.write(ascii_image)

main()