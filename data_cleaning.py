import csv

array = []
with open("data/german.txt", "r") as data_file:
    for row in data_file.readlines():
        word = row.replace(" â€“ ", ",")
        word = word.replace(" ~ ", ",")
        word = word.replace(". ", ",")
        word = word.split(",")
        array.append(word)
        for l in array:
            l[3] = l[3].strip("\n")

with open("data/ger_to_eng.csv", "w") as f:
    w = csv.writer(f, delimiter = ",")
    w.writerows(array)

