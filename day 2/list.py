# declare a list
#my_list =[123,233,-83,4,]
#print(my_list)
#my_list.append(9999)
#my_list.insert(0,5)
#print(len(my_list))
#my_list.pop()
#my_list.pop(2)
#my_list_2=[5,6,7,8]
#new_1st=my_list+my_list_2
#new_1st=my_list_2.copy()
#print(*new_1st)
#print(*my_list)
#print(*my_list,end="@")
#cnt=my_list.count(4)
#print(cnt)
#my_list.sort()
#print(*my_list)
#map(more then on input)
#split(separated the space)
#dynamicinput
my_list=list(map(int,input().split(",")))
user_enter=my_list[0]
if(user_enter==1):
    my_list.append(0)
   print(my_list)
elif(user_enter==2):
    my_list.pop()
    print(my_list)
elif(user_enter==3):
    my_list.sort()
    print(my_list)
elif (user_enter==4):
    print(len(my_list))