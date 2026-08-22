def add_init(cls):
    fields = cls.__annotations__

    def __init__(self, **kwargs) -> None:
        for name in fields:
            if name not in kwargs:
                raise TypeError(f"Missing argument: {name}")
            setattr(self, name, kwargs[name])

    cls.__init__ = __init__
    return cls