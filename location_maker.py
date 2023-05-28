from math import cos, pi, sin
import random

def main():
    f = open('location.txt', 'w')
    i = 0

    for i in range(50):

        f.write(str(i+1) + '\n')

        f.write('gx = [' + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ','
                + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ',' 
                + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ']\n')
        f.write('gy = [' + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ','
                + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ',' 
                + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ']\n')
        f.write('sx = [' + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ','
                + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ',' 
                + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ']\n')
        f.write('sy = [' + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ','
                + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ',' 
                + str(round(random.uniform(-2.5,2.5), 3)) + ',' + str(round(random.uniform(-2.5,2.5), 3)) + ']\n')
        i +=1
    
    f.close()

main()
        