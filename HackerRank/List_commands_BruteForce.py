if __name__ == '__main__':
    N = int(input())
    mylist=[]
    x=1
    for _ in range(N):
        T= raw_input().split()
        if T[0]=="append" :
            mylist.append(int(T[1]))
        if T[0]=="insert" :
            mylist.insert(int(T[1]), int(T[2]))    
        if T[0]=="remove" :
            mylist.remove(int(T[1]))
        if T[0]=="sort" :
            mylist.sort() 
        if T[0]=="reverse" :
            mylist.reverse()
        if T[0]=="pop" :
            mylist.pop()
        if T[0]=="print" :
            print(mylist)
