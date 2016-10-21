filtered_words = ["the"]

def Parse_Input(user_input):
    output = ""

    for char in user_input.lower():
        if char.isdigit() or char.isalpha() or char == " ":
            output += char

    while "  " in output:
        output.replace("  ", " ")

    user_input = []
    output = output.split(" ")
    
    for word in output:
        if word not in filtered_words:
            user_input.append(word)
    
    return user_input
