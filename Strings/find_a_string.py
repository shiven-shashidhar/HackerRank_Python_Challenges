def count_substring(string, sub_string):
    temp = string
    idx = -1
    count = 0
    while len(temp) > 0:
        idx = temp.find(sub_string)
        if(idx == -1):
            return count       
        else:
            temp = temp[idx+1:]
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)