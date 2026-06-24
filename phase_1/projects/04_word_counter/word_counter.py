filename = "sample.txt"

try:
    with open(filename, "r") as f:
        text = f.read().lower()

    words = text.split()
    count = {}
    
    for x in words:
        # Strips explicit punctuation from each individual word
        clean_word = x.strip(".,!?;:'\"")
        if clean_word:
            if clean_word not in count:
                count[clean_word] = 1
            else:
                count[clean_word] += 1
            
    print(count)
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")