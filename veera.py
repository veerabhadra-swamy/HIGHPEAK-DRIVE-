file=open("input.txt","r") 
line=[]
for row in file:
    line.append(row.rstrip('\n'))  
line.pop(1)  #Removing the unwanted Lines
line.pop(1)
line.pop(1)
x=[]
y=[]

#Creating the list containing Goodies value
for i in range(0,len(line)):
    x.append(line[i].split(":"))
    y.append(int(x[i][1]))
num=y.pop(0)
x.pop(0)
unsorted_list=y[:]

sorted_list = []

# Sorting the goodies value list

while unsorted_list:
    minimum = unsorted_list[0]
    for item in unsorted_list:
        if item < minimum:
            minimum = item
    sorted_list.append(minimum)
    unsorted_list.remove(minimum)
diff=sorted_list[-1]
poi=0

#Finding the lowest difference

for i in range(0,len(sorted_list)-num):
    if sorted_list[i+(num-1)]-sorted_list[i]<diff:
        diff=sorted_list[i+(num-1)]-sorted_list[i]
        poi=i
#Creating the dictionary
      
di={}  
for i in range(0,len(x)):
    di[str(y[i])]=x[i][0]

#Writing the output into file
    
new=open("outout.txt","w")
for i in range(0,num):
    r=di[str(sorted_list[poi+i])]+" : "+str(sorted_list[poi+i])+"\n"
    new.write(r)
file.close()
new.close()
