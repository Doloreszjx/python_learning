#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else

    # conditional statements let you use "a if C else b"

    # match-case makes it easy to compare multiple values
    value = "four"
    match value:
        case "one":
            print('you enter one')
        case "two" | "three":
            print('you enter other number')
        case _:
            print('you enter wrong')


if __name__ == "__main__":
    main()
