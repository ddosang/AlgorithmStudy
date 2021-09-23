
def DFS(x):
    print(x) #3 2 1
    if x > 0:
        DFS(x-1)
        print(x) #1 2 3



if __name__=="__main__":
    DFS(3)