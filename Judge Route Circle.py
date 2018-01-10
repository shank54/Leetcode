class Solution:
    def judgeCircle(self, moves):
        x = 0
        y = 0
        for i in range(len(moves)):
            if moves[i]=="U":
                x += 9
            elif moves[i]=="D":
                x += -9
            elif moves[i]=="L":
                y += 8
            elif moves[i]=="R":
                y += -8
        return x==y==0