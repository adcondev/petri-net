import numpy as np
class MatrixPetriNet:
    __slots__ = ("_mo","_pre","_post","_mk","_last_mk","_enabled")
    def __init__(self,
        M_o = np.array([
                        [2],
                        [0],
                        [0],
                        [0],
                        [0]
                        ]),
        Pre = np.array([
                        [2,0,0,0,0],
                        [0,1,0,0,0],
                        [0,0,1,0,0],
                        [0,0,0,1,0],
                        [0,0,0,0,1]
                        ]),
        Post = np.array([
                        [0,0,0,1,1],
                        [1,0,0,0,0],
                        [1,0,0,0,0],
                        [0,1,0,0,0],
                        [0,0,1,0,0]
                        ])):
        self._mo = self._mk = M_o
        self._pre, self._post = Pre, Post
    def M_o(self):
        return self._mo.transpose()[0]
    def Pre(self):
        return self._pre.transpose()
    def Post(self):
        return self._post.transpose()
    def M_k(self):
        return self._mk.transpose()[0]
    def Firing(self):
        while True:
            IsBlocked = True
            print("\nMarcado actual: ", self.M_k())
            for t_i in self.Enabled():
                IsBlocked = False
                print("Transición " + str(t_i) + " habilitada.")
            if IsBlocked:
                print("Red bloqueada...")
                break
            To_Fire = input("Selección: ")
            if To_Fire == "exit":
                break
            self._mk.transpose()[0] = self.M_k() - self.Pre()[int(To_Fire)] + self.Post()[int(To_Fire)]
    def Enabled(self):
            return (i for i,pre in enumerate(self.Pre()) if all(self.M_k() >= pre))
PetNet = MatrixPetriNet().Firing()
