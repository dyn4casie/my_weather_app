# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    #Open the file
    file = open("./story.txt","r")
    #Read the file and store in a variable
    read_file_content = file.read()
    return read_file_content
read_file_content("./story.txt")
    # [assignment] Add your code here 
    


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = read_file_content("./story.txt")
    split_text = text.split()
    #print(split_text)
    counts ={}
    for word in split_text:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(count_words())