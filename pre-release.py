coc = 550
input("welcome to the 'book your trip' program\n[press ENTER to continue]")
print("-------------------------------------")
students = int(input(" how many students are going to the trip?\n>"))
if students > 45:
               print("sorry too many students, MAX. number is 45")
               input("[press ENTER to exit]")
elif students > 39:
    TicketC = (students*30) - 120
elif (students > 29)and (students <40) :
    TicketC = (students*30) - 90
elif (students > 19) and (students < 30):
    TicketC = (students*30) - 60
elif (students > 9) and (students < 20):
    TicketC = (students*30) - 30
else:
    TicketC = students * 30
print("The total TICKET cost of trip is $",(students*30))
totalcost = (students*30) + coc
print("The total  cost of trip is $",totalcost)
cperstudent = int(totalcost / students)
print("I would reccommend the cost per student to be $",(cperstudent))
print("--------------------------------------")
studentdsgoing = []
paidornot= []
studentspaid = 0
studentshaventpaid = 0
for i in range(students):
    studentdsgoing.append(input("Please input student name\n>"))
    paidornot.append(input("has the student paid\n[yes OR no]\n"))
    if paidornot[i] == "yes" or paidornot[i] =='y' :
        studentspaid = studentspaid + 1   
    else:
        studentshaventpaid = studentshaventpaid + 1
    print("=====================")        
print (studentdsgoing)
print ("students paid is:", studentspaid)
print ("students not paid is:", studentshaventpaid)
input(" -------------------------------------- \npress ENTER to have a list of who has paid\n---------------------------------------")
for i in range(students):
    print("Student:",studentdsgoing[i])
    print("paid?:", paidornot[i])
    print("====================")
input(" -------------------------------------- \npress ENTER to see profit/loss you could make\n---------------------------------------")
sales = studentspaid*cperstudent
profitorloss = sales - totalcost
print("sales made is $", sales)
if sales > totalcost:
    print ("you have made a profit of $", profitorloss)
elif sales == totalcost:
    print ("you have broken even $")
else:
    print ("you have made a loss of $", profitorloss)
input("thank you for using 'book your trip' program\n[press ENTER to exit]")
