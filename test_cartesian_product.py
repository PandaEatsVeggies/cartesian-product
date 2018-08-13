import cartesian_product

if __name__ == '__main__':
    set1 = [1, 2, 3]
    set2 = ['a', 'b', 'c']
    set3 = [1.1, 2.2, 3.3]
    c = cartesian_product.CartesianProduct(set1, set2, set3)
    for i in c:
        print(i)
