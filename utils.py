import functools
import time

BATTLE_LOG = []


def log_action(func):
    """Записує кожен виклик методу в журнал бою."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        BATTLE_LOG.append(f"{args[0].name}: {func.__name__} -> {result}")
        return result
    return wrapper


def timer(func):
    """Показує, скільки часу виконувалась функція."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__}: {time.perf_counter() - start:.3f} с")
        return result
    return wrapper