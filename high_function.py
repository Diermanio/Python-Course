from functools import reduce

def run():

    num_list = [ i for i in range(1, 6)]

    squares = list(map(lambda i: i**2, num_list))

    print("Uso de map: {}".format(squares))

    two_list = [ 2, 2, 2, 2, 2]

    pow_list = reduce(lambda a, b: a*b, two_list)

    print(pow_list)

if __name__ == "__main__":
    run()