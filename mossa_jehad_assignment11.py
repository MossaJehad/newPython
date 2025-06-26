with open('story.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    j = 0;
    i = 0;
    n = 1;
    while(i < len(data)):
        i += 1
    while(j < len(data)):
        if(data[j] == '\n' or data[j] == '\0'):
            n += 1
        j += 1
print("Content: \n", data, "\n")
print(f"Number of charcters: \n", i, "\n")
print(f"Number of lines: \n", n, "\n")
