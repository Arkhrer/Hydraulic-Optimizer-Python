from pymoo.core.problem import Problem
from typing import final
from epyt import epanet

NUMBEROFPIPES: final = 8

class TesteProb(Problem):
    def __init__(self):
        self.Xmin = []
        self.Xmax = []
        self.NumberOfVariables = NUMBEROFPIPES

        for i in range(self.NumberOfVariables):
            self.Xmin.append(0)
            self.Xmax.append(13)

        super().__init__(n_var = self.NumberOfVariables, n_obj = 2, x1 = self.Xmin, xu= self.Xmax, vtype = float)

    def __evaluate(self, x, out, *args, **kwargs):
        pass

Problem = TesteProb()