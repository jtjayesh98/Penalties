import csv
import random
  
  
# reading the database


file = open('WorldCupShootouts.csv')
csvreader = csv.reader(file)


header = []
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append((row[7], row[6]))


file.close()

# print(int(rows[1][1]))

adsilva = 23/30
ansilva = 28/36
nani = 12/20
moutinho = 12/15
ronaldo = 144/173

penalties = []

for i in range(10):
    goals = 0
    attempts = 0
    for j in range(len(rows)):
        # print(i+1 == int(rows[j][0]))
        if i+1 == int(rows[j][0]):
            if rows[j][1] != '':
                attempts = attempts + 1
                # print(rows[j][1])
                goals = goals + int(rows[j][1])
    penalties.append(goals/attempts)


penalty = random.randint(1, 100)/100

case1 = [ronaldo, moutinho, adsilva, ansilva, nani]
case2 = [nani, ansilva, adsilva, moutinho, ronaldo]

team1 = [penalties[0], penalties[2], penalties[4], penalties[6], penalties[8]]
team2 = [penalties[1], penalties[3], penalties[5], penalties[7], penalties[9]]

iterations = 100
c1 = []
c12 = []
c2 = []
c22= []
for i in range(10000):
    penalty = random.randint(1, 100)/100
    score1 = []
    score2 = []
    for j in range(5):
        if penalty >= (1-case1[j])*(1-team1[j]):
            score1.append(1)
        else:
            score1.append(0)
        if penalty >= (1-case2[j])*(1-team1[j]):
            score2.append(1)
        else:
            score2.append(0)
    c1.append(score1)
    c2.append(score2)

for i in range(10000):
    penalty = random.randint(1, 100)/100
    score1 = []
    score2 = []
    for j in range(5):
        if penalty >= (1-case1[j])*(1-team2[j]):
            score1.append(1)
        else:
            score1.append(0)
        if penalty >= (1-case2[j])*(1-team2[j]):
            score2.append(1)
        else:
            score2.append(0)
    c12.append(score1)
    c22.append(score2)
final1 = []
final2 = []
for i in range(len(c1)):
    final1.append(sum(c1[i]))
for i in range(len(c2)):
    final2.append(sum(c2[i]))
final12 = []
final22 = []
for i in range(len(c12)):
    final12.append(sum(c12[i]))
for i in range(len(c22)):
    final22.append(sum(c22[i]))
goals1 = []
goals2 = []
for i in range(6):
    goal1 = 0
    goal2 = 0
    for j in range(len(final1)):
        if final1[j] == i:
            goal1 = goal1 + 1
        if final2[j] == i:
            goal2 = goal2 + 1
    goals1.append(goal1)
    goals2.append(goal2)
# print(goals1)
print(len(final1))
print(len(final2))
f = open("results.csv", "w")
writer = csv.writer(f)
for i in range(len(final1)):
    data = [final1[i], final2[i]]
    writer.writerow(data)
f.close()

f = open("tally.csv", "w")
writer = csv.writer(f)
for i in range(len(goals1)):
    data = [goals1[i], goals2[i]]
    writer.writerow(data)
f.close()

goals12 = []
goals22 = []
for i in range(6):
    goal1 = 0
    goal2 = 0
    for j in range(len(final12)):
        if final12[j] == i:
            goal1 = goal1 + 1
        if final22[j] == i:
            goal2 = goal2 + 1
    goals12.append(goal1)
    goals22.append(goal2)
# print(goals1)
print(len(final12))
print(len(final22))
f = open("results2.csv", "w")
writer = csv.writer(f)
for i in range(len(final12)):
    data = [final12[i], final22[i]]
    writer.writerow(data)
f.close()

f = open("tally2.csv", "w")
writer = csv.writer(f)
for i in range(len(goals12)):
    data = [goals12[i], goals22[i]]
    writer.writerow(data)
f.close()