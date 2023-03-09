#!/usr/bin/python3

import subprocess
import re
import matplotlib.pyplot as plt
from PIL import Image

# Define the host to ping
host = str(input("IP address or domain: "))

# Define the number of pings to send
count = 10

# Execute the ping command and capture its output
print(f"Pinging to {host}...")
ping_output = subprocess.check_output(["ping", "-c", str(count), 
host]).decode("utf-8")

# Parse the output to extract the ping times
ping_times = re.findall(r"time=(\d+\.\d+)", ping_output)

# Convert the ping times to floating-point numbers
ping_times = [float(time) for time in ping_times]

# Plot the ping times as a line graph
plt.plot(ping_times)
plt.xlabel("Ping Number")
plt.ylabel("Ping Time (ms)")
plt.title(f"Ping Times to {host}")
plt.grid(True)

# Save the plot to a file
plt.savefig("graph.png")
img = Image.open("graph.png")
img.show()

print("done!")
