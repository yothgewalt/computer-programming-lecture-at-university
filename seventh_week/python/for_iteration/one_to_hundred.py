from __future__ import division


def one_to_hundred():
    for hundred in range(1, 101):
        print("%s\t" % hundred, end=" ")

        if hundred % 20 == 0:
            print("\n")

if __name__ == "__main__":
    one_to_hundred()