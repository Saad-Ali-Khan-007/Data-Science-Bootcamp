def analyze_file():
    file_name = input("Enter file name: ")
    file = open(file_name, "r")
    content = file.read()
    line_count = content.count("\n") + 1
    char = len(content)
    words = len(content.split())
    file_count = {"character": char, "word": words, "lines": line_count}
    print(file_count)
    file.close()


analyze_file()


def serach_word():
    file_name = input("Enter file name: ")
    input_word = input("Enter the word: ")
    file = open(file_name, "r")
    content = file.read()
    words = content.split()
    input_word_count = 0
    for word in words:
        if input_word.lower() == word.lower():
            input_word_count += 1
    print(input_word_count)
    file.close()


serach_word()
