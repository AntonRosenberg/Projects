import numpy as np
from OscillatorAndGliders import translate
'''
state=[[0, 0 , 1],[1, 0 , 0],[0,0 ,1 ]]
state=np.array(state)
index = np.where(state == 1)
print(index)
'''
state = [
    [0, 1, 2],
    [2, 3, 4]
]
print(translate(state, -1, 0))
