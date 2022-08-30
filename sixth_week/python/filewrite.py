def main():
    outfile = open("philosophers.txt", "w")

    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")

    outfile.close()

if __name__ == "__main__":
    main()