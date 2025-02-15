import threading

def stress_cpu():
    while True:
        pass  # Infinite loop to utilize CPU

# Create multiple threads to maximize CPU usage
num_threads = 8  # Adjust based on your CPU cores
threads = []

for _ in range(num_threads):
    t = threading.Thread(target=stress_cpu)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
