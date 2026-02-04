import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} is brewing chai...")
    count = 0
    for _ in range(5_000_000):
        count += 1
    print(f"{threading.current_thread().name} has finished brewing chai.")

thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
end = time.time()

print(f"Total time taken: {end - start} seconds")
# Note: Due to Python's Global Interpreter Lock (GIL), even though we are using
# multiple threads, the execution is not truly parallel.