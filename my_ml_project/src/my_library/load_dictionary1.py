import csv
import pykakasi


def load_dictionary1(file_path):
    polarity_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if len(row) >= 2:
                word = row[0].strip()
                polarity = row[1].strip()
                polarity_dict[word] = polarity
    return polarity_dict


def load_dictionary2(file_path):
    polarity_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if len(row) >= 2:
                polarity = row[0].strip()
                word = row[1].strip()
                polarity_dict[word] = polarity
    return polarity_dict

def kanji_conversion(kanji):
    kks = pykakasi.kakasi()
    if kks.convert(kanji)[0].get("orig") != kanji:
        return kks.convert(kanji)[0].get("hira")
    else:
        return "It is Hiragana"
