class Coffee:

    def __init__(self, brand, d, c):
        self.__brand = brand #coffee name
        self.__d = d #demand
        self.__c = c #unit cost
        self.__h = self.__c/3 #holding cost
        self.__k = 10 #order cost

    def getBrand(self): #allows access to private field: brand
        return self.__brand
    
    def getDemand(self):
        return self.__d    

    def Q(self):
        return ((2*self.__k*self.__d)/self.__h)**(1/2)

    def TAC(self):
        return (self.Q()*self.__h/2)+(self.__d*self.__k/self.Q())+(self.__d*self.__c)

    def T(self):
        return (self.Q()/self.__d)*52
    
    def totalQ(inputList):
        """ Returns the total balance for a list of objects"""
        sum = 0
        for i in inputList:
            sum += (((2*i.__k*self.__d)/i.__h)**(1/2)) # Since dunder __ makes 
        return sum   

    def __str__(self): #return values of name, unit cost, demand, Q, TAC, T
        message = '{0:15} {1:<15.2f} {2:<15.0f} {3:<15.0f} {4:<15.2f} {5:<15.2f}'.format(self.__brand, self.__c, self.__d, self.Q(), self.TAC(), self.T())
        return message
        #creates a string representation of coffee object
        
 
