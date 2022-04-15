class favanimal():
    def __init__(self, arms,legs,eyes,tail,furry):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry
    def printattributes(self):
        print("My arms are %s inches long."%(self.arms))
        print("My legs are %s inches long"%(self.legs))
        print("I have %s eyes"%(self.eyes))
        if self.tail:
            print("I have a tail")
        else:
            print("I dont' have a tail")
        if self.furry:
            print("I am furry")
        else:
            print("I amd not furry")
        
Holly = favanimal(12.0,12.0,2,True,True)
favanimal.printattributes(Holly)