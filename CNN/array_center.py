import numpy as np

def calculate_com(arr):
    x_sum = 0
    y_sum = 0
    m_sum = 0
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            if(arr[x][y]==1):
                x_sum+=x
                y_sum+=y
                m_sum+=1
    if m_sum==0:
        return arr
    return (round(x_sum/m_sum),round(y_sum/m_sum))

def center(arr):
    com = calculate_com(arr)
    x_correction = com[0]-32
    y_correction = com[1]-32
    new_arr = np.zeros((64,64))
    for x in range(64):
        for y in range(64):
            if(arr[x][y]==1):
                new_x = x-x_correction
                new_y = y-y_correction
                if (0<=new_x and new_x<=63) and (0<=new_y and new_y<=63):
                    new_arr[new_x][new_y] = 1
    return new_arr