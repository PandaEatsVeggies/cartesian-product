import cartesian_product

if __name__ == '__main__':
    set1 = (1, 2, 3)
    set2 = ('a', 'b', 'c')
    set3 = (1.1, 2.2, 3.3)

    # check no arguments
    c1 = cartesian_product.CartesianProduct()
    for i in c1:
        print(i)

    # check cartesian product of two sets
    c2 = cartesian_product.CartesianProduct(set1, set2)
    for i in c2:
        print(i)

    # check cartesian product of three sets
    c3 = cartesian_product.CartesianProduct(set1, set2, set3)
    for i in c3:
        print(i)

    # check cartesian product of two sets but both of sets repeated twice
    c4 = cartesian_product.CartesianProduct(set1, set1, set2, set2)
    for i in c4:
        print(i)