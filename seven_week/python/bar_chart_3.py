from turtle import color
import matplotlib.pyplot as plt

def main():
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    
    bar_width = 10
    
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'c', 'k'))
    
    plt.title('Sales by Year')
    
    plt.xlabel('Year')
    plt.ylabel('Sales')
    
    plt.xticks([5, 15, 25, 35, 45],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],
               ['$0n', '$1n', '$2n', '$3n', '$4n', '$5n'])
    
    plt.show()
    
main()