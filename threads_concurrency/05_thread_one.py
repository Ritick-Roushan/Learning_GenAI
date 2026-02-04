import threading
import time 

def boil_milk():
    print("Boiling milk...")
    time.sleep(2)  # Simulate time taken to boil milk
    print("Milk boiled.")

def toast_bun():
    print("Toasting bun...")
    time.sleep(3)  # Simulate time taken to toast bun
    print("Bun toasted.")


start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print("Total time taken for making breakfast:", end - start)