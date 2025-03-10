from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("I can walk and run")

class snake(animal):
     def move(self):
        print("I can crawl")

class dog(animal):
     def move(self):
        print("I can walk")

class rabbit(animal):
     def move(self):
        print("I can hop")

h=human()
h.move()
s=snake()
s.move()
d=dog()
d.move()
r=rabbit()
r.move()


    