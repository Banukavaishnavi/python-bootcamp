#mr Z is selected in olympics is participated in 
#swimming compition only one is selected among them.
#x and y are the rnds of z.x participated in badminton,
#y is participated in table tennis .
# according to selection community the requrimnet for badminton h=140,w is factor of 2,bf=<12%.
# according to the selection community the tabletennis requriment is h=minimum 118 to 148,w=factor 
#of no.of medal won by mr z,bf=14%.
#according to the perivous history z 
#participated 14 games out it having success rate of 65%.write a program check x,y,z from india they travel'' in same plane or  not. 
x_height=int(input("height eligibilty for badminton"))
x_weight=int(input("weight eligibilty for badminton"))
x_bodyfat=int(input("bodyfat eligibilty for badminton"))
y_height=int(input("height eligibilty for tabletennis"))
zmedals=(50/100)*14
y_weight=int(input("weight eligibilty for tabletennis"))
y_bodyfat=int(input("bodyfat eligibilty for tabletennis"))
if((x_height>=140) and (x_weight%2==0) and (x_bodyfat<12)):
    if(y_height>=118 or y_height<=148) and (y_weight%zmedals==0) and (y_bodyfat==14)):
        print("x,y,z are travelling in same plane")
    else:
        print("only x,z are travelling in same plane") 
else:
    print("only z are travelling in same plane")




