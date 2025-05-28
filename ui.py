from lib.ansi import *
import os
from iolib import *
import cmdlib

class Window:
    def __init__(self, title: str | None = None):
        self.title = title

class Screen:
    def __init__(self):
        self.width, self.height = os.get_terminal_size()
        self.set_prompt()
        self.windows = []
    def render(self):
        print(cursor.HOME + screen.ERASE_LINE + style.COLOR_WHITE + "> " + style.COLOR_GREEN
        + (style.COLOR_GREEN + style.STYLE_ITALIC + style.STYLE_UNDERLINE + self.prompt_msg + cursor.HOME if self.prompt == "" else self.prompt))
    def set_prompt(self, prompt: str = "", prompt_msg: str = ""):
        self.prompt = prompt
        self.prompt_msg = prompt_msg
    def run_command(self, command: str) -> str:
        if command == "x":
            exit(0)
        elif command.startswith("wa"): # Window Add <title>
            args = cmdlib.get_args("wa", command, maxsplit=1)
            self.add_window(Window(args[0] if len(args) != 0 else None))
            return "Opened window #"
        elif command.startswith("we"): # Window Edit <id> <x> <y>
            args = cmdlib.get_args("we", command, maxsplit=4)
            return "Moved window # to x y"
        elif command.startswith("wf"): # Window Focus <id>
            args = cmdlib.get_args("wf", command, maxsplit=2)
            return "Press CTRL+X to unfocus from window #"
        elif command.startswith("wxa"): # Window Close All
            while len(self.windows) != 0: self.remove_window(0)
            return "Closed windows"
        elif command.startswith("wx"): # Window Close <id>
            args = cmdlib.get_args("wx", command, maxsplit=2)
            if not (len(args) != 0 and args[0].isdigit()): return "No #"
            window_id = int(args[0])
            if not (0 <= window_id < len(self.windows)): return "Idk #"
            self.remove_window(window_id)
            return "Closed window #"
        else:
            return f"Invalid command \"{command}\""
    def add_window(self, window: Window) -> int:
        self.windows.append(window)
        return len(self.windows)-1
    def remove_window(self, window_id: int) -> Window:
        return self.windows.pop(window_id)