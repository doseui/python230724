str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str) # self를 누락하면 글로벌 변수값을 프린트 한다.(버그 조심)

g = GString()
g.set("First Message")
g.print()
