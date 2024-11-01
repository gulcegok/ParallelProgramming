import tracemalloc
import time

def performance(f):
    setattr(performance, 'counter', 0)
    setattr(performance, 'total_mem', 0)
    setattr(performance, 'total_time', 0)

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        setattr(performance, 'counter', getattr(performance, 'counter') + 1)
        setattr(performance, 'total_mem', getattr(performance, 'total_mem') + peak)
        setattr(performance, 'total_time', getattr(performance, 'total_time') + end_time - start_time)
        return result
    return wrapper
