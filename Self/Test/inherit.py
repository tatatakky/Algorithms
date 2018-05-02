class Parent:
    def __init__(self,name,height,weight): #コンストラクタ
        self.name=name
        self.height=height
        self.weight=weight
    def output_p(self):
        print("<{}さんの情報>".format(self.name))
        print("名前:{} 身長:{} 体重:{}".format(self.name,self.height,self.weight))

class Child(Parent):
    def __init__(self,name,height,weight,bloodtype): #コンストラクタ
        super().__init__(name,height,weight) #スーパーコンストラクタの呼び出し
        self.bloodtype=bloodtype
    def output_c(self):
        super().output_p()
        print("血液型:{}".format(self.bloodtype))

if __name__=="__main__":

    p=Parent("AAA",170,70) #インスタンスを生成する
    p.output_p()

    c=Child("aaa",165,60,"A") #インスタンスを生成する
    c.output_c()
