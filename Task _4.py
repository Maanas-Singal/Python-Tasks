import threading
import time

def function_one():
    # Simulate some task for function_one
    for _ in range(5):
        print("Function One")
        time.sleep(1)

def function_two():
    # Simulate some task for function_two
    for _ in range(5):
        print("Function Two")
        time.sleep(1)

if __name__ == "__main__":
    # Create two threads for each function
    thread_one = threading.Thread(target=function_one)
    thread_two = threading.Thread(target=function_two)

    # Start both threads
    thread_one.start()
    thread_two.start()

    # Wait for both threads to finish
    thread_one.join()
    thread_two.join()

    print("Both functions have finished.")
====================================================================
## We have defined two functions function_one and function_two, and used the threading architecture.
## Thread class to create two threads for each function. 
## The start() method is used to start the execution of both threads. 
## Then, we use the join() method to wait for both threads to complete before printing the final message
