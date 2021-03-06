#encoding=utf-8

'''
工厂模式、抽象工厂模式的优点：
1、工厂模式巨有非常好的封装性，代码结构清晰；在抽象工厂模式中，其结构还可以随着需要进行更深或者更浅的抽象层级调整，非常灵活；
2、屏蔽产品类，使产品的被使用业务场景和产品的功能细节可以分而开发进行，是比较典型的解耦框架。
工厂模式、抽象工厂模式的使用场景：
1、当系统实例要求比较灵活和可扩展时，可以考虑工厂模式或者抽象工厂模式实现。比如，
在通信系统中，高层通信协议会很多样化，同时，上层协议依赖于下层协议，那么就可以对应建立对应层级的抽象工厂，根据不同的“产品需求”去生产定制的实例。
'''

class Burger():
    name=""
    price=0.0
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class cheeseBurger(Burger):
    def __init__(self):
        self.name="cheese burger"
        self.price=10.0
class spicyChickenBurger(Burger):
    def __init__(self):
        self.name="spicy chicken burger"
        self.price=15.0

class Snack():
    name = ""
    price = 0.0
    type = "SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0

class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

class foodFactory():
    type=""
    def createFood(self,foodClass):
        print self.type," factory produce a instance."
        foodIns=foodClass()
        return foodIns
class burgerFactory(foodFactory):
    def __init__(self):
        self.type="BURGER"
class snackFactory(foodFactory):
    def __init__(self):
        self.type="SNACK"
class beverageFactory(foodFactory):
    def __init__(self):
        self.type="BEVERAGE"

if  __name__=="__main__":
    burger_factory=burgerFactory()
    snack_factorry=snackFactory()
    beverage_factory=beverageFactory()
    cheese_burger=burger_factory.createFood(cheeseBurger)
    print cheese_burger.getName(),cheese_burger.getPrice()
    chicken_wings=snack_factorry.createFood(chickenWings)
    print chicken_wings.getName(),chicken_wings.getPrice()
    coke_drink=beverage_factory.createFood(coke)
    print coke_drink.getName(),coke_drink.getPrice()



















