def scalar_product(vec1, vec2):
    if len(vec1) == len(vec2):
        product = 0
        for element in list(zip(vec1, vec2)):
            product += element[0] * element[1]
        return product
    else:
        print("Length of two vectors aren't the same")


if __name__ == "__main__":
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    result = scalar_product(a, b)
    print(result)

    c = [1, 2, 12, 4, 3]
    d = [2, 4, 2, 8]
    result2 = scalar_product(c, d)
    print(result2)