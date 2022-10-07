import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import os

def rule110(frameNum, image, pattern, j):
    j.append(frameNum+1)
    if len(j) != len(set(j)):
        j[-1]+=1

    if j[-1] > len(pattern[0, :])-1:
        ani.FuncAnimation.pause(animation)

        return image

    for i in range(1, len(pattern)-1):
        if pattern[j[-1]-1,i+1] == pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i] == 1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1, i-1] == pattern[j[-1]-1,i] == 1 and pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==pattern[j[-1]-1,i+1]==1 and pattern[j[-1]-1,i]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==1 and pattern[j[-1]-1,i] == pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==0 and pattern[j[-1]-1,i+1]==pattern[j[-1]-1, i]==1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==pattern[j[-1]-1,i+1]==0 and pattern[j[-1]-1,i]==1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i] == 0 and pattern[j[-1] - 1, i + 1] == 1:
            pattern[j[-1], i] = 1
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i + 1] == pattern[j[-1] - 1, i] == 0:
            pattern[j[-1], i] = 0

    image.set_data(pattern)
    return image

def rule90(frameNum, image, pattern, j):
    j.append(frameNum+1)
    if len(j) != len(set(j)):
        j[-1]+=1

    if j[-1] > len(pattern[0, :])-1:
        ani.FuncAnimation.pause(animation)

        return image

    for i in range(1,len(pattern)-1):
        if pattern[j[-1]-1,i+1] == pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i] == 1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1, i-1] == pattern[j[-1]-1,i] == 1 and pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==pattern[j[-1]-1,i+1]==1 and pattern[j[-1]-1,i]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==1 and pattern[j[-1]-1,i] == pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==0 and pattern[j[-1]-1,i+1]==pattern[j[-1]-1, i]==1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i+1]==0 and pattern[j[-1]-1,i]==1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i] == 0 and pattern[j[-1] - 1, i + 1] == 1:
            pattern[j[-1], i] = 1
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i + 1] == pattern[j[-1] - 1, i] == 0:
            pattern[j[-1], i] = 0

    image.set_data(pattern)
    return image

def rule30(frameNum, image, pattern, j):
    j.append(frameNum+1)
    if len(j) != len(set(j)):
        j[-1]+=1

    if j[-1] > len(pattern[0, :])-1:
        ani.FuncAnimation.pause(animation)

        return image

    for i in range(1,len(pattern)-1):
        if pattern[j[-1]-1,i+1] == pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i] == 1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1, i-1] == pattern[j[-1]-1,i] == 1 and pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==pattern[j[-1]-1,i+1]==1 and pattern[j[-1]-1,i]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==1 and pattern[j[-1]-1,i] == pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==0 and pattern[j[-1]-1,i+1]==pattern[j[-1]-1, i]==1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i+1]==0 and pattern[j[-1]-1,i]==1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i] == 0 and pattern[j[-1] - 1, i + 1] == 1:
            pattern[j[-1], i] = 1
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i + 1] == pattern[j[-1] - 1, i] == 0:
            pattern[j[-1], i] = 0

    image.set_data(pattern)
    return image

def rule184(frameNum, image, pattern, j):
    j.append(frameNum+1)
    if len(j) != len(set(j)):
        j[-1]+=1

    if j[-1] > len(pattern[0, :])-1:
        ani.FuncAnimation.pause(animation)

        return image

    for i in range(1,len(pattern)-1):
        if pattern[j[-1]-1,i+1] == pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i] == 1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1, i-1] == pattern[j[-1]-1,i] == 1 and pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==pattern[j[-1]-1,i+1]==1 and pattern[j[-1]-1,i]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==1 and pattern[j[-1]-1,i] == pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==0 and pattern[j[-1]-1,i+1]==pattern[j[-1]-1, i]==1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i+1]==0 and pattern[j[-1]-1,i]==1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i] == 0 and pattern[j[-1] - 1, i + 1] == 1:
            pattern[j[-1], i] = 0
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i + 1] == pattern[j[-1] - 1, i] == 0:
            pattern[j[-1], i] = 0

    image.set_data(pattern)
    return image

def myrule1(frameNum, image, pattern, j):
    j.append(frameNum+1)
    if len(j) != len(set(j)):
        j[-1]+=1

    if j[-1] > len(pattern[0, :])-1:
        ani.FuncAnimation.pause(animation)

        return image

    for i in range(1,len(pattern)-1):
        if pattern[j[-1]-1,i+1] == pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i] == 1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1, i-1] == pattern[j[-1]-1,i] == 1 and pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==pattern[j[-1]-1,i+1]==1 and pattern[j[-1]-1,i]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==1 and pattern[j[-1]-1,i] == pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==0 and pattern[j[-1]-1,i+1]==pattern[j[-1]-1, i]==1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i+1]==0 and pattern[j[-1]-1,i]==1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i] == 0 and pattern[j[-1] - 1, i + 1] == 1:
            pattern[j[-1], i] = 0
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i + 1] == pattern[j[-1] - 1, i] == 0:
            pattern[j[-1], i] = 0

    image.set_data(pattern)
    return image

def myrule2(frameNum, image, pattern, j):
    j.append(frameNum+1)
    if len(j) != len(set(j)):
        j[-1]+=1

    if j[-1] > len(pattern[0, :])-1:
        ani.FuncAnimation.pause(animation)

        return image

    for i in range(1,len(pattern)-1):
        if pattern[j[-1]-1,i+1] == pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i] == 1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1, i-1] == pattern[j[-1]-1,i] == 1 and pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==pattern[j[-1]-1,i+1]==1 and pattern[j[-1]-1,i]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==1 and pattern[j[-1]-1,i] == pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==0 and pattern[j[-1]-1,i+1]==pattern[j[-1]-1, i]==1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i+1]==0 and pattern[j[-1]-1,i]==1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i] == 0 and pattern[j[-1] - 1, i + 1] == 1:
            pattern[j[-1], i] = 1
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i + 1] == pattern[j[-1] - 1, i] == 0:
            pattern[j[-1], i] = 0

    image.set_data(pattern)
    return image

def myrule3(frameNum, image, pattern, j):
    j.append(frameNum+1)
    if len(j) != len(set(j)):
        j[-1]+=1

    if j[-1] > len(pattern[0, :])-1:
        ani.FuncAnimation.pause(animation)

        return image

    for i in range(1,len(pattern)-1):
        if pattern[j[-1]-1,i+1] == pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i] == 1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1, i-1] == pattern[j[-1]-1,i] == 1 and pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==pattern[j[-1]-1,i+1]==1 and pattern[j[-1]-1,i]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==1 and pattern[j[-1]-1,i] == pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==0 and pattern[j[-1]-1,i+1]==pattern[j[-1]-1, i]==1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i+1]==0 and pattern[j[-1]-1,i]==1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i] == 0 and pattern[j[-1] - 1, i + 1] == 1:
            pattern[j[-1], i] = 1
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i + 1] == pattern[j[-1] - 1, i] == 0:
            pattern[j[-1], i] = 1

    image.set_data(pattern)
    return image

def myrule4(frameNum, image, pattern, j):
    j.append(frameNum+1)
    if len(j) != len(set(j)):
        j[-1]+=1

    if j[-1] > len(pattern[0, :])-1:
        ani.FuncAnimation.pause(animation)

        return image

    for i in range(1,len(pattern)-1):
        if pattern[j[-1]-1,i+1] == pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i] == 1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1, i-1] == pattern[j[-1]-1,i] == 1 and pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==pattern[j[-1]-1,i+1]==1 and pattern[j[-1]-1,i]==0:
            pattern[j[-1],i] = 0
        elif pattern[j[-1]-1,i-1]==1 and pattern[j[-1]-1,i] == pattern[j[-1]-1,i+1]==0:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1]==0 and pattern[j[-1]-1,i+1]==pattern[j[-1]-1, i]==1:
            pattern[j[-1],i] = 1
        elif pattern[j[-1]-1,i-1] == pattern[j[-1]-1,i+1]==0 and pattern[j[-1]-1,i]==1:
            pattern[j[-1],i] = 0
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i] == 0 and pattern[j[-1] - 1, i + 1] == 1:
            pattern[j[-1], i] = 0
        elif pattern[j[-1] - 1, i - 1] == pattern[j[-1] - 1, i + 1] == pattern[j[-1] - 1, i] == 0:
            pattern[j[-1], i] = 1

    image.set_data(pattern)
    return image

# program will save a gif to the local folder
if __name__=='__main__':
    N = 100
    pattern=np.zeros([N, N])
    #pattern[0,:] = np.random.randint(0, 2, size=N)
    pattern[0, round(N/2)]=1
    rule = input('Enter rule number [110, 90, 30, 184, myrule<1:4>]: ')
    global j
    j = []

    fig, ax = plt.subplots()
    image = ax.imshow(pattern, interpolation='nearest')

    if rule == '110':
        animation = ani.FuncAnimation(fig, rule110, fargs=(image, pattern, j), interval=100)
        animation.save('rule110.gif')
    elif rule == '90':
        animation = ani.FuncAnimation(fig, rule90, fargs=(image, pattern, j), interval=100)
        animation.save('rule90.gif')
    elif rule == '30':
        animation = ani.FuncAnimation(fig, rule30, fargs=(image, pattern, j), interval=100)
        animation.save('rule30.gif')
    elif rule == '184':
        animation = ani.FuncAnimation(fig, rule184, fargs=(image, pattern, j), interval=100)
        animation.save('rule184.gif')
    elif rule == 'myrule1':
        animation = ani.FuncAnimation(fig, myrule1, fargs=(image, pattern, j), interval=100)
        animation.save('myrule1.gif')
    elif rule == 'myrule2':
        animation = ani.FuncAnimation(fig, myrule2, fargs=(image, pattern, j), interval=100)
        animation.save('myrule2.gif')
    elif rule == 'myrule3':
        animation = ani.FuncAnimation(fig, myrule3, fargs=(image, pattern, j), interval=100)
        animation.save('myrule3.gif')
    elif rule == 'myrule4':
        animation = ani.FuncAnimation(fig, myrule4, fargs=(image, pattern, j), interval=100)
        animation.save('myrule4.gif')
    else:
        print('invalid rule please try again')
        os.system('/usr/local/bin/python3.9 /Users/antonrosenberg/Documents/GitHub/ComplexSystem/HomeWork1/1D_gameoflife.py')
    print('Simulation complete check gif out')
    #plt.show()