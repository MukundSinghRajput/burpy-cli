from .enum import TextFormat


def format_text(text: str, *styles: TextFormat) -> str:
    """
    Format text with multiple styles/colors

    Example:
    format_text("Hello", TextFormat.RED, TextFormat.BOLD)
    """
    formatted_text = text
    for style in styles:
        formatted_text = f"{style.value}{formatted_text}{TextFormat.RESET.value}"
    return formatted_text