import ui
import readchar as rc
from iolib import *
import lib.ansi

screen = ui.Screen()

print(lib.ansi.screen.ERASE_SCREEN + lib.ansi.cursor.HOME)

prompt = ""
prompt_msg = ""
while True:
    # Render screen
    screen.render()
    # Raw read next character (no waiting for enter key)
    char = rc.readchar()
    match char:
        case "\n":
            # Command handler
            prompt_msg = screen.run_command(prompt)
            # Reset prompt
            prompt = ""
        case _:
            # Add character to prompt
            prompt += char
    # Set the updated prompt
    screen.set_prompt(prompt, prompt_msg)