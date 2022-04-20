from numpy import *
def main():
    X = linspace(0,2*pi,1000)
    Y = sin(X)
    Table = concatenate((X,Y), axis= 1000)
    print(Table)
    
if __name__ == '__main__':
    main()
    