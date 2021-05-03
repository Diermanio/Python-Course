class LesserError(Exception):
    """When the value passed is less than 0 """
    pass

def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num%i==0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un numero: "))
        if num < 1: raise LesserError
        print(divisors(num))
        print("Fini")
    except ValueError:
        print("Strings are not valid")
    except LesserError:
        print("Only value greater than 0")

if __name__ == "__main__":
    run()