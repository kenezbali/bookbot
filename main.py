def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        diction = {}
        sorter = []
        lowered = string_lower(file_contents)
        count = counter(file_contents)
        for letter in lowered:
            if letter not in diction:
                diction[letter] = 1
            else:
                diction[letter] = diction[letter] + 1
        for i in diction:
            if i.isalpha():
                sorter.append({"letter": i, "num": diction[i]})
            
        sorter.sort(reverse = True, key=sort_on)
        print(f"--- Begin report of {path_to_file} ---")
        print(f"{count} words found in the document")
        for i in sorter:
            print(f"The '{i['letter']}' character was found {i['num']} times")
        print("--- End report ---")
def string_lower (string):
    lowered = string.lower()
    return lowered

def sort_on(dict):
    return dict["num"]
def counter(string):
    words = string.split()
    count = 0
    for word in words:
        count += 1
    return count
main("books/frankenstein.txt")