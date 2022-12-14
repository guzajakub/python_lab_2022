import threading
import time
import random

"""
In this exercise I was cooperating with M.Kaszuba
"""

class Philosopher(threading.Thread):

    def __init__(self, philosopher, first, second, deadlock):
        super().__init__()
        self.philosopher = philosopher
        self.first_fork = first
        self.second_fork = second
        self.without_deadlock = deadlock

    def eating(self):

        first_fork_num = self.philosopher
        second_fork_num = (self.philosopher + 1) % 5

        if self.without_deadlock:
            if self.philosopher % 2 == 0:
                temp = self.first_fork
                self.first_fork = self.second_fork
                self.second_fork = temp
                first_fork_num = (self.philosopher + 1) % 5
                second_fork_num = self.philosopher

        time.sleep(random.randint(1, 6))
        self.first_fork.acquire()
        print(f"Philosopher {self.philosopher} acquired fork {first_fork_num} \n")

        time.sleep(random.randint(1, 6))
        self.second_fork.acquire()
        print(f"Philosopher {self.philosopher} acquired fork {second_fork_num} \n")

        time.sleep(2)
        print(f"Philosopher {self.philosopher} is eating...\n")

        self.first_fork.release()
        print(f"Philosopher {self.philosopher} released fork {first_fork_num} \n")
        self.second_fork.release()
        print(f"Philosopher {self.philosopher} released fork {second_fork_num} \n")

    def run(self):
        while True:
            print(f"Philosopher {self.philosopher} is thinking\n")
            time.sleep(random.randint(1, 6))
            self.eating()


if __name__ == '__main__':

    without_deadlock = True
    forks = [threading.Condition(threading.Lock()) for idx in range(5)]
    philosophers = [Philosopher(num, forks[num], forks[(num + 1) % 5], without_deadlock) for num in range(5)]

    for philo in philosophers:
        philo.start()
