string = "Four score and seven years ago"
position = string.find("seven")
if position != -1:
    print("The word \"seven\" was found at index", position)
else:
    print("The word \"seven\" was not found.")