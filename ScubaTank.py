class ScubaTank:
    def __init__(self,label,bar):
        self.label = label
        self.__bar = bar
    def get_bar(self):
        return self.__bar
    def set_bar(self,bar):
        if bar >= 0 and bar <= 300:
            self.__bar = bar
        else:
            print("Invalid pressure.")
    def fill(self,amount):
        if amount > 0 :
            self.__bar += amount
        else:
            print("Invalid amount.")
    def release(self,amount):
        if amount <= 0 :
            print("Invalid amount.")
        elif amount > self.__bar:
            print("Not enough air.")
        else:
            self.__bar -= amount 
    def __str__(self):
        return f"Tank {self.label}: {self.__bar} bar"
def transfer_air(source, target, amount):
    old_bar = source.get_bar()
    source.release(amount)

    if old_bar - source.get_bar() == amount:
        target.fill(amount)
t = ScubaTank("A", 80)
print(t)
t.fill(40)
print(t.get_bar())
t.set_bar(250)
print(t)
t.set_bar(400)
print(t.get_bar())
t.release(0)
t.release(300)
t.release(50)
print(t)





        
