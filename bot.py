import datetime

def addNew_Deadline(List_2D):    # function to add new deadline
    print("\nAdd deadline:\n")    
    while True:                   # infinite while loop
        inputi = input()              # taking input from user
        if inputi == "STOP":          # if input = STOP
            break                         # break the infinite loop
        innerList = inputi.split()    # split the input string (i.e. create a innerList)
        List_2D.append(innerList)     # append the innerLists to the 2D list
    D1 = {}                   # an empty dictionary
    for e in List_2D:         # for each element in 2D list
        if e[2] in D1:        # creating the dictionary           (if key already in D1 then append)
            D1[e[2]].append(e[0].upper() + " || " + e[1].upper()) #(to the list (i.e. the value))
        else:                                                     # else (i.e. for new key)
            D1[e[2]] = [e[0].upper() + " || " + e[1].upper()]     # assign the value of the key
    return D1

def viewAll_Deadlines(D1):     # function to display deadlines
    if D1:                     # if dictionary is not empty
        dateS = []             # an empty list
        for k in D1:           # for each key in D1
            dateS.append(k)    # creating the list with the keys [i.e. dates (with string)]
        ADate = [datetime.datetime.strptime(d, "%d/%m/%Y") for d in dateS] # creating a list with actual dates
        ADate.sort()                                                       # sort the dates in the list
        sortedD = [datetime.datetime.strftime(d, "%d/%m/%Y") for d in ADate] # new list with sorted dates
        print("\nDeadlines:\n")                
        for dt in sortedD:                # for each date in sortedD list
            print(dt)                     # print the date
            if len(D1[dt]) > 1:           # if date has multiple task
                for i in D1[dt]:              # for each task in that date
                    print(i)                      # print task
            else:                         # else (i.e. date with single task)
                print(D1[dt][0])              # display the task
            print("==================")    
    else:                                # else (i.e. dictionary D1 is empty)
        print("There is no deadline.")   # print there is no deadline


# main program

List_2D = []                   # an empty list
dict1 = {}                     # an empty dictionary
print("1. Add new Deadline.")      # 1 to add new deadline  
print("2. View all deadlines.")    # 2 to view deadlines
print("3. Exit.")                  # 3 to exit
while True:                                       # while True (i.e. infinite loop)
    ch = int(input("Enter your choice (1-3): "))  # taking the choice from user
    if ch == 1:                                   # if ch = 1
        dict1 = addNew_Deadline(List_2D)          # calling the addNew_deadline function
    elif ch == 2:                                 # if ch = 2
        viewAll_Deadlines(dict1)                  # calling the viewAll_deadlines function
    elif ch == 3:                                 # if ch = 3
        print("Exiting...")                       # exiting
        break                                     # breaking the infinite loop
    else:                                         # else (i.e. for ch other than 1/2/3)
        print("Invalid choice!!")                 # print invalid choice