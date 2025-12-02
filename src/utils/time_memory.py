import time
import psutil

def get_mem():
    return psutil.Process().memory_info().rss

class Timer:
    def __enter__(self):
        self.start = time.time()
        self.mem_start = get_mem()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        self.mem_end = get_mem()

    @property
    def time(self):
        return self.end - self.start

    @property
    def memory(self):
        return self.mem_end - self.mem_start
