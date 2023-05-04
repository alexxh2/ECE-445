import csv
import pandas as pd
import matplotlib.pyplot as plt
from numpy import nan
from mpl_toolkits import mplot3d
import numpy as np

lim = 50
trial_num = 5
trial_num = str(trial_num)

def parse():
    """
    parse first reads the input data in as a .csv file and then clean the data of any gaps in data. 
    It then calculates the coordinate % error for each frame in the data set and creates the appropriate
    graphs that help visualize the discrepencies between the LEDs and reflective balls.

    input: none
    return value: none
    output: graphs depicting %errors and position
    """

    # get input data and parse

    idta_file = 'Test 1 Both Objects (Team 78).csv'
    idf = pd.read_csv(idta_file,encoding='cp1252', skiprows=3)

    framedata = idf['Frame'].tolist()[1:]

    posx = idf['TX'].tolist()[1:]
    posy = idf['TY'].tolist()[1:]
    posz = idf['TZ'].tolist()[1:]

    aposx = idf['TX.1'].tolist()[1:]
    aposy = idf['TY.1'].tolist()[1:]
    aposz = idf['TZ.1'].tolist()[1:]


    # clean data
    while (nan in posx):
        i = posx.index(nan)
        del framedata[i]
        del posx[i]
        del posy[i]
        del posz[i]
        del aposx[i]
        del aposy[i]
        del aposz[i]
    
    while (nan in posy):
        i = posy.index(nan)
        del framedata[i]
        del posx[i]
        del posy[i]
        del posz[i]
        del aposx[i]
        del aposy[i]
        del aposz[i]

    while (nan in posz):
        i = posz.index(nan)
        del framedata[i]
        del posx[i]
        del posy[i]
        del posz[i]
        del aposx[i]
        del aposy[i]
        del aposz[i]

    while (nan in aposx):
        i = aposx.index(nan)
        del framedata[i]
        del posx[i]
        del posy[i]
        del posz[i]
        del aposx[i]
        del aposy[i]
        del aposz[i]

    while (nan in aposy):
        i = aposy.index(nan)
        del framedata[i]
        del posx[i]
        del posy[i]
        del posz[i]
        del aposx[i]
        del aposy[i]
        del aposz[i]

    while (nan in aposz):
        i = aposz.index(nan)
        del framedata[i]
        del posx[i]
        del posy[i]
        del posz[i]
        del aposx[i]
        del aposy[i]
        del aposz[i]


    percent_errors_x = []
    percent_errors_y = []
    percent_errors_z = []
    percent_errors_total = []
    newframe = []
    nposx = []
    nposy = []
    nposz = []
    naposx = []
    naposy = []
    naposz = []

    # calculate % errors

    for n in range(len(framedata)):

        p_error_x = p_error(posx[n], aposx[n])
        p_error_y = p_error(posy[n], aposy[n])
        p_error_z = p_error(posz[n], aposz[n])

        p_error_total = p_error_x + p_error_y + p_error_z

        if abs(p_error_total) < lim:
            percent_errors_x.append(p_error_x)
            percent_errors_y.append(p_error_y)
            percent_errors_z.append(p_error_z)
            percent_errors_total.append(p_error_total)
            newframe.append(float(framedata[n]))
            nposx.append(float(posx[n]))
            nposy.append(float(posy[n]))
            nposz.append(float(posz[n]))
            naposx.append(float(aposx[n]))
            naposy.append(float(aposy[n]))
            naposz.append(float(aposz[n]))

    print(np.median(percent_errors_total))

    '''

    #PLOTTING DATA

    # total % error
    x = newframe
    y = percent_errors_total

    fig = plt.figure()
    ax = plt.axes()
    ax.plot(x, y)

    ax.set(xlabel='Frames', ylabel='Total Percent Error')

    fig.suptitle('Total % Error between Reflective Balls and 780 nm LEDs for Trial ' + trial_num,fontsize=12,ha='center')

    ax.grid()
    fig.savefig("Total % Error Graph.png")
    plt.show()
    
    # coordinate % error
    x = newframe
    y = percent_errors_total
    i = percent_errors_x
    j = percent_errors_y
    k = percent_errors_z

    fig, ax = plt.subplots()
    ax.plot(x, i, "-b", label = "Percent error x")
    ax.plot(x, j, "-r", label = "Percent error y")
    ax.plot(x, k, "-g", label = "Percent error z")
    ax.legend(loc="upper right")

    ax.set(xlabel='Frames', ylabel='Coordinate Percent Errors')
    fig.suptitle('Coordinate % Error between Reflective Balls and 780 nm LEDs for Trial ' + trial_num,fontsize=11,ha='center')
    
    ax.grid()
    fig.savefig("Coordinate % Error Graph.png")
    plt.show()
    
    #x values
    a = nposx
    b = naposx

    fig, ax = plt.subplots()
    ax.plot(x, a, "-b", label = "LED x value")
    ax.plot(x, b, "-r", label = "Reflective Ball x value")
    ax.legend(loc="upper right")

    ax.set(xlabel='Frames', ylabel='X Coordinate Values (mm)')
    fig.suptitle('X values between Reflective Balls and 780 nm LEDs for Trial ' + trial_num,fontsize=12,ha='center')
    
    ax.grid()
    fig.savefig("X values.png")
    plt.show()

    # y values
    a = nposy
    b = naposy

    fig, ax = plt.subplots()
    ax.plot(x, a, "-b", label = "LED y value")
    ax.plot(x, b, "-r", label = "Reflective Ball y value")
    ax.legend(loc="upper right")

    ax.set(xlabel='Frames', ylabel='Y Coordiniate Values (mm)')
    fig.suptitle('Y values between Reflective Balls and 780 nm LEDs for Trial ' + trial_num,fontsize=12,ha='center')
    
    ax.grid()
    fig.savefig("Y values.png")
    plt.show()

    #z values

    a = nposz
    b = naposz

    fig, ax = plt.subplots()
    ax.plot(x, a, "-b", label = "LED z value")
    ax.plot(x, b, "-r", label = "Reflective Ball z value")
    ax.legend(loc="upper right")

    ax.set(xlabel='Frames', ylabel='Z Coordiniate Values (mm)')
    fig.suptitle('Z values between Reflective Balls and 780 nm LEDs for Trial ' + trial_num,fontsize=12,ha='center')
    
    ax.grid()
    fig.savefig("Z values.png")
    plt.show()


    #3D graph
    x = nposx
    y = nposy
    z = nposz
    a_x = naposx
    a_y = naposy
    a_z = naposz

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z, 'blue', label = "LEDs")
    ax.plot3D(a_x, a_y, a_z, 'red', label = "Reflective balls")
    ax.legend()
    fig.suptitle('Coordinate Values (mm) for Reflective Balls and 780 nm LEDs for Trial ' + trial_num,fontsize=12,ha='center')
    
    ax.grid()
    fig.savefig("Coordinate Graph 3D.png")
    plt.show()


    x = nposx
    y = nposy

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, percent_errors_total, 'blue', label = "percent error")
    ax.plot3D(x, y, 0, 'red', label = "LED xy position")
    ax.legend()
    
    fig.suptitle('Percent error between Reflective Balls and 780 nm LEDs for Trial ' + trial_num,fontsize=12,ha='center')
    
    ax.grid()
    fig.savefig("% error Graph 3D.png")
    plt.show()
    '''

    


def median(p1, p2):
    return (p1 + p2) / 2

    
def p_error(observed, expected):

    # percent error = | (observed - expected) / expected | * 100

    return abs((float(observed) - float(expected)) / float(expected)) * 100


def main():
    parse()
      
if __name__ == "__main__":
    main()