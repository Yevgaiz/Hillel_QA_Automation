import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.in_progres = False

    def start(self):
        if not self.in_progres:
            self.start_time = time.time()
            self.in_progres = True

    def stop(self):
        if self.in_progres:
            end_time = time.time()
            self.elapsed_time += end_time - self.start_time
            self.in_progres = False

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.in_progres = False

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second
time.sleep(1)
with t:
    time.sleep(2)
print(t.elapsed_time)  # ~3 seconds

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds
