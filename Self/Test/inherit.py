class Parent:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def output_p(self):
        print("名前:{} 身長:{} 体重:{}".format(self.name,self.height,self.weight))

class Child(Parent):
    def __init__(self,name,height,weight,bloodtype):
        super().__init__(name,height,weight)
        self.bloodtype=bloodtype
    def output_c(self):
        print("名前:{} 身長:{} 体重:{} 血液型:{}".format(self.name,self.height,self.weight,self.bloodtype))


p=Parent("AAA",170,70)
p.output_p()

c=Child("aaa",165,60,"A")
c.output_c()
