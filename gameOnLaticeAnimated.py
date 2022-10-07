import numpy as np
import pprint
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import time
from tqdm import trange

'''
def mutate(mu, gameBoard, L, N):
    mutated = np.zeros([L, L])
    for i in range(L):
        for j in range(L):
            r = np.random.rand()
            if r < mu:
                if gameBoard[i][j] == N:
                    gameBoard[i][j] = 0
                    mutated[i][j] = 1
                elif gameBoard[i][j] == 0:
                    gameBoard[i][j] = N
                    mutated[i][j] = 1
    return gameBoard, mutated
'''
def mutate(mu, gameBoard, L,N):
    mutated = np.zeros([L,L])
    for i in range(L):
        for j in range(L):
            r = np.random.rand()
            if r < mu:
                gameBoard[i][j] = np.random.randint(0, N+1)
                mutated[i][j] = 1
    return gameBoard, mutated

def calc_score(gameBoard, neighbours, score, L, N, T, R, P, S):
    for i in range(L):
        for j in range(L):
            for neighbour in neighbours:
                prisoner1 = gameBoard[i][j]
                if i + neighbour[0] < L:
                    pos1Neighbour = i + neighbour[0]
                else:
                    pos1Neighbour = 0

                if j + neighbour[1] < L:
                    pos2Neighbour = j + neighbour[1]
                else:
                    pos2Neighbour = 0

                prisoner2 = gameBoard[int(pos1Neighbour)][int(pos2Neighbour)]

                if prisoner1 > prisoner2:
                    score[i][j] += prisoner2 * R + S + (N - prisoner2 - 1) * P
                elif prisoner1 == prisoner2:
                    score[i][j] += prisoner1 * R + (N - prisoner1) * P
                elif prisoner1 < prisoner2:
                    score[i][j] += prisoner1 * R + T + (N - prisoner1 - 1) * P

    return score

def update_game_board(frameNum,image,  gameBoard, R):
    gameBoard, mutated = mutate(mu, gameBoard, L, N)

    score = [[0 for j in range(L)] for i in range(L)]

    score = calc_score(gameBoard, neighbours, score, L, N, T, R, P, S)
    # print(mutated)
    for i in range(L):
        for j in range(L):
            if mutated[i][j] == 1:
                continue
            scoreIndividual = score[i][j]

            for neighbour in neighbours:
                if i + neighbour[0] < L:
                    pos1Neighbour = i + neighbour[0]
                else:
                    pos1Neighbour = 0

                if j + neighbour[1] < L:
                    pos2Neighbour = j + neighbour[1]

                else:
                    pos2Neighbour = 0

                scoreNeighbour = score[int(pos1Neighbour)][int(pos2Neighbour)]

                if scoreNeighbour < scoreIndividual:
                    scoreIndividual = scoreNeighbour
                    gameBoard[i][j] = gameBoard[int(pos1Neighbour)][int(pos2Neighbour)]
                elif scoreNeighbour == scoreIndividual:
                    r = np.random.rand()
                    if r >= 0.5:
                        gameBoard[i][j] = gameBoard[int(pos1Neighbour)][int(pos2Neighbour)]
    plt.title(f'R = {R}, S = {S}, t = {frameNum}')
    image.set_data(gameBoard)
    return image

if __name__ == '__main__':

    L = 50
    N = 7
    T = 0
    R_list = np.linspace(0.4, 0.9, 12)
    P = 1
    S = 1.5
    numRounds = 100
    mu = 0.01

    for R in R_list:
        # gameBoard = [[[0 for k in range(N)] for j in range(L)] for i in range(L)]
        gameBoard = [[N for j in range(L)] for i in range(L)]

        for i in range(L):
            for j in range(L):
                strategy1 = [1 for _ in range(N)]
                n = np.random.randint(0, N+1)
                for k in range(n, N):
                    strategy1[k] = -1
                gameBoard[i][j] = strategy1.count(1)

        neighbours = [[0, 1], [0, -1], [-1, 0], [1, 0]]


        fig, ax = plt.subplots()
        image = ax.imshow(gameBoard)
        fig.colorbar(image)
        animation = ani.FuncAnimation(fig, update_game_board, fargs=(image, gameBoard, R), frames=200, interval=150)
        animation.save(f'R={R}.gif')
        plt.close('all')
