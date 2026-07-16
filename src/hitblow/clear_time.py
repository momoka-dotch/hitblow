import time


def start_timer():
    return time.time()


def format_elapsed(start_time):
    elapsed = time.time() - start_time
    return f"{elapsed:.1f}秒"