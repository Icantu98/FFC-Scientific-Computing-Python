import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        if(len(kwargs)==0):
            print("at least one argument needed")
            quit()

        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, num):
        s = []
        if(num>len(self.contents)):
            return self.contents
        # random list of indices  
        tl = random.sample(range(len(self.contents)), k=num)
        for i in tl:
            s.append(self.contents[i]) # s: list based on indices
        tmp = [self.contents[i] for i in range(len(self.contents)) if not i in tl]
        self.contents=tmp # contents without tl
        return s


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []
    print(expected_balls)
    for k,v in expected_balls.items():
        for i in range(v):
            expected.append(k)

    hit = 0
    for ne in range(num_experiments):
        ch = copy.deepcopy(hat)
        drawn = ch.draw(num_balls_drawn)

        chk = False
        for e in expected:
            if e in drawn:
                chk=True
                drawn.remove(e)
            else:
                chk = False
                break # failes if something isnt in Num_balls
      
        if chk:
            hit += 1
  
    return hit/ num_experiments

