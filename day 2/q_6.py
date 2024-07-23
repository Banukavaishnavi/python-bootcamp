# take a space separated input from a user and print alternate elements
my_list=list(map(int,input().split()))
for i in range(len(my_list)):
    if(i%2!=0):
        print(my_list[i])
    