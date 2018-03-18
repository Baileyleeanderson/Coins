
count_head = 0
count_tail = 0
attempt = 0
import random
for x in range(5000):
    g = random.randint(0,1)
    attempt = attempt +1
    if g == 0:
        count_head += 1
        print"Attempt #",attempt,"Throwing a coin...Its a head!...Got",count_head,"so far and",count_tail,"tail(s)so far."
    elif g == 1:
        count_tail += 1
        print"Attempt #",attempt,"Throwing a coin...Its a head!...Got",count_head,"so far and",count_tail,"tail(s)so far."
if attempt == 5000:
    print"Attempt #",attempt,"Thowing a coin...Its a head!...Got",count_head,"so far and",count_tail,"tail(s)so far. Ending the program, thank you!"