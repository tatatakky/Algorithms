class Addition:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def mix(self):
        su = self.x+self.y
        print("{}+{}={}".format(self.x,self.y,su))
add=Addition(3,27)
add.mix()
