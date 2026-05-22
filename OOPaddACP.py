class Addition:
    def __init__(self,num1,num2,num3):
        self.num1= num1
        self.num2 = num2
        self.num3 = num3

    def addnum(self):
        total = self.num1+self.num2+self.num3
        print("The sum is",total)

obj = Addition(134,29,60)
obj.addnum()