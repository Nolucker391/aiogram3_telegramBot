from .users import User
from typing import Union, List, Callable, Any
from functools import wraps


def role_decorator(roles: Union[User, List[User]]) -> Callable:
    def decorator(func: Callable) -> Callable:
        setattr(func, 'role', roles)

        return func

    return decorator
