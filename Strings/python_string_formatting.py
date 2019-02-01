def print_formatted(number):
    # your code goes here
    binary = '{0:b}'.format(number)
    length = len(binary)
    for i in range(1,number+1):
        temp = '{0:>' + str(length) + 'd} {1:>' + str(length) + 'o} {2:>' + str(length) + 'X} {3:>' + str(length) +'b}'
        print(temp.format(i,i,i,i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)