
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

# main routine

# heading
statement_generator("Bit Calculator for Integers, Texts, and Images", "=")
# loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":


    data_type = user_choice()
    print("You chose", data_type)

