if __name__ == '__main__':
    s = input().strip()
    alnumFlag = False
    alphaFlag = False
    digitFlag = False
    lowerFlag = False
    upperFlag = False

    for i in range(len(s)):
        if(s[i].isalnum()):
            alnumFlag = True
        if(s[i].isalpha()):
            alphaFlag = True
        if(s[i].isdigit()):
            digitFlag = True
        if(s[i].islower()):
            lowerFlag = True
        if(s[i].isupper()):
            upperFlag = True                

    print(alnumFlag)
    print(alphaFlag)
    print(digitFlag)
    print(lowerFlag)
    print(upperFlag)

