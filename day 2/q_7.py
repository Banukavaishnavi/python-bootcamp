#find the avg of elements in the even index 
list=list(map(int,input().split(" ")))
sum=0
count=0
for i in range(len(list)):
    if(list[i]%2==0):
        count+=1
        print(sum/count)
        