"""Metaclass which can mangle attributes and methods like this:
   <name> -> custom_<name>."""


class CustomMeta(type):
    """Metaclass for mangling attributes and methods."""
    def __call__(cls, *args, **kwargs):
        cls2rename = super().__call__(*args, **kwargs)
        dirs2rename = set([am_name for am_name in dir(cls2rename)
                           if not am_name.startswith("__")])
        vars2rename = set(list(vars(cls2rename).keys()))
        dirs2rename = dirs2rename - vars2rename
        for am_name in dirs2rename:
            am = super().__getattribute__(am_name)
            super().__setattr__("custom_" + am_name, am)
            super().__delattr__(am_name)
        for am_name in vars2rename:
            am = cls2rename.__getattribute__(am_name)
            cls2rename.__setattr__("custom_" + am_name, am)
            cls2rename.__delattr__(am_name)
        return cls2rename
