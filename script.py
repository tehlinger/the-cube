class Face:
    def __init__(self):
        self.cells = [None for i in range(0,9)]

    def __init__(self,color):
        if color not in "WOGRBY":
            raise ValueError("Argument is not a color : " + str(color))
        self.cells = [color for i in range(0,9)]

    def __str__(self):
        formatted_str = ""
        for i in range(0,3):
            for j in range(0,3):
                formatted_str = formatted_str + self.cells[i*3+j]
            formatted_str = formatted_str + "\n" 
        return formatted_str

        return ''.join(self.cells)

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
                res = res + str(self.up.cells[3*i+j])
            res += "\n"
        #PRINT MID
        for i in range(0,3):
            for j in range(0,3):
                res = res + str(self.left.cells[3*i+j])
            res += " " 
            for j in range(0,3):
                res = res + str(self.front.cells[3*i+j])
            res += " " 
            for j in range(0,3):
                res = res + str(self.right.cells[3*i+j])
            res += " " 
            for j in range(0,3):
                res = res + str(self.back.cells[3*i+j])
            res += "\n"
        #PRINT DOWN
        for i in range(0,3):
            res = res + "    "
            for j in range(0,3):
                res = res + str(self.down.cells[3*i+j])
            res += "\n"
        return res
