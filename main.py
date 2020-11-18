import random
import json

name = input("Файл: ")
t = int(input("Количество предложений: "))

try:
    #======Getting save======
    print("Getting save")
    with open(name+"-save.json", 'r') as file:
        words = json.loads(file.read())
except:
    #=======Loading==========
    print("Loading")
    text = "START "
    end = ['!', "?", '.']
    with open(name+".txt", 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha() or char in end or char==" ":
                    if char in end:
                        text += " END START "
                    elif char == ' ' and text[-1] == ' ':
                        continue
                    else:
                        text += char.lower()
        file.close()
        
    if text[-6:] == 'START ':
        text = text[:-7]
    else:
        text += ' END'

    #=======Creating==========
    print("Creating")
    words = {}
    word_list = text.split()
    i = 0
    for word in word_list:
        i += 1
        if word == 'END':
            continue
        try:
            words[word][word_list[i]]+=1
        except:
            try:
                words[word][word_list[i]]=1
            except:
                words[word]={word_list[i]:1}

    #=======Saving==========
    print("Saving")
    with open(name+"-save.json", 'w') as file:
        json.dump(words, file)
        file.close()
            
#=======Constructing==========
print("Constructing")
for times in range(0,t):
    out = ""
    current = 'START'
    i =0
    while current != 'END' and i != 40:
        rand_sum = sum(words[current].values())
        rand = random.randrange(rand_sum)
        position = 0
        for el in words[current]:
            position += words[current][el]
            if rand < position:
                current = el
                break
        out += ' ' + current
        i += 1
    out = out[1].upper() + out[2:-4] + '.'
    print(out)














