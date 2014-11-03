import sys, math
import heapq

# The code below will read all the game information for you.
# On each game turn, information will be available on the standard input, you will be sent:
# -> the total number of visible enemies
# -> for each enemy, its name and distance from you
# The system will wait for you to write an enemy name on the standard output.
# Once you have designated a target:
# -> the cannon will shoot
# -> the enemies will move
# -> new info will be available for you to read on the standard input.


class PQueue:
    def __init__(self):
        self.a = []
    
    def push(self, ele, pri):
        heapq.heappush(self.a, (pri, len(self.a), ele))
    
    def pop(self):
        heapq.heappop(self.a)
        
    def __iter__(self):
        while len(self.a) > 0:
            yield self.pop()
    
    def __len__(self):
        return len(self.a)
    
    

# game loop
while 1:
    count = int(raw_input()) # The number of current enemy ships within range
    enemies = PQueue()
    for i in xrange(count):
        # enemy: The name of this enemy
        # dist: The distance to your cannon of this enemy
        enemy, dist = raw_input().split()
        dist = int(dist)
        enemies.push(enemy, dist)
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    # The name of the most threatening enemy (HotDroid is just one example)
    for enemy in enemies:
        print enemy
