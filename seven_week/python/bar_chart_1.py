from turtle import color
import matplotlib.pyplot as plt

def main():
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    bar_width = 5
    
    plt.bar(left_edges, heights, bar_width, color=('b'))
    plt.show()
    
if __name__ == '__main__':
    main()