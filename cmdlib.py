def get_args(command: str, prompt: str, sep: str = " ", maxsplit: int = -1):
    argstr = prompt.split(command+" ", maxsplit=1)
    if len(argstr) != 2: return []
    args = argstr[1].split(sep=sep, maxsplit=maxsplit)
    return [] if args == [""] else args