additional_lines = ["Stars up above,\n", "Whispers words of love"]
with open("poem.txt", "a") as file:
    # file.write("Roses are red,\n")
    # file.write("Violets are blue,\n")
    # file.write("Sugar is sweet,\n")
    # file.write("So are you!\n")
    file.writelines(additional_lines)
