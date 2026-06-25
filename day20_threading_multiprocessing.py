# Day 20 - Threading and Multiprocessing
import threading
import multiprocessing
import time

# Threading example
def worker(name, delay):
    print(f"Thread {name} starting")
    time.sleep(delay)
    print(f"Thread {name} done")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"T{i}", i * 0.5))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished")

# Thread Lock example
counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(100)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Counter: {counter}")  # Should be 100

# Multiprocessing example
def square(n):
    return n * n

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(10))
    print(results)
