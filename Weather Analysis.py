temparature=[]
for i in range(7):
    temp=float(input("enter temparature:"))
    temparature.append(temp) 
avrg=sum(temparature)/len(temparature) 
maximum=max(temparature)
minimum=min(temparature)

print("average temparature in a week is:",avrg) 
print("maximum temparature in a week is:",maximum) 
print("minimum temparature in a week is:",minimum) 
