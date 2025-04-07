class TerminalColors:
    """Clearly structured ANSI escape sequences for terminal colors."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colorize(text: str, color: str, bold: bool = False, underline: bool = False) -> str:
    """
    Clearly colorize text strings for enhanced terminal output readability.

    Args:
        text (str): Text clearly defined to colorize.
        color (str): Color explicitly provided from TerminalColors class.
        bold (bool): Optionally bold text explicitly.
        underline (bool): Optionally underline text explicitly.

    Returns:
        str: Colored terminal string clearly generated.
    """
    formatted_text = color

    if bold:
        formatted_text += TerminalColors.BOLD
    if underline:
        formatted_text += TerminalColors.UNDERLINE

    formatted_text += text + TerminalColors.ENDC
    return formatted_text

def demonstrate_colors():
    """ Clearly structured demo for easy interactive use."""
    print(colorize("PrimeVox SDK - Success Message", TerminalColors.GREEN, bold=True))
    print(colorize("PrimeVox SDK - Warning Message", TerminalColors.WARNING))
    print(colorize("PrimeVox SDK - Error Message", TerminalColors.FAIL, underline=True))
    print(colorize("PrimeVox SDK - Information", TerminalColors.CYAN))

# Explicit interactive execution provided
if __name__ == "__main__":
    demonstrate_colors()