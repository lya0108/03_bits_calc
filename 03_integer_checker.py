def num_check(question, low):

    valid = False
    while not valid:

        error = "please enter a number that is more than zero""(or equal to) {}".format(low)

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

keep_going = ""
while keep_going == "":
    print()
    # asks user for integer, width, and height
    var_integer = num_check("enter an integer: ", 0)
    print()
    # asks user for width and height of an image
    width = num_check("image width? ", 1)
    print()
    height = num_check("image height?", 1)