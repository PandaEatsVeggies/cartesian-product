import cartesian_product_generator as cpg

if __name__ == '__main__':
    set1 = (1, 2, 3)
    set2 = ('a', 'b', 'c')
    set3 = (1.1, 2.2, 3.3)

    # check no arguments
    for i in cpg.cartesian_product_generator():
        print(i)

    # check cartesian product of two sets
    for i in cpg.cartesian_product_generator(set1, set2):
        print(i)

    # check cartesian product of three sets
    for i in cpg.cartesian_product_generator(set1, set2, set3):
        print(i)

    # check cartesian product of two sets but both of sets repeated twice
    for i in cpg.cartesian_product_generator(set1, set1, set2, set2):
        print(i)
