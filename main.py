def getCSV():
    import csv
    with open('data.csv') as csvfile:
        return list(csv.DictReader(csvfile))

data = getCSV()

def q_1():
    nationalities = list()
    for row in data:
        nationalities.append(row['nationality'])
    nationalities = set(nationalities)
    return len(nationalities)

def q_2(): 
    club = list()
    for row in data:
        club.append(row['club'])
    club = set(club)
    return len(club)

def q_3():
    name = list()
    for row in data:
        name.append(row['full_name'])
    return name[:20]

def q_4():
    sortedData = data
    wage = list()
    def getWage(e):
        return float(e['eur_wage'])
    sortedData.sort(key=getWage, reverse=True)
    i = 0
    for row in sortedData:
        if (i < 10):
            wage.append(row['full_name'])
            i += 1
    return wage

def q_5():
    sortedData = data
    age = list()
    def getAge(e):
        return int(e['age'])
    sortedData.sort(key=getAge, reverse=True)
    i = 0
    for row in sortedData:
        if(i < 10):
            age.append(row['full_name'])
            i += 1
    return age   

def q_6():
    ages = data
    from collections import Counter
    ages = dict(Counter([int(age['age']) for age in ages]))  
    return ages
