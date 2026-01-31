import csv
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []

def get_pos(x):
    with open("assets/positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    striped = x.split()
    new = []
    for k in striped:
        b = list(k)
        for g in b:
            if g in punctuation_chars:
                b.remove(g)
        j = "".join(b)
        new.append(j)
    c = 0
    for i in new:
        i = i.lower()
        if i in positive_words:
            c += 1
    return c

# list of negative words to use
negative_words = []

def get_neg(x):
    with open("assets/negative_words.txt") as neg_f:
        for lin in neg_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
    striped = x.split()
    new = []
    for k in striped:
        b = list(k)
        for g in b:
            if g in punctuation_chars:
                b.remove(g)
        j = "".join(b)
        new.append(j)
    c = 0
    for i in new:
        i = i.lower()
        if i in negative_words:
            c += 1
    return c

New_Data = []
with open("assets/project_twitter_data.csv","r") as ptd_row:
    reader = csv.reader(ptd_row)
    header = next(reader)
    for row in reader:
        Net_Score = ""
        if get_pos(row[0]) > get_neg(row[0]):
            Net_Score += "Positive"
        elif get_pos(row[0]) == get_neg(row[0]):
            Net_Score += "Neutral"
        else:
            Net_Score += "Negative"
        New_Data.append([row[1],row[2],get_pos(row[0]),get_neg(row[0]),get_pos(row[0])-get_neg(row[0])])

with open("resulting_data.csv","w") as result:
    new = csv.writer(result)
    new.writerow(["Number of Retweets","Number of Replies","Positive Score","Negative Score","Net Score"])
    new.writerows(New_Data)
        
