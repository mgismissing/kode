from lib.ansi import screen, cursor, style

pyprint = print
pyexit = exit

def print(string: str) -> None:
    pyprint(string, end=style.RESET, flush=True)
def println(string: str) -> None:
    print(string + "\r\n")
def exit(code: int) -> None:
    print(screen.ERASE_SCREEN + cursor.HOME)
    pyexit(code)