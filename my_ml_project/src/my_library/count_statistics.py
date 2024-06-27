import pykakasi

def count_1(d1, d2, sentence):
    p, n, e = 0, 0, 0
    cue = []
    d2_new = regroup(d2)
    for i in range(len(sentence)):
        for j in range(len(sentence) - i):
            print(sentence[j:j+i+1], d1.get(sentence[j:j+i+1]), d2_new.get(sentence[j:j+i+1]))
            if d1.get(sentence[j:j+i+1]) != None:
                if d1.get(sentence[j:j+i+1]) == "p":
                    p += 1
                    cue.append([sentence[j:j+i+1], j, j+i+1, "p"])
                elif d1.get(sentence[j:j+i+1]) == "n":
                    n += 1
                    cue.append([sentence[j:j + i + 1], j, j + i + 1, "n"])
                else:
                    e += 1
                    cue.append([sentence[j:j + i + 1], j, j + i + 1, "e"])
            if d2_new.get(sentence[j:j+i+1]) != None:
                if d2_new.get(sentence[j:j+i+1]) == "ネガ（経験）" or d2_new.get(sentence[j:j+i+1]) == "ネガ（評価）":
                    n += 1
                    cue.append([sentence[j:j + i + 1], j, j + i + 1, "n"])
                if d2_new.get(sentence[j:j+i+1]) == "ポジ（評価）" or d2_new.get(sentence[j:j+i+1]) == "ポジ（経験）":
                    p += 1
                    cue.append([sentence[j:j + i + 1], j, j + i + 1, "p"])
    print(p, n, e)
    Mood_result = [p, n, e]
    return Mood_result, cue, sentence

def count(d1, d2, sentence):
    p, n, e = 0, 0, 0
    cue = []
    #punctuation = []
    d2_new = regroup(d2)
    kks = pykakasi.kakasi()
    word_group = kks.convert(sentence)
    for word_index in word_group:
        #print(word_index['orig'].find("。"), word_index['orig'].find("、"))
        if word_index['orig'].find("。")!= -1:
            #punctuation.append(["。", word_index['orig'].index("。")])
            word_index['orig'] = word_index['orig'][:word_index['orig'].index("。")]

        if word_index['orig'].find("、")!= -1:
            #punctuation.append(["、", word_index['orig'].index("、")])
            word_index['orig'] = word_index['orig'][:word_index['orig'].index("、")]

        if word_index['hira'].find("。")!= -1:
            #punctuation.append(["。", word_index['hira'].index("。")])
            word_index['hira'] = word_index['hira'][:word_index['hira'].index("。")]

        if word_index['hira'].find("、")!= -1:
            #punctuation.append(["、", word_index['hira'].index("、")])
            word_index['hira'] = word_index['hira'][:word_index['hira'].index("、")]

        #print(word_index['orig'], d1.get(word_index['orig']), d2_new.get(word_index['orig']), word_index['hira'], d1.get(word_index['hira']), d2_new.get(word_index['hira']))
        if d1.get(word_index['orig']) != None:
            if d1.get(word_index['orig']) == "p":
                p += 1
                cue.append([word_index['orig'], "p"])
            elif d1.get(word_index['orig']) == "n":
                n += 1
                cue.append([word_index['orig'], "n"])
            else:
                e += 1
                cue.append([word_index['orig'], "e"])

        elif d1.get(word_index['hira']) != None:
            if d1.get(word_index['hira']) == "p":
                p += 1
                cue.append([word_index['hira'], "p"])
            elif d1.get(word_index['hira']) == "n":
                n += 1
                cue.append([word_index['hira'], "n"])
            else:
                e += 1
                cue.append([word_index['hira'], "e"])

        if d2_new.get(word_index['orig']) != None:
            if d2_new.get(word_index['orig']) == "ネガ（経験）" or d2_new.get(word_index['orig']) == "ネガ（評価）":
                n += 1
                cue.append([word_index['orig'], "n"])
            elif d2_new.get(word_index['orig']) == "ポジ（評価）" or d2_new.get(word_index['orig']) == "ポジ（経験）":
                p += 1
                cue.append([word_index['orig'], "p"])

        elif d2_new.get(word_index['hira']) != None:
            if d2_new.get(word_index['hira']) == "ネガ（経験）" or d2_new.get(word_index['hira']) == "ネガ（評価）":
                n += 1
                cue.append([word_index['hira'], "n"])
            elif d2_new.get(word_index['hira']) == "ポジ（評価）" or d2_new.get(word_index['hira']) == "ポジ（経験）":
                p += 1
                cue.append([word_index['hira'], "p"])

    #print(p, n, e)
    Mood_result = [p, n, e]
    return Mood_result, cue, sentence



def regroup(d2):
    d2_new = {}
    # regroup d2 and key
    for i in range(len(list(d2.items()))):
        p = list(d2.items())[i][0]
        if p.find("る") != -1:
            d2_new.update({p[:list(p).index("る")]: list(d2.items())[i][1]})
        if p.find("る ") != -1:
            s = p.split(" ")
            d2_new.update({p[:list(p).index(" ")]: list(d2.items())[i][1]})
            for j in range(len(s) - 1):
                re = s[0].replace("る" , s[j+1])
                d2_new.update({re: list(d2.items())[i][1]})

            d2_new.update({s[0].replace("る", "たい"): list(d2.items())[i][1]})

        elif p.find(" ") != -1:
            while p.find(" ") != -1:
                p = p[:list(p).index(" ")] + p[list(p).index(" ") + 1:]
            d2_new.update({p: list(d2.items())[i][1]})
        else:
            d2_new.update({p: list(d2.items())[i][1]})

    return d2_new

#regroup d1(noun --> adjective)

