from tkinter import*
import numpy as np
from functools import partial
import matplotlib.pyplot as plt
import matplotlib.animation as ani


def createInputWin(N):

    def randRun(win, state):
        for i in range(N):
            for j in range(N):
               state[i,j] = np.random.randint(0, 2)
        win.destroy()

    def setVal(state, i, j):
        if state[i, j] == 0:
            state[i, j] = 1
        else:
            state[i, j] = 0
        plt.imshow(state)
        plt.show()

    def run(win):
        plt.close()
        win.destroy()

    win = Tk()
    win.geometry('800x400')
    state = np.zeros([N, N])
    for i in range(N):
        for j in range(N):
            buttons = Button(win, width=10, text="", command=partial(setVal, state, i, j), bg='purple')
            buttons.grid(row=i, column=j)


    runButton = Button(win, width=10, text='Run', command=partial(run, win), bg='green')
    runButton.grid(row=N+1, column=round(N/2))

    runButton = Button(win, width=10, text='Random', command=partial(randRun, win, state), bg='green')
    runButton.grid(row=N + 1, column=round(N / 2)-1)

    win.mainloop()
    return state