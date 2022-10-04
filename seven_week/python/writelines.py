def main():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    outfile = open('C:\Users\Yothgewalt\Desktop\computer-programming-lecture-at-university\cities.txt', 'w')
    
    cities = map(lambda x: x+'\n', cities)
    outfile.writelines(cities)
    
    outfile.close()
    
if __name__ == '__main__':
    main()