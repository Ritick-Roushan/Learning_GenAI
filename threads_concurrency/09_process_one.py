import threading
import time

def cpu_heavy():
    print(f"crunchy some numbers...")
    total =0
    for i in range(10**7):
        total += 1
    print("Done")

start  = time.time()
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Time Taken: {time.time()-start:.2} seconds")