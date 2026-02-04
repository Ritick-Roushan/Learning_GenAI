from multiprocessing import Process
import time 

def brew_chai(name):
    print(f"{name} chai brewing started")
    time.sleep(3)
    print(f"{name} chai brewing completed")

if __name__ == "__main__":
    chai_makers = [
                 Process(target=brew_chai, args=(f"ChaiMaker #{i+1}", ))
                    for i in range(3)
                 ]

    # start all processes

    for p in chai_makers:
        p.start()

    # wait for all processes to complete

    for p in chai_makers:
        p.join()

    print("All chai brewing completed.")         