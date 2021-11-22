
# puts series of symbols at start and end of text
def statement_generator(text, decoration):

    ends = decoration * 3

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# checks user choice is 'integer', 'text', or 'image'
def user_choice():

    valid = False
    while not valid:
        
        integer_ok = {"integer", "int", "number"}
        text_ok = ["text", "t", "txt"]
        image_ok = ["image", "img", "picture", "pic", "p"]

        response = input("file type (integer / text / image): ").lower()

        if response in integer_ok:
            return "integer"

        elif response in text_ok:
            return "text"

        elif response in image_ok:
            return "image"
        
        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image: ")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            print("Please choose a valid file type")
            print()

# checks input is more than a given value
def num_check(question, low):

    valid = False
    while not valid:

        error = "please enter a integer that is more than (or equal to) {}".format(low)

        try:

            response = int(input(question))

            if response >= low:
                return response 

            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

# calculate the # of bits for text (# of characters x 8)
def text_bits():
    
    print()
    # asks user for a string...
    var_text = input("enter some text: ")

    # calculate # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working
    print()
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    print("# of bits is {} x 8...".format(var_length))
    print("we need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""

# finds # of bits for 24 bit colour
def image_bits():

    # get width and height...
    image_width = num_check("Image width? ", 1)
    image_height = num_check("Image height? ", 1)

    # calculate # of pixels
    num_pixels = image_width * image_height

    # calculate # bits (24 x num pixels)
    num_bits = num_pixels * 24

    # output answer with working
    print()
    print("# of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
    print("# bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""

# converts decimal to binary and states how many bits are needed to represent the original integer
def int_bits():

    # get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    # source for code below is
    # https://stackoverflow.com/questions/699866/python-int-to-binary-string

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_binary)

        # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""

# main routine

# heading
statement_generator("Bit Calculator for Integers, Texts, and Images", "=")
# loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # asks user for file type
    data_type = user_choice()
    print("You chose", data_type)

    # for integers, ask for integer
    if data_type == "integer":
        int_bits()

    # for images, ask for width and height
    # must be more than / equal to 1
    elif data_type == "image":
        image_bits()
    
    # for text, ask for a string
    else:
        text_bits()
    
    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()
