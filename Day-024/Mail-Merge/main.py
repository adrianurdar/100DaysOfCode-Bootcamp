# Create a letter using starting_letter.docx

# Read the invited names file line by line
with open("./Input/Names/invited_names.txt", mode="r") as data:
    raw_names = data.readlines()

# Clear names of the "\n"
names = []
for raw_name in raw_names:
    name = raw_name.strip("\n")
    names.append(name)

print(names)

# Read the content of the starting letter
with open("./Input/Letters/starting_letter.docx") as letter:
    letter = letter.read()

# Change signature to my signature
letter = letter.replace("Angela", "Adrian")

for name in names:
    # Replace the [name] placeholder with the actual name.
    new_letter = letter.replace("[name]", name)
    print(new_letter)

    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode="w") as file:
        file.write(new_letter)
