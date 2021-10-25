"""Metaclass which can mangle attributes and methods like this:
   <name> -> custom_<name>."""


class CustomMeta(type):
    """Metaclass for mangling attributes and methods."""
    def __new__(mcs, name, bases, namespace):
        to_rename = [name for name in namespace
                     if not name.startswith("__")
                     and not name.endswith("__")]
        for name in to_rename:
            namespace["custom_" + name] = namespace.pop(name)
        return super().__new__(mcs, name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        cls2rename = super().__call__(*args, **kwargs)
        vars2rename = list(vars(cls2rename).keys())
        for am_name in vars2rename:
            am = cls2rename.__getattribute__(am_name)
            cls2rename.__setattr__("custom_" + am_name, am)
            cls2rename.__delattr__(am_name)
        return cls2rename
