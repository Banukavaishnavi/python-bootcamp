# a mother give her child 700 rs to bring some fruits from market,the boy went to market he took 10 apples,8 oranges,2 dozen bananas.one apple=15rs,one orange=5rs and 1 banana =4rs.and the boy gave 700 rs to shopkeeper if the shopkeeper ask more than that requried money then he is a cheater if not he is good person.
apple=10
banana=24
orange=8
cost_apples=apple*15
cost_banana=banana*4
cost_orange=orange*5
total=cost_apples+cost_banana+cost_orange
print(f"the apples cost{cost_apples},the banana cost{cost_banana},the orange cost{cost_orange}")
print(total)
if(total>700):
    print("the shopkeeper is a cheater")
else:
    print("he is not")
  