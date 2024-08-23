import numpy as np

def apply(cube,move):
    #TODO : ajouter la ROTATIONde la face droite
    #puis : créer x, y , z (attention aux rotations)
    if move not in ["R","R'"] :
        raise ValueError("Move '"+str(move)+"' unknown.")
    if move == "R":
        tmp = cube.up.cells[:,2].copy()
        cube.up.cells[:,2] = cube.front.cells[:,2]
        cube.front.cells[:,2] = cube.down.cells[:,2]
        cube.down.cells[:,2] = cube.back.cells[:,0]
        cube.back.cells[:,0] = tmp
        return cube
    if move == "R'":
        tmp = cube.up.cells[:,2].copy()
        cube.up.cells[:,2] = cube.back.cells[:,0]
        cube.back.cells[:,0] = cube.down.cells[:,2]
        cube.down.cells[:,2] = cube.front.cells[:,2]
        cube.front.cells[:,2] = tmp 
        return cube

class Face:
    def __init__(self):
        self.cells = [[None for i in range(0,3)] for j in range(0,3)]

    def __init__(self,color):
        if color not in "WOGRBY":
            raise ValueError("Argument is not a color : " + str(color))
        self.cells = np.array([[color for i in range(0,3)] for j in range(0,3)])

    def __str__(self):
        formatted_str = ""
        for i in range(0,3):
            for j in range(0,3):
                formatted_str = formatted_str + self.cells[i,j]
            formatted_str = formatted_str + "\n" 
        return formatted_str

class Cube:
    def __init__(self):
        self.down = Face("W")
        self.front = Face("O")
        self.left = Face("G")
        self.back = Face("R")
        self.right = Face("B")
        self.up = Face("Y") 

    def __str__(self):
        #PRINT UP
        res = ""
        for i in range(0,3):
            res = res + "    "
            for j in range(0,3):
                res = res + str(self.up.cells[i,j])
            res += "\n"
        #PRINT MID
        for i in range(0,3):
            for j in range(0,3):
                res = res + str(self.left.cells[i,j])
            res += " " 
            for j in range(0,3):
                res = res + str(self.front.cells[i,j])
            res += " " 
            for j in range(0,3):
                res = res + str(self.right.cells[i,j])
            res += " " 
            for j in range(0,3):
                res = res + str(self.back.cells[i,j])
            res += "\n"
        #PRINT DOWN
        for i in range(0,3):
            res = res + "    "
            for j in range(0,3):
                res = res + str(self.down.cells[i,j])
            res += "\n"
        return res
