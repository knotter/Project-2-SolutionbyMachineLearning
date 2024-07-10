import os

def load_1(file_path = "../data/dictionary1.txt"):
  print(file_path)
  with open(file_path, 'r', encoding="utf-8") as f:
    all_lines = f.read()
  all_lines_list = all_lines.strip().split("\n")
  res = []
  for all_lines in all_lines_list:
    res.append(all_lines.split("\t"))

  #print(res)
  return res

def load_2(file_path = "../data/dictionary2.txt"):
  print(file_path)
  with open(file_path, 'r', encoding="utf-8") as f:
    all_lines = f.read()
  all_lines_list = all_lines.strip().split("\n")
  res = []
  for all_lines in all_lines_list:
    convert = all_lines.split("\t")
    if convert[0] == "ネガ（経験）" or convert[0] == "ネガ（評価）":
      convert[0] = "n"
    else:
      convert[0] = "p"

    res.append([convert[1], convert[0]])

  print("res =",res)
  res_1 = []
  # regroup d2 and key
  for i in range(len(res)):
    p = res[i][0]

    if p.find("る ") != -1:
      s = p.split(" ")
      if res_1.count([res[i][0], res[i][1]]) == 0:
        res_1.append([p[:p.index(" ")], res[i][1]])
      for j in range(len(s) - 1):
        re = s[0].replace("る", s[j + 1])
        res_1.append([re, res[i][1]])

      res_1.append([s[0].replace("る", "たい"), res[i][1]])

    elif p.find(" ") != -1:
      while p.find(" ") != -1:
        p = p[:list(p).index(" ")] + p[list(p).index(" ") + 1:]
      res_1.append([p, res[i][1]])
    else:
      res_1.append([p, res[i][1]])

  print("res_1=",res_1)
  return res_1


#dic_1 = load_1("C:/Users/obscu/PycharmProjects/python_Curriculum/9th/my_ml_project/data/dictionary1.txt")
#dic_2 = load_2("C:/Users/obscu/PycharmProjects/python_Curriculum/9th/my_ml_project/data/dictionary2.txt")
#print(dic_1 + dic_2)