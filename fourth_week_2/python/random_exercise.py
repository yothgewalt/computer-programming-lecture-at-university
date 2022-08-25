from re import A


if __name__ == "__main__":
    message = input("original text: ")
    output_text = message

    previous_index = 0
    index = 0
    while index < len(message):
        if index > 0:
            pass
        else:
            output_text[index] += message[index].upper()
            print(output_text)

        index += 1
    
    print(len(output_text))

