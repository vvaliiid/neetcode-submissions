class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c= 0 
        point = k
        while len(tickets) >=1 :
            if point == 0 and tickets[point] == 1:
                return c+1
            if point == 0 and tickets[point]>1:
                tickets[0]-=1
                c+=1
                point = len(tickets) -1
                aaa = tickets.pop(0)
                tickets.append(aaa)
            elif tickets[0]==1:
                tickets.pop(0)
                point -=1
                c+=1
            if tickets[0]>1 and point!=0:
                tickets[0]-=1
                point -= 1
                petit = tickets.pop(0)
                tickets.append(petit)
                c+=1
        return c



        