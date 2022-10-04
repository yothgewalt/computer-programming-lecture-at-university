import matplotlib.pyplot as plt

def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    
    plt.plot(x_coords, y_coords, marker='o')
    
    plt.title('Sales by Year')
    
    plt.xlabel('Year')
    plt.ylabel('Sales')
    
    plt.xticks([0, 1, 2, 3, 4],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5],
               ['$0n', '$1n', '$2n', '$3n', '$4n', '$5n'])
    
    plt.grid(True)
    
    plt.show()
    
if __name__ == "__main__":
    main()