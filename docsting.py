
from functools import wraps

def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    #wrapper.__name__ = fn.__name__
    #wrapper.__name__ = fn.__doc__

    return wrapper


@decorator
def test(arg1, arg2):
    """
   общее описание
   примеры кода

    :param arg1: что это такое, описание параметра
    :param arg2:
    :return:
    """
    ...
@decorator
def test2(arg1, arg2):
    """

    :param arg1:
    :param arg2:
    :return:
    """
    ...
def test2(arg1, arg2):...

print(f"я вызываюсь при импорте и выполнении скрипта {__name__}")

if __name__ == '__main__':
    print(test.__name__)
    print(test.__doc__)
    help(test)


