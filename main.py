import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from GUI import createInputWin

from scipy import signal
import time

def calcNeighbours(state, N):
    index = np.where(state == 1)
    index = np.array(index)
    index[0]=index[0]+1
    index[1]=index[1]+1
    neighbours = np.zeros([N+2, N+2])
    for i in range(len(index[0])):
        neighbours[index[0,i]+1,index[1,i]+1] += 1
        neighbours[index[0,i]+1,index[1,i]] += 1
        neighbours[index[0,i]+1,index[1,i]-1] += 1

        neighbours[index[0,i]-1,index[1,i]-1] += 1
        neighbours[index[0,i]-1,index[1,i]+1] += 1
        neighbours[index[0,i]-1,index[1,i]] += 1

        neighbours[index[0,i],index[1,i]+1] += 1
        neighbours[index[0,i],index[1,i]-1] += 1

    numOfNeighbours = np.copy(neighbours[1:-1,1:-1])

    # PERIODIC BOUNDARY #####################################################

    lastRow = neighbours[-1][1:-1]
    firstRow = neighbours[0][1:-1]
    lastColumn = neighbours[1:-1, N+2 - 1]
    firstColumn = neighbours[1:-1, 0]
    numOfNeighbours[0, :] = np.copy(numOfNeighbours[0, :] + lastRow)
    numOfNeighbours[N - 1, :] = np.copy(numOfNeighbours[N - 1, :] + firstRow)
    numOfNeighbours[:, 0] = np.copy(numOfNeighbours[:, 0] + lastColumn)
    numOfNeighbours[:, N - 1] = np.copy(numOfNeighbours[:, N - 1] + firstColumn)
    numOfNeighbours[-1,-1] = np.copy(numOfNeighbours[-1,-1]+ neighbours[0,0])
    numOfNeighbours[-1, 0] = np.copy(numOfNeighbours[-1, 0] + neighbours[0, -1])
    numOfNeighbours[0, 0] = np.copy(numOfNeighbours[0, 0] + neighbours[-1, -1])
    numOfNeighbours[0, -1] = np.copy(numOfNeighbours[0, -1] + neighbours[-1, 0])

    ##########################################################################
    return numOfNeighbours

def udateState(frameNum, image, state, N):
    '''
    numOfNeighbours = signal.convolve2d(state, np.ones((3, 3)), mode='same') #TODO doesnt work well
    numOfNeighbours[0,:] = numOfNeighbours[0,:] + state[N-1,:]
    numOfNeighbours[N-1, :] = numOfNeighbours[N-1,:] + state[0,:]
    numOfNeighbours[:,0] = numOfNeighbours[:,0] + state[:,N-1]
    numOfNeighbours[:, N-1] = numOfNeighbours[:, N-1] + state[:, 0]
    '''
    numOfNeighbours = calcNeighbours(state, N)
    for i in range(N):
        for j in range(N):
            if state[i][j] == 0 and numOfNeighbours[i, j] == 3:
                state[i][j] = 1
            else:
                if numOfNeighbours[i][j] < 2 or numOfNeighbours[i][j] > 3:
                    state[i][j] = 0

    image.set_data(state)
    return image

def udateStateMyway(frameNum, image, state, N):
    numOfNeighbours = calcNeighbours(state, N)
    for i in range(N):
        for j in range(N):
            if state[i][j] == 0 and numOfNeighbours[i, j] >= 4:
                state[i][j] = 1
            else:
                if numOfNeighbours[i][j] < 5:
                    state[i][j] = 0

    image.set_data(state)
    return image

def udateStateMyway2(frameNum, image, state, N):
    numOfNeighbours = calcNeighbours(state, N)
    for i in range(N):
        for j in range(N):
            if state[i][j] == 0 and numOfNeighbours[i, j] > 5:
                state[i][j] = 1
            else:
                if numOfNeighbours[i][j] < 4:
                    state[i][j] = 0

    image.set_data(state)
    return image

def udateStateMyway3(frameNum, image, state, N):
    numOfNeighbours = calcNeighbours(state, N)
    for i in range(N):
        for j in range(N):
            r = np.random.randint(8)
            if state[i][j] == 0 and numOfNeighbours[i, j] > r:
                state[i][j] = 1
            else:
                if numOfNeighbours[i][j] < r-4 or numOfNeighbours[i][j] > r+4:
                    state[i][j] = 0

    image.set_data(state)
    return image


def udateVote(frameNum, image, state, N):

    numOfNeighbours = calcNeighbours(state, N)
    for i in range(N):
        for j in range(N):
            if numOfNeighbours[i, j] < 4:
                state[i][j] = 0
            elif numOfNeighbours[i, j] > 5:
                state[i][j] = 1

    image.set_data(state)
    return image

def initiateVote(N, probability):
    state = np.zeros([N,N])
    for i in range(N):
        for j in range(N):
            r = np.random.rand()
            if r <= probability:
                state[i, j] = 1
            else:
                state[i, j] = 0
    return state

if __name__ == '__main__':
    N = 10
    p = 0.5
    state = createInputWin(N)
    #state = initiateVote(N, probability=p)
    #state = np.random.randint(0, 2, [N,N])
    #Tkinker doesn't work on mac so you need to manually use the matrix below for initiating a certain pattern
    '''
    state = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ]
    '''
    #state = np.array(state)

    #state=np.loadtxt('Spaceship 00 38 06')
    fig, ax = plt.subplots()
    image = ax.imshow(state, interpolation='nearest')
    animation = ani.FuncAnimation(fig, udateState, fargs=(image, state, N), interval=50)
    '''
    animation = ani.FuncAnimation(fig, udateVote, fargs=(image, state, N), frames=25, interval=100)
    animation = ani.FuncAnimation(fig, udateStateMyway, fargs=(image, state, N),frames=50, interval=100)
    animation = ani.FuncAnimation(fig, udateStateMyway2, fargs=(image, state, N), frames=50, interval=100)
    animation = ani.FuncAnimation(fig, udateStateMyway3, fargs=(image, state, N), frames=50, interval=100)
    '''
    
    #animation.save('SavedGIF.gif')
    plt.show()

