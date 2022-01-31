from importlib.resources import path
import PIL.Image as pil

def convertToGrayScale(image):
    return image.convert("L")

def resizeImage(image, new_width=200):
    width, height = image.size
    ratio = height//width
    new_height = int(new_width*ratio)
    return image.resize((new_width, new_height))

def convertPixelToAsciiChar(image):
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":",",", "."]
    pixels = image.getdata()
    # print("pixels len ", len(pixels))
    chars = ""
    for pixelValue in pixels:
        chars += ASCII_CHARS[pixelValue//25]
    return chars

if __name__ == "__main__":
    path = input("Give path to the image needed to convert\n")

    try:
        image = pil.open(path)
    except:
        print(path, "It is an invalid path")

    # resize image
    # new_width = input("give a new width\n")
    # if new_width == "no":
    #     new_width= image.size[0]
    resizedImage = resizeImage(image)

    # convert image to grayscale
    grayScaleImage = convertToGrayScale(resizedImage)

    # convert each pixel to corresponding ascii
    new_chars_for_image = convertPixelToAsciiChar(grayScaleImage)

    #format and split one big list as per width
    count_chars = len(new_chars_for_image)
    # print(count_chars)
    ascii_image = ""
    for i in range(0, count_chars, resizedImage.size[0]):
        ascii_image += new_chars_for_image[i:i+resizedImage.size[0]]+"\n"

    with open("ascii_art.txt","w") as file:
        file.write(ascii_image)