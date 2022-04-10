import PIL.Image

# ascii characters used to build the output text in desending order of intensity , matches up each pixel with a char with same intesity
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", "," "."]

# resize image according to a new width


# takes the image and a new desired width as the arguments
def resize_image(image, new_width=100):
    width, height = image.size  # get width and height of image and save it into image.size
    ratio = height / width  # get ratio by dividing
    # get new height by multiplying ratio by new width
    new_height = int(new_width * ratio)
    # create a new resized image using the images new resized values
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale


def grayify(image):  # takes a PIL image
    grayscale_image = image.convert("L")  # L converts it to grayscale
    return(grayscale_image)

# convert pixels to a string of ASCII characters


def pixels_to_ascii(image):  # new function to convert
    pixels = image.getdata()  # this returns a list of each pixels grayscale value
    # go through each pixel and iterate a corresponding ascii char and combine this list into a single string using join
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


def main(new_width=100):
    # attempt to open image from user-input
    # this allows people to say what their image is called
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        # if the pathname is not vaild this will catch that
        print(path, "is not a valid pathanme to an image.")

    # convert image to ASCII
    # this is a long list of ascii char, one for each pixel in the image
    # but they are not sized to our desired size
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # format
    pixel_count = len(new_image_data)  # get the full length of the list
    # length of each string is now desired width of new image and combine these strings into a single string
    ascii_image = "\n".join(
        new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # print result
    print(ascii_image)

    # save the result to "ascii_image.txt"
    # open a new file called ascii image text in writing mode as f
    with open("ascii_image.txt", "w") as f:
        # call f.write to save the ascii image in the file
        f.write(ascii_image)


main()
