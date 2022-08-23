if __name__ == "__main__":
    balloon = "          Anirach has a balloon.          "
    print("[", balloon.strip(), "]")
    print("[", balloon.lstrip(), "]")
    print("[", balloon.rstrip(), "]")

    balloon = "##########Anirach has a balloon.##########"
    print("[", balloon.strip("#"), "]")
    print("[", balloon.rstrip("#"), "]")