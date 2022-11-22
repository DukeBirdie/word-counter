i = input("Input words to count: ",)
j = 0
for k in i:
    if k == ' ':
        j += 1
    else:
        continue
    
    if k == "  ":
        break
print("Word count: ", j-1)