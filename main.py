# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

def getCSV():
    import csv
    with open('data.csv') as csvfile:
        return list(csv.DictReader(csvfile))

data = getCSV()
# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 
def q_1():

    nationalities = list()

    for row in data:
        nationalities.append(row['nationality'])

    nationalities = set(nationalities)

    return len(nationalities)

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    
    club = list()

    for row in data:
        club.append(row['club'])

    club = set(club)

    return len(club)

# **Q3.** Liste o primeiro nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():

    name = list()

    for row in data:
        name.append(row['full_name'].split(' ', 1)[0])

    return name[:20]

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():

    sortedData = data
    wage = list()

    def getWage(e):
        return e['eur_wage']

    sortedData.sort(key=getWage, reverse=True)

    i = 0
    for row in sortedData:
        if (i < 10):
            wage.append(row['full_name'])
            wage.append(row['eur_wage'])
            i += 1

    return wage
# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():

    sortedData = data
    age = list()

    def getAge(e):
        return e['age']

    sortedData.sort(key=getAge, reverse=True)

    i = 0
    for row in sortedData:
        if(i < 10):
            age.append(row['full_name'])
            age.append(row['age'])
            i += 1

    return age   

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    ages = data
    from collections import Counter
    ages = dict(Counter([age['age'] for age in ages]))
    
    return ages