#!/usr/bin/python3

import matplotlib.pyplot as plt
from PIL import Image

# Open the file and read the ping times into a list
with open('test.txt') as f:
    ping_times = []
    for line in f:
        if 'time=' in line:
            time_index = line.find('time=') + 5
            end_index = line.find(' ms')
            ping_times.append(float(line[time_index:end_index]))

# Create a graph
plt.plot(ping_times)

# Add labels and titles
plt.xlabel('Ping Number')
plt.ylabel('Ping Time (ms)')
plt.title('Ping Times')

# Show the graph
plt.savefig("graph.png")
img = Image.open("graph.png")
img.show()
