import matplotlib.pyplot as plt

def main():
    sales = [100, 400, 300, 600]
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']
    plt.pie(sales, labels=slice_labels)
    plt.title('Sales by Quarter')
    plt.show()
    
main()