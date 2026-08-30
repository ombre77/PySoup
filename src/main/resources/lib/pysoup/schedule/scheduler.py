from typing import Optional
from ..utils import _gBridge

class Task:
    def __init__(self) -> None:
        self.id: Optional[int] = None

    def cancel(self) -> None:
        if self.id is None:
            raise RuntimeError("cancel() called before this task was assigned an id")
        _gBridge().cancelTask(self.id)

def run_later(delay_ticks:int):
    def marker(fn):
        fn._pysoup_schedule=("later",delay_ticks)
        return fn

    return marker

def repeating(delay_ticks:int,period_ticks:int):
    def marker(fn):
        fn._pysoup_schedule=("timer",delay_ticks,period_ticks)
        return fn
    return marker

def async_task():
    def marker(fn):
        fn._pysoup_async=True
        return fn
    return marker


def task():
    """Mark the function as a schedule task. You can then use @run_later, @repeating or @async_task to run as you like.
    
The assignated method **has** to get 1 task arg

e.g.
```python
@task()
@run_later(10)
def some_task(task:Task):
    broadcast(f"cancelling task {task.id}")
    task.cancel()
    ```"""
    def decorator(fn):
        schedule=getattr(fn,"_pysoup_schedule",("now",0))
        is_async=getattr(fn,"_pysoup_async",False)
        kind=schedule[0]

        t=Task()

        def callback():
            fn(t)

        if kind=="now":
            task_id=_gBridge().runTaskAsync(callback) if is_async else _gBridge().runTask(fn)
        elif kind=="later":
            _,delay=schedule
            task_id=_gBridge().runTaskLater(callback,delay)
            if is_async:
                raise ValueError("run_later() doesn't support async yet - use repeating() with async_task() instead")
        elif kind=="timer" and len(schedule)==3:
            _,delay,period=schedule
            task_id=(_gBridge().runTaskTimerAsync(callback,delay,period) if is_async else
                _gBridge().runTaskTimer(callback,delay,period))

        else:
            raise ValueError(f"Unknown schedule: {kind}")

        return fn
    return decorator

