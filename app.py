# Farhan's solution of fizz_buzz algorithm
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizz buzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"
    else:
        return input


print(fizz_buzz(5))
