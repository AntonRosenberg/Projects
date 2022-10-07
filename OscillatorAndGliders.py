import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from collections import Counter
from main import calcNeighbours
from datetime import datetime
import sys


def translate(transState, x, y):
    transState = np.copy(np.roll(transState, x, axis=1))
    transState = np.copy(np.roll(transState, y, axis=0))
    return transState


def checkConfig(state1, state2):
    if (state1 == state2).all():
        return state1
    return []

'''
def checkConfig(states):
    for i in range(len(states)):
        config = states[i]
        dupliCheck = states[:i-1]+states[i+1:]
        if config in dupliCheck:
            return config
    return []
'''

def udateState(state, states, N, choice):

    numOfNeighbours = calcNeighbours(state, N)
    for i in range(N):
        for j in range(N):
            if state[i][j] == 0 and numOfNeighbours[i, j] == 3:
                state[i][j] = 1
            else:
                if numOfNeighbours[i][j] < 2 or numOfNeighbours[i][j] > 3:
                    state[i][j] = 0

    states.append(state)

    # OSCILLATORS
    if choice == 'osc':
        for i in range(len(states)):
            for j in range(len(states)):
                if j!=i:
                    oscillators = checkConfig(states[i], states[j])
                    if len(oscillators)>0:
                        np.savetxt('Oscillator '+str(datetime.now().strftime("%H %M %S")), oscillators)
                        return True

    # SPACESHIPS
    if choice == 'space':
        transStates = []
        directions = [[1,1], [1, 0], [0,1],[-1,-1],[-1,0],[0,-1],[1,-1],[-1,1]]
        for i in range(len(states)):
            for j in range(8):
                transStates.append(translate(states[i], directions[j][0], directions[j][1]))

        for i in range(len(states)):
            for j in range(len(transStates)):
                    spaceships = checkConfig(transStates[j],states[i])
                    if len(spaceships)>0 and np.count_nonzero(spaceships)>0:
                        np.savetxt('Spaceship ' + str(datetime.now().strftime("%H %M %S")), spaceships)
                        return True

    return False


if __name__ == '__main__':
    N = 10
    for j in range(5):
        states=[]
        #state = np.random.randint(0, 2, [N,N])
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
        state = np.pad(state, N)
        states = [state]
        for i in range(20):
            bol = udateState(state, states, 3*N, 'space')
            if bol==True:
                break