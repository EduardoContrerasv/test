ga = 1
while ga == 1:
    try:
        patients = int(input("number of patients"))
        if patients > 0 :
            ga = 0
    except ValueError as error:
        print("no")
counter = 0
older = 0
younger = 0

try:
    while counter != patients:
        name = input("patient name")
        age = int(input("patient age"))
        if age < 0:
            print ("invalid input")
        elif age >= 0 and age <= 60:
            younger += 1
            counter += 1
        elif age > 60:
            older += 1
            counter += 1
except ValueError as error:
    print ("invalid input")
    
print (f"older than 60 {older}, younger than 60 {younger}")
