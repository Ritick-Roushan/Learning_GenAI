from multiprocessing import Process
import time

def cpu_heavy():
    print(f"crunchy some numbers...")
    total =0
    for i in range(10**8):
        total += 1
    print("Done")

if __name__ == "__main__":
    start  = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print(f"Time Taken: {time.time()-start:.2} seconds")