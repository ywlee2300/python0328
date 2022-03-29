#전역변수
str = "Not Class Member"
class GString:
    
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str)

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()
