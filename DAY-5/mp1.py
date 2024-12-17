import multiprocessing
import os
import time

def f1():
    print(f'This is f1 block: PID:{os.getpid()} PPID:{os.getppid()}')
    time.sleep(1)
    print('Exit from f1 block')

def f2():
    print(f'This is f2 block: PID:{os.getpid()} PPID:{os.getppid()}')
    time.sleep(1)
    print('Exit from f2 block')

print(f"This is main block: PID:{os.getpid()} PPID:{os.getppid()}")

if __name__ == '__main__':
    P1 = multiprocessing.Process(target=f1)
    P1.start()
    P2 = multiprocessing.Process(target=f2)
    P2.start()
    P1.join()
    P2.join()
    print(f"This is main block: PID:{os.getpid()} PPID:{os.getppid()}")
    print("Exit from main block")
