from multiprocessing import Process
import time

def crunch_numbers():
    print("Starting to crunch numbers...")
    total = 0
    for _ in range(100_000_00):
        total += 1
    print("Finished crunching numbers. Total:", total)

if __name__ == "__main__":    

    start  = time.time()

    p1 = Process(target=crunch_numbers)
    p2 = Process(target=crunch_numbers)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()
    print("Total time taken:", end - start)