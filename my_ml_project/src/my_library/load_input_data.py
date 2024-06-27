def load(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = file.read()
        splited_data = data.split()
    return splited_data
