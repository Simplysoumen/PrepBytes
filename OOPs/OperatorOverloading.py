class Student:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        ans1 = self.x + other.x
        ans2 = self.y + other.y
        return '{} {}'.format(ans1,ans2)

    def __lt__(self, other):
        ans1 = self.x + other.y
        ans2 = self.x + other.y
        if(ans1<ans2):
            return True
        else:
            return False

s1 = Student(10,20)
s2 = Student(500,6)
if(s1<s2):
    print("s1 is smaller")
else:
    print("s2 is smaller")
