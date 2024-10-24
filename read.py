# file = open("dad_jokes.txt","r")
# content = file.read()
# print(content)
# file.close()

# file = open("dad_jokes.txt","r")
# lines = file.readlines()
#
# for line in lines:
#     print(line)
#
# file.close()

with open("dad_jokes.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip().upper())

