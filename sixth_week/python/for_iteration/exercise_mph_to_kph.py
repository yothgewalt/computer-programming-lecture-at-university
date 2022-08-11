def main():
    print("KPH\tMPH")
    print("--------------")

    for kilometer in range(60, 140, 10):
        mile = kilometer * 0.6214
        print("{}\t{:.1f}".format(kilometer, mile))

    print("--------------")

if __name__ == "__main__":
    main()