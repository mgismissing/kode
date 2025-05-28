class cursor:
    def MOVE(type_: str) -> str:
        return "\033[" + type_
    def UP(lines: int) -> str:
        return cursor.MOVE(lines + "A")
    def DOWN(lines: int) -> str:
        return cursor.MOVE((lines + "B"))
    def LEFT(lines: int) -> str:
        return cursor.MOVE(lines + "D")
    def RIGHT(lines: int) -> str:
        return cursor.MOVE((lines + "C"))
    
    HOME: str = MOVE("H")

class screen:
    def ERASE(type_: str) -> str:
        return "\033[" + type_
    
    ERASE_SCREEN_FROM: str = ERASE("0J")
    ERASE_SCREEN_TO: str = ERASE("1J")
    ERASE_SCREEN: str = ERASE("2J")
    ERASE_LINE_FROM: str = ERASE("0K")
    ERASE_LINE_TO: str = ERASE("1K")
    ERASE_LINE: str = ERASE("2K")

class style:
    def STYLE(code: str) -> str:
        return "\033[" + code + "m"
    
    COLOR_BLACK: str = STYLE("30")
    COLOR_RED: str = STYLE("31")
    COLOR_GREEN: str = STYLE("32")
    COLOR_YELLOW: str = STYLE("33")
    COLOR_BLUE: str = STYLE("34")
    COLOR_MAGENTA: str = STYLE("35")
    COLOR_CYAN: str = STYLE("36")
    COLOR_WHITE: str = STYLE("37")
    RESET: str = STYLE("0")
    RESET_WEIGHT: str = STYLE("22")
    RESET_ITALIC: str = STYLE("23")
    RESET_UNDERLINE: str = STYLE("24")
    RESET_BLINK: str = STYLE("25")
    RESET_COLORSWAP: str = STYLE("27")
    RESET_VISIBILITY: str = STYLE("28")
    RESET_STRIKETHROUGH: str = STYLE("29")
    STYLE_BOLD: str = STYLE("1")
    STYLE_DIM: str = STYLE("2")
    STYLE_ITALIC: str = STYLE("3")
    STYLE_UNDERLINE: str = STYLE("4")
    STYLE_BLINK: str = STYLE("5")
    STYLE_COLORSWAP: str = STYLE("7")
    STYLE_HIDDEN: str = STYLE("8")
    STYLE_STRIKETHROUGH: str = STYLE("9")