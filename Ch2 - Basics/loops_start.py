#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    # while x < 4:
    #     print(x)
    #     x += 1

    # TODO: define a for loop
    for x in range(10):
        if x % 2 == 0:
            print(x)
            continue
        if x < 5:
            break

    # TODO: use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # TODO: use the break and continue statements

    # TODO: using the enumerate() function to get index
    for index, item in enumerate(days):
        print(index, item)


if __name__ == "__main__":
    main()
