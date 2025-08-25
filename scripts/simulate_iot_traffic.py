
"""
Simulate IoT-like network activity (placeholder).

Use hping3/nmap externally for realistic traffic or extend this script
to generate HTTP requests, DNS queries, etc.
"""
import time
import random

DEVICES = ["smart-tv", "camera-1", "thermostat", "router", "tablet"]
DESTS = ["example.com", "api.test.dev", "cdn.assets.net"]

def simulate():
    for _ in range(10):
        device = random.choice(DEVICES)
        dest = random.choice(DESTS)
        bytes_out = random.randint(5000, 300000)
        print(f"{device} -> {dest} : {bytes_out} bytes sent")
        time.sleep(0.5)

if __name__ == "__main__":
    simulate()
