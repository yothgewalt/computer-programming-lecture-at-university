import random

ROWS = 3
COLS = 4

def find_bigest_numeric(values):
    bigest = values[0][0]
    for rows in values:
        for columns in rows:
            if columns > bigest:
                bigest = columns
                
            return bigest

def main():
    sum_value = 0
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)
            
    for r in range(ROWS):
        for c in range(COLS):
            sum_value += values[r][c]
            
    
    print(values)
    print(find_bigest_numeric(values))        
    print(sum_value)
    
if __name__ == '__main__':
    main()