# Put your code here
def print_unique_words_sorted():
#     input('Enter file name (example.txt)')
    with open('example.txt', 'r') as file:
        contents = file.read().strip().split()
        s = sorted(list(set(contents)))
        print(s)
        return s

print_unique_words_sorted()
