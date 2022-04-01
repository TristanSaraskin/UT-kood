from minimax import minimax
import time

a = [
    [[0, 0, 0],0,[0, 2, 0],0,0,0,[0, 6, 1],0],
    [0,[1, 1, 0],0,0,0,[1, 5, 1],0,[1, 7, 1]],
    [[2, 0, 0],0,[2, 2, 0],0,0,0,[2, 6, 1],0],
    [0,[3, 1, 0],0,0,0,[3, 5, 1],0,[3, 7, 1]],
    [[4, 0, 0],0,[4, 2, 0],0,0,0,[4, 6, 1],0],
    [0,[5, 1, 0],0,0,0,[5, 5, 1],0,[5, 7, 1]],
    [[6, 0, 0],0,[6, 2, 0],0,0,0,[6, 6, 1],0],
    [0,[7, 1, 0],0,0,0,[7, 5, 1],0,[7, 7, 1]]
]

#start_time = time.time()
#tulemus = minimax(a, 4, True)[1]
#print(round(time.time() - start_time, 4), " seconds")

averages = []
depths = []
for n in range(2,8):
    times = []
    for i in range(50):
        start_time = time.time()
        minimax(a, n, True)
        stop_time = round(time.time() - start_time, 4)
        times.append(stop_time)
    average = round(sum(times) / len(times), 4)
    averages.append(average)
    depths.append(n)
    print(n, average)

print(depths)
print(averages)