if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i,j,k] for i in range(1+x) for j in range(1+y) for k in range(1+z) if (i+j+k) != n])

