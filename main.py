import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from prisoner import Prisoner

if __name__ == '__main__':
    # Years in prison parameters
    T = 0
    R = 0.5
    P = 1
    S = 1.5

    # Game parameters
    N = 10
    n_list = [_ for _ in range(N+1)]
    m_list = [_ for _ in range(N+1)]

    years_prisoner1 = []
    years_matrix = np.zeros([len(n_list), len(m_list)])

    for m in m_list:
        for n in n_list:
            strategy1 = [1 for _ in range(N)]
            strategy2 = [1 for _ in range(N)]

            for i in range(n, N):
                strategy1[i] = -1

            for j in range(m, N):
                strategy2[j] = -1

            prisoner1 = Prisoner(strategy1)
            prisoner2 = Prisoner(strategy2)

            for k in range(N):
                if prisoner1.strategy[k] == prisoner2.strategy[k] == 1:
                    prisoner1.sentence(years=R)
                    prisoner2.sentence(years=R)
                    continue
                elif prisoner1.strategy[k]>prisoner2.strategy[k]:
                    prisoner2.sentence(years=T)
                    prisoner1.sentence(years=S)

                    prisoner1.change_strategy()
                    continue
                elif prisoner1.strategy[k]<prisoner2.strategy[k]:
                    prisoner1.sentence(years=T)
                    prisoner2.sentence(years=S)

                    prisoner2.change_strategy()
                    continue
                elif prisoner1.strategy[k] == prisoner2.strategy[k] == -1:
                    prisoner1.sentence(years=P)
                    prisoner2.sentence(years=P)

            #rgb = colors.colorConverter.to_rgb(str(prisoner1.years/15))
            #plt.plot(n, m, 'o', color=rgb)

            years_prisoner1.append(prisoner1.years)
            years_matrix[n, m] = prisoner1.years



    N, M = np.meshgrid(n_list, m_list)
    #plt.plot(n_list, m_list, ec='k')
    plt.contourf(N,M,years_matrix)
    plt.colorbar()
    plt.ylabel('n')
    plt.xlabel('m')
    plt.plot([1,10], [0, 9], 'black')
    plt.legend('n=m-1')
    plt.show()
    #print(f'Prisoner 1 has served {prisoner1.years} years, prisoner 2 has served {prisoner2.years} years')



