#take input from user
rows=int(input("please enter the total number of rows:"))
number=1 #initialise by 1


print("floyd's triangle")
#outer loop for numbers of rows 
for i in range(1, rows+1):
    #inner loop for number of column
    for j in range (1,i+1):
        #display result
        print(number,end= ' ')
        number+=1
    print()

#take input from user
rows=int(input("please enter the total number of rows:"))
number=1 #initialise by 1


print("floyd's triangle")
#outer loop for numbers of *