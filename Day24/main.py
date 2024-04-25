#file = open("my_file.txt")

#contents = file.read()
#print(contents)


with open("\\Users\Mateusz\Desktop\my_file.txt", mode="r") as file:
    content = file.read()
    print(content)




file.close()
