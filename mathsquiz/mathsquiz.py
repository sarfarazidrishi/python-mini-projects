import random
import time
import threading
from queue import Queue

min_limit=1
max_limit=10
total_problems=4
time_limit=10

def generate_problem():
    operator=random.choice(["+", "-", "*"])
    left=random.randint(min_limit, max_limit)
    right=random.randint(min_limit, max_limit)
    problem=f"{left}{operator}{right}"
    # answer=eval(problem)
    # print(f"{left}+{right}={answer}")
    return problem

def get_input(queue):
    try:
        user_input=input()
        queue.put(user_input)
    except Exception:
        queue.put(None)
        
print("welcome to the maths quiz, you have limited time for each question")
for i in range(total_problems):
    problem=generate_problem()
    answer=eval(problem)
    print(f"Question {i+1}: {problem} ")
    
    question_start_time=time.time()
    input_queue=Queue()
    while time.time()-question_start_time<time_limit:
        remaining_time=time_limit-(time.time()-question_start_time)
        print(f" Time remaining {remaining_time:.1f} seconds", end="\r")
        
        input_thread=threading.Thread(target=get_input, args=(input_queue,))
        input_thread.daemon=True
        input_thread.start()
        
        input_thread.join(timeout=remaining_time)
        
        if input_queue.empty():
            print("time's u! moving to the next Question")
            print(f"the correct answer is: {answer}")
            break
        
        try:
            user_answer=float(input_queue.get_nowait())
            if user_answer==answer:
                print("correct")
                break
            else:
                print("wrong answer! try again")
        except ValueError:
            print("invalild input: enter a number")
        
        if time.time()- question_start_time>=time_limit:
            print("time is up")
            print(f"correct anser is {answer}")
            break
print("quiz completed")


"""niche dusra program h """
# from queue import Queue
# import threading
# import time

# task_queue=Queue()

# def producer():
#   for i in range(5):
#     task=f"task {i+1}"
#     print(f"producing task {task}")
#     task_queue.put(task)
#     time.sleep(1)

# def consumer():
#   while not task_queue.empty() or producer_thread.is_alilve():
#     if not task_queue.empty():
#       task=task_queue.get()
#       print(f"consuming {task}")
#       time.sleep(2)
#       task_queue.task_done()
#     else:
#       print("consumer waiting to be added task from producer")
#       time.sleep(0.5)

# producer_thread=threading.Thread(target=producer)
# producer_thread.start()
# consumer_thread=threading.Thread(target=consumer)
# consumer_thread.start()

# producer_thread.join()
# task_queue.join()

# consumer_thread.join()

