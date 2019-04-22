import mysql.connector
import csv
mysql = mysql.connector.connect(host="localhost", user = "root", password = "Calculations99", database = "Spy")
cursor = mysql.cursor(buffered=True)

#Spy.AGENT
def insert_agent():
    insert_command = ("INSERT INTO Spy.AGENT (Agent_id, Name, Status, Salary, Emergency_contact_line) VALUES (%s, %s, %s, %s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.AGENT")
    except Exception as err:
        print('Reject deletion')
    print(insert_command)
    with open("agent_list_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            #data = i
            #data[0] = int(data[0])
            #data[3] = int(data[3])
            #data[4] = int(data[4])
            #data = tuple(data)
            #print("\n\n")
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.AGENT")
    #for x in cursor:
    #    print(x)

#insert Spy.FIREARM
def insert_firearm():
    insert_command = ("INSERT INTO Spy.FIREARM (Origin, Caliber, Type, Make, Serial_no, Cost, Agent_id) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.FIREARM")
    except Exception as err:
        print('Reject deletion')
    print(insert_command)
    with open("firearm_list_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            #data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(data)
            #print(type(data))
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print("Duplicate entry. Ignore the entry entered")
    cursor.execute("SELECT * FROM Spy.FIREARM")
    #for x in cursor:
    #    print(x)

#Spy TARGET
def insert_target():
    insert_command = ("INSERT INTO Spy.TARGET (Target_code_name, Legal_name, Affiliation) VALUES (%s, %s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.TARGET")
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("target_list_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.TARGET")
    #for x in cursor:
    #    print(x)

#Spy UNIT
def insert_unit():
    insert_command = ("INSERT INTO Spy.UNIT (Unit_id, Budget, Target_code_name) VALUES (%s, %s, %s)")
    cursor.execute("DELETE FROM Spy.UNIT")
    print(insert_command)
    with open("unit_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.UNIT")
    for x in cursor:
        print(x)

#Spy SPY
def insert_spy():
    insert_command = ("INSERT INTO Spy.SPY (Spy_code_name, Specialty, Target_code_name) VALUES (%s, %s, %s)")
    cursor.execute("DELETE FROM Spy.SPY")
    print(insert_command)
    with open("spy_list_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            print(tuple(i))
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.SPY")
    for x in cursor:
        print(x)

#Spy HOME_SPY
def insert_home_spy():
    insert_command = ("INSERT INTO Spy.HOME_SPY (Spy_code_name, Current_location, Unit_id, Agent_id) VALUES (%s, %s, %s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.HOME_SPY")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("home_spy_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.HOME_SPY")
    for x in cursor:
        print(x)

#Spy FOREIGN_SPY_ORGANIATION
def insert_foreign_spy_organization():
    insert_command = ("INSERT INTO Spy.FOREIGN_SPY_ORGANIZATION (Org_name, Origin, Relationship) VALUES (%s, %s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.FOREIGN_SPY_ORGANIZATION")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("foreign_spy_organization.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            print(data)
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.FOREIGN_SPY_ORGANIZATION")
    for x in cursor:
        print(x)

#Spy FOREIGN_SPY
def insert_foreign_spy():
    insert_command = ("INSERT INTO Spy.FOREIGN_SPY (Spy_code_name, Org_name) VALUES (%s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.FOREIGN_SPY")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("foreign_spy.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            print(data)
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT Org_name FROM Spy.FOREIGN_SPY")
    for x in cursor:
        print(x)

#Spy GADGET
def insert_gadget():
    insert_command = ("INSERT INTO Spy.GADGET (Service_tag, Cost, Description, Agent_id) VALUES (%s, %s, %s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.GADGET")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("gadget_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            print(data)
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.GADGET")
    for x in cursor:
        print(x)

#Spy FOREIGN_SPY_SIGHTING
def insert_foreign_spy_sighting():
    insert_command = ("INSERT INTO Spy.FOREIGN_SPY_SIGHTING (Spy_code_name, Date, Address) VALUES (%s, %s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.FOREIGN_SPY_SIGHTING")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("foreign_spy_sighting_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            print(data)
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.FOREIGN_SPY_SIGHTING")
    for x in cursor:
        print(x)

#Spy COMMON_LOCATION
def insert_common_location():
    insert_command = ("INSERT INTO Spy.COMMON_LOCATION (Target_code_name, Address) VALUES (%s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.COMMON_LOCATION")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("common_location_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            print(data)
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.COMMON_LOCATION")
    for x in cursor:
        print(x)

#Spy TARGET_SIGHTING
def insert_target_sighting():
    insert_command = ("INSERT INTO Spy.TARGET_SIGHTING (Target_code_name, Date, Address) VALUES (%s, %s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.TARGET_SIGHTING")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("target_sighting_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            print(data)
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.TARGET_SIGHTING")
    for x in cursor:
        print(x)

#Spy OPERATOR
def insert_operator():
    insert_command = ("INSERT INTO Spy.OPERATOR (Agent_id,Unit_id) VALUES (%s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.OPERATOR")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("operator_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            print(data)
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.OPERATOR")
    for x in cursor:
        print(x)

#Spy ALIAS
def insert_alias():
    insert_command = ("INSERT INTO Spy.ALIAS (Spy_code_name, Name, Address, Occupation) VALUES (%s, %s, %s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.ALIAS")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("alias_list_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.ALIAS")
    for x in cursor:
        print(x)

#Spy OTHER
def insert_other():
    insert_command = ("INSERT INTO Spy.OTHER (Agent_id, Occupation) VALUES (%s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.OTHER")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("other_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.OTHER")
    for x in cursor:
        print(x)

#Spy MEANS_OF_CONTACT
def insert_means_of_contact():
    insert_command = ("INSERT INTO Spy.MEANS_OF_CONTACT (Agent_id, Contact_line, Sattelite_link_address, Delivery_point) VALUES (%s, %s, %s, %s)")
    try:
        cursor.execute("DELETE FROM Spy.MEANS_OF_CONTACT")
        print('Table deleted')
    except Exception as err:
        print('Reject the deletion')
    print(insert_command)
    with open("means_of_contact_file.csv", "r") as file:
        f = csv.reader(file)
        for i in f:
            data = list(i)
            #data[1] = int(data[1])
            #data[5] = int(data[5])
            #data[4] = int(data[4])
            #data[6] = int(data[6])
            #data = tuple(data)
            #print(type(data))
            try:
                cursor.execute(insert_command, tuple(i))
            except Exception as err:
                print(err)
    cursor.execute("SELECT * FROM Spy.MEANS_OF_CONTACT")
    for x in cursor:
        print(x)

#execute insert commands
insert_agent()
insert_firearm()
insert_target()
insert_unit()
insert_spy()
insert_home_spy()
insert_foreign_spy_organization()
insert_foreign_spy()
insert_foreign_spy_sighting()
insert_common_location()
insert_target_sighting()
insert_operator()
insert_alias()
insert_other()
insert_means_of_contact()
#commit changes
mysql.commit()
