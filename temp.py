# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import matplotlib.pyplot as bar_graph

#setting width and location of bar
#y will show the number of times heads came up

head_count = 0
double_head_count = 0
triple_head_count = 0
tails_count = 0


flipHistory = [None] * 1000

#coinFlip = random.uniform(0,1)
# anything below .40, including .40 is heads
# anything above .40 is tails

biasedCoin = {"Heads": .40, "Tails": .60}

heads = biasedCoin.get("Heads")

for x in range(1000):
    flipHistory[x] = random.uniform(0,1)
    if flipHistory[x] <= heads:
        head_count = head_count + 1
        #print("H")
        if x > 0 and flipHistory[x-1] <= heads:
            double_head_count = double_head_count + 1
            if x > 1 and flipHistory[x-2] <= heads:
                triple_head_count = triple_head_count + 1
    else:
       tails_count = tails_count + 1
       #print("T")
        #do nothing


#print("heads: ", head_count)
#print("tails: ", tails_count)

xOne = [.5]
yOne = [head_count]

xTwo = [1.5]
yTwo = [double_head_count]

xThree = [2.5]
yThree = [triple_head_count]

#x = [3.5]
#y = [tails_count]

bar_graph.bar(xOne, yOne, label = "HEADS", color = 'brown')
bar_graph.bar(xTwo, yTwo, label = "DOUBLE HEADS", color = 'silver')
bar_graph.bar(xThree, yThree, label = "TRIPLE HEADS", color = 'gold')
#bar_graph.bar(x, y, label = "TAILS", color = 'magenta')

#TODO: change 10 to total coint flips
bar_graph.axis([0, 3, 0, 1000])
bar_graph.ylabel('Number of Occurences')
bar_graph.title('Results of 1000 Coin Flips')
bar_graph.legend()
bar_graph.show()



