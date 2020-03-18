# Put your code here
def print_beautiful_tabular_data():
    filename = input("What file do you want to read from?")
    table = ''
    try:
        with open(filename, 'r') as data:
            for line in data.readlines():
                print(line)
                words = line.split(" ")
                table += " ".join(words)
                table += "\n"
            print(table)
    except IOError:
        print("Issue reading file")

print_beautiful_tabular_data()