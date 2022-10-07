import numpy as np
import pprint
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import time
from tqdm import trange

'''
def mutate(mu, gameBoard, L,N):
    mutated = np.zeros([L,L])
    for i in range(L):
        for j in range(L):
            r = np.random.rand()
            if r < mu:
                if gameBoard[i][j] == N:
                    gameBoard[i][j] = 0
                    mutated[i][j]=1
                elif gameBoard[i][j] == 0:
                    gameBoard[i][j] = N
                    mutated[i][j]=1
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


def calc_score(gameBoard, neighbours, score,L ,N, T, R, P, S):

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

                if prisoner1>prisoner2:
                    score[i][j] += prisoner2*R+S+(N-prisoner2-1)*P
                elif prisoner1 == prisoner2:
                    score[i][j] += prisoner1*R+(N-prisoner1)*P
                elif prisoner1<prisoner2:
                    score[i][j] += prisoner1*R+T+(N-prisoner1-1)*P

    return score

if __name__ == '__main__':
    L = 50
    N = 7
    T = 0
    R_list = np.linspace(0.5,0.9,25)
    P = 1
    S_list = np.linspace(0.8,2.5,25)
    numRounds = 500
    mu = 0.01
    sigma_sum=np.zeros([len(R_list), len(S_list)])


    for ind2 in trange(len(S_list)):
        for ind1 in trange(len(R_list)):
            sigma = np.zeros(N+1)
            numOfn = np.zeros([numRounds,N + 1])
            R=R_list[ind1]
            S=S_list[ind2]
            gameBoard = [[N for j in range(L)] for i in range(L)]

            for i in range(L):
                for j in range(L):
                    strategy1 = [1 for _ in range(N)]
                    n=np.random.randint(0, N+1)
                    for k in range(n, N):
                        strategy1[k] = -1
                    gameBoard[i][j] = strategy1.count(1)

            '''
            for i in range(L):
                for j in range(L):
                    r=np.random.rand()
                    if r>=0.5:
                        gameBoard[i][j] = 0
            '''
            '''
            numDefectors=10
            for _ in range(numDefectors):
                for t in range(numDefectors):
        
                    gameBoard[round(_)][round(t)]=10
            print(gameBoard.count(0))
            '''


            neighbours = [[0,1], [0,-1], [-1,0], [1,0]]

            for _ in range(numRounds):
                gameBoard, mutated = mutate(mu, gameBoard, L, N)
                if _ > 100:

                    for num in range(N + 1):
                        for arr in gameBoard:
                            numOfn[_,num]+=arr.count(num)

                score = [[0 for j in range(L)] for i in range(L)]

                score = calc_score(gameBoard, neighbours, score, L, N, T, R, P, S)
                #print(mutated)
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
            for i in range(N+1):
                sigma[i] = np.var(numOfn[:,i])

            sigma_sum[ind1,ind2] = np.sum(sigma)
            '''
            plt.imshow(gameBoard)
            plt.colorbar()
            plt.title(f'R = {R}, S = {S}')
            #plt.savefig(f'R = {R}, all strategies allowed.png')
            plt.close('all')
            '''
    plt.contourf(R_list, S_list, sigma_sum)
    plt.colorbar()
    plt.title('Countour')
    plt.xlabel('R')
    plt.ylabel('S')
    plt.savefig(f'Contour.png')






