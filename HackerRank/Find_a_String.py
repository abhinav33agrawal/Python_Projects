def count_substring(string, sub_string):
    count,sums = 0,0
    for i in range(0,len(string)):
        if match(string[count:len(sub_string)+count],sub_string):
            sums += 1
        count += 1
    return sums

def match(s1,s2):
    return s1 == s2
        


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
