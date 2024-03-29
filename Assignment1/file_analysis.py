def analyze_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            line_count = content.count("\n") + 1
            char_count = len(content)
            word_count = len(content.split())
            file_info = {
                "characters": char_count,
                "words": word_count,
                "lines": line_count,
            }
            return file_info
    except FileNotFoundError:
        print("File not found.")
        return {"characters": 0, "words": 0, "lines": 0}


def search_word(file_name, word):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            words = content.split()
            word_count = sum(1 for w in words if w.lower() == word.lower())
            return word_count
    except FileNotFoundError:
        print("File not found.")
        return 0


# Test cases for analyze_file()
print(analyze_file("sample.txt"))  # Assuming sample.txt is present
# Expected Output: {"characters": 68, "words": 12, "lines": 3}

print(analyze_file("nonexistent_file.txt"))  # Test case for nonexistent file
# Expected Output: {"characters": 0, "words": 0, "lines": 0}

# Test cases for search_word()
print(search_word("sample.txt", "Lorem"))  # Assuming sample.txt is present
# Expected Output: 1 (Assuming "Lorem" occurs once in sample.txt)

print(search_word("sample.txt", "nonexistentword"))  # Test case for word not found
# Expected Output: 0

print(search_word("nonexistent_file.txt", "word"))  # Test case for nonexistent file
# Expected Output: 0
