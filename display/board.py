import numpy as np
import sys
import time
import os

class LifeGame:
    def __init__(self, L=15, p=0.2):
        self.L = L
        self.survive = [2, 3]
        self.birth = [3]
        element_list = [1, 0]
        prob_list = [p, 1-p]
        #ランダム
        #self.lattice = np.random.choice(a=element_list, size=(self.L+2)**2, p=prob_list).reshape(self.L+2, -1)
        #グライダー
        self.lattice = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ])
        #銀河
        '''self.lattice = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ])'''
        self.lattice[0, :] = self.lattice[self.L+1, :] = 0
        self.lattice[:, 0] = self.lattice[:, self.L+1] = 0

    def canvas_update(self):
        os.system("cls")
        print("\n")
        l = ""
        for y in range(1, self.L+1):
            for x in range(1, self.L+1):
                if self.lattice[x, y]:
                    l += " ■"
                else:
                    l += " □"
            l += "\n"
        print(l)
        print("\n")
        time.sleep(1)

    def progress(self):
        L = self.L
        T_max = 10
        t = 0
        while t < T_max:
            try:
                self.canvas_update()
                
                self.lattice[0, 0] = self.lattice[self.L, self.L]
                self.lattice[0, self.L+1] = self.lattice[self.L, 1]
                self.lattice[self.L+1, 0] = self.lattice[1, self.L]
                self.lattice[self.L+1, self.L+1] = self.lattice[1, 1]
                for m in range(1, self.L+1):
                    self.lattice[0, m] = self.lattice[self.L, m]
                    self.lattice[m, 0] = self.lattice[m, self.L]
                    self.lattice[m, self.L+1] = self.lattice[m, 1]
                    self.lattice[self.L+1, m] = self.lattice[1, m]
                    
                nextsites = []
                for i in range(1, self.L+1):
                    for j in range(1, self.L+1):
                        neighbor = np.sum(self.lattice[i-1:i+2, j-1:j+2]) - self.lattice[i, j]
                        if self.lattice[i, j]:
                            if neighbor in self.survive:
                                nextsites.append((i, j))
                        else:
                            if neighbor in self.birth:
                                nextsites.append((i, j))
                    
                self.lattice[:] = 0
                for nextsite in nextsites:
                    self.lattice[nextsite] = 1
                #print(nextsites)
                t += 1
            
            except KeyboardInterrupt:
                print("stopped.")
                break

if __name__ == "__main__":
    LifeGame().progress()