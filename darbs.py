

                #1. uzdevums

# Izmantojot teksta failā esošo informāciju nosākiet:

#Kurā gadā bija dibināts vecākais Omānas reģiona uzņēmums (informācija ir pieejama kolonnā Founded)?

#Atbildes vietā ierakstiet tikai veselo skaitli.


# import csv

# def oldest_company(filename):
    #with open(filename, 'r') as file:
        #reader = csv.reader(file)
        #next(reader)  
        #oldest_year = float('inf')
        #for row in reader:
            #if row[4] == 'Oman' and int(row[6]) < oldest_year:
                #oldest_year = int(row[6])
    #return oldest_year

#print(oldest_company('data.txt'))

                #2. uzdevums


# Izmantojot teksta failā esošo informāciju nosākiet:

# Kāds ir darbinieku skaits, kas strādā Latvijā?

# Atbildes vietā ierakstiet tikai veselo skaitli.


#import csv

#def employees_in_latvia(filename):
    #total_employees = 0
    #with open(filename, 'r') as file:
        #reader = csv.reader(file)
        #next(reader)  
        #for row in reader:
            #if row[4] == 'Latvia':
                #total_employees += int(row[8])
    #return total_employees

#print(employees_in_latvia('data.txt'))

                #3. uzdevums


#Izmantojot teksta failā esošo informāciju nosākiet, 

#Kāds ir darbinieku skaits kas strādā telekomunikācijas jomā Latvijā.  (Industry = Telecommunications, Country = Latvia) ?

#Atbildes vietā ierakstiet tikai veselo skaitli.


#import csv

# def telecom_employees_in_latvia(filename):
    #total_employees = 0
    #with open(filename, 'r') as file:
        #reader = csv.reader(file)
        #next(reader)
        #for row in reader:
            #if row[4] == 'Latvia' and row[7] == 'Telecommunications':
                #total_employees += int(row[8])
    #return total_employees

#print(telecom_employees_in_latvia('data.txt'))



                        #4. uzdevums

#Izmantojot teksta failā esošo informāciju nosākiet:

#Cik no datu bāze esošajiem Latvijas kompānijām ir SSL sertifikāts? (SSL sertifikāts ir kompānijām, kuram tīmekļa adrese sākas ar https://)

#Atbildes vietā ierakstiet tikai veselo skaitli.

#import csv

#def employees_in_latvia(data):
    #total_employees = 0
    #with open(data, 'r') as file:
        #reader = csv.reader(file)
        #next(reader)  # Skip the header
        #for row in reader:
            #if 'https://' in row[3] and row[4] == 'Latvia':
                #total_employees += 1
    #return total_employees

#print(employees_in_latvia('data.txt'))


                    #5. uzdevums




#Izmantojot teksta failā esošo informāciju nosākiet:


#Cik reizes datu bāzē tiek minēts domēna vārds .org reģionam Latvia?

#Atbildes vietā ierakstiet tikai veselo skaitli.

#import csv
#def employees_in_latvia(data):
    #total_employees = 0
    #with open(data, 'r') as file:
        #reader = csv.reader(file)
        #next(reader)  
        #for row in reader:
            #if '.org' in row[3] and row[4] == 'Latvia':
                #total_employees += 1
    #return total_employees

#print(employees_in_latvia('data.txt'))