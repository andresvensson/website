import MySQLdb, sys, time, random

def temp_read():
    db = MySQLdb.connect(host="10.0.0.160", user="temp", passwd="letmein", db="temp")
    cursor = db.cursor()
    RPi2 = "SELECT * FROM RPi2 ORDER BY Time DESC LIMIT 1"
    RPi3 = "SELECT * FROM RPi3 ORDER BY Time DESC LIMIT 1"
    OWM = "SELECT * FROM OWM ORDER BY Time DESC LIMIT 1"
    try:
        cursor.execute(RPi2)
        print("reading OK")

    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))

    data = cursor.fetchone()

    try:
         cursor.execute(RPi3)
    except:
        print("Error %d: %s" % (e.args[0], e.args[1]))

    data1 = cursor.fetchone()

    try:
         cursor.execute(OWM)
    except:
        print("Error %d: %s" % (e.args[0], e.args[1]))

    data2 = cursor.fetchone()

    data = data + (data1)
    data = data + (data2)

    print "values", data

    for rows in data:
        print rows

    #label = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", ]


    return data

    #Dator =	data1)[0]
    #Door = 	data1)[2]
    #Over Bed = data[5]
    #Under bed= data[7]
    #OWM = 	data[10]

    cursor.close()
    db.close()


def RPi2():
    db = MySQLdb.connect(host="10.0.0.160", user="temp", passwd="letmein", db="temp")
    cursor = db.cursor()
    RPi2 = "SELECT S1temp FROM RPi2 ORDER BY Time DESC LIMIT 48"
    try:
        cursor.execute(RPi2)
        print("reading OK")

    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))

    dataTuple = cursor.fetchall()


    # Pause this
    # Convert to list
    data = list(dataTuple)
    # Make it a list
    list_of_lists = map(list, data)

    # List the list of lists...
    values = [y for x in list_of_lists for y in x]

    #print"......TEST.......", values[0], values[2], values[4], values[6]

    dataTuple = cursor.fetchall()

    return values

    cursor.close()
    db.close()


def labels(amount):
    db = MySQLdb.connect(host="10.0.0.160", user="temp", passwd="letmein", db="temp")
    cursor = db.cursor()
    RPi2 = "SELECT Time FROM RPi2 ORDER BY Time DESC LIMIT " + str(amount)
    try:
        cursor.execute(RPi2)
        print("reading OK")

    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))

    times = cursor.fetchall()


    # Pause this
    # Convert to list
    data = list(times)
    # Make it a list
    list_of_lists = map(list, times)

    # List the list of lists...
    labels = [y for x in list_of_lists for y in x]

    #print"......TEST.......", values[0], values[2], values[4], values[6]

    dataTuple = cursor.fetchall()

    return labels

    cursor.close()
    db.close()


def random_ints(num, lower=0, upper=30):
        return [random.randrange(lower,upper+1) for i in range(num)]

#print random_ints(48)


def static_labels():
    #labels = ["now", "-0.15",-"0.30","-0.45","-1","-0.15","-0.30","-0.45","-2","-0.15","-0.30","-0.45","-3","-0.15","-0.30","-0.45","-4","-0.15","-0.30","-0.45","-5","-0.15","-0.30","-0.45","-6","-0.15","-0.30","-0.45","-7","-0.15","-0.30","-0.45","-8","-0.15","-0.30","-0.45","-9","-0.15","-0.30","-0.45","-10","-0.15","-0.30","-0.45","-11","-0.15","-0.30","-0.45","-12"]
    labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48"]
    return labels

def main_fetcher():
    print "....::::Fetching from DB::::...."
    temp_read()
    print "Bye"

    sys.exit()


if __name__ == "__main__":
    main_fetcher()
