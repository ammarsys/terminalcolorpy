# Standard library imports

from typing import Union

import time
import random


GITHUB = "https://www.github.com/novusys/terminalcolorpy"
END = "\033[0m"
COLOR_DICT = {
    # color
    "pink": "\033[95m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "black": "\x1b[30m",
    "orange": "\033[38;2;255;69;0m",
    # highlight
    "grayhl": "\x1b[7m",
    "pinkhl": "\x1b[45m",
    "blackhl": "\x1b[40m",
    "yellowhl": "\x1b[43m",
    "greenhl": "\x1b[42m",
    "bluehl": "\x1b[44m",
    "redhl": "\x1b[41m",
    # markup
    "bold": "\033[1m",
    "underline": "\033[4m",
    "italic": "\x1B[3m",
    "striked": "\033[9m",
    "framed": "\033[52m",
}


def hex_to_rgb(hexcode: str) -> list:
    """Convert a hex code (string) to RGB. Source: """

    hexcode = hexcode.lstrip("#")
    hlen = len(hexcode)
    return list(
        int(hexcode[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)
    )


def rgb_to_ansi(rgb: Union[list, tuple], num: int) -> str:
    """
    Converts RGB to ANSI escape sequences.

    Args:
        rgb (Union[list, tuple]): list/tuple to convert
        num (int): 38 or 4; represents whether the string should be a highlight or a color

    Returns:
        str with ANSI escape sequences
    """

    return f"\033[{num};2;{rgb[0]};{rgb[1]};{rgb[2]}m"


def flip_text(text: str) -> str:
    """Flip text to characters that are upside down version of that letter."""

    return text.translate(
        str.maketrans(
            r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""",
            r"""ɐqɔpǝɟƃɥᴉɾʞꞁɯuodbɹsʇnʌʍxʎzⱯᗺƆᗡƎᖵ⅁HIᒋ⋊ꞀWNOԀꝹᴚS⊥∩ɅMX⅄Z0ІᘔƐᔭ59Ɫ86¡„#$%⅋,)(*+'-˙/:؛>=<¿@]\[ᵥ‾`}|{~""",
        )
    )[::-1]


def prainbow(text: str) -> str:
    """Returns text in colors of the rainbow (RGB 1-255, not CSPRNG)"""

    return (
        "".join(
            [
                rgb_to_ansi(
                    (
                        random.randint(1, 255),
                        random.randint(1, 255),
                        random.randint(1, 255),
                    ),
                    38,
                )
                + i
                for i in text
            ]
        )
        + END
    )


def blink(message: str, length: float = 1, new_message: str = " ") -> None:
    """
    Print the message then replace it with a new message.

    Beware, this function is **blocking** because of the print statement. If you need to run this function
    synchronously, please refer to the accepted answer of this S/O question,
    https://stackoverflow.com/questions/54685210/calling-sync-functions-from-async-function

    Args:
        message (str):
        length (float):
        new_message (str): message to be displayed after the timer expires (default is nothing)

    Returns:
        None
    """

    print(message, end="")
    time.sleep(length)
    print(f"\r{new_message}")


def colored(
    text: str,
    color: Union[list, tuple, str],
    highlight: Union[list, tuple, str] = None,
    markup: Union[list, tuple] = None,
) -> str:
    """
    Parse color arguments and return the applied version to the text.

    Args:
        text (str): text to parse
        color (Union[list, tuple, str]): color for the text, accepts RGB, hex and English words
        highlight ([list, tuple, str]): highlight for the text, accepts RGB, hex and English words
        markup ([list, tuple]): markup from _Colors.color_dict

    Returns:
        A string with the (now colored) text
    """

    to_return = []
    try:
        color = color.lower() if isinstance(color, str) else color
        highlight = highlight.lower() if isinstance(highlight, str) else highlight
        markup = [i.lower() for i in markup] if isinstance(markup, (list, tuple)) else markup

        for k, v in ((color, 38), (highlight, 48)):
            if isinstance(k, str):
                if "#" in k:
                    to_return.append(rgb_to_ansi(hex_to_rgb(k), v))
                else:
                    to_return.append(COLOR_DICT[k if v == 38 else k + "hl"])

            elif isinstance(k, (list, tuple)):
                if max(k) > 255:
                    raise Exception("The RGB values must be inbetween 1 and 255.")
                to_return.append(rgb_to_ansi(k, v))

        if isinstance(markup, (list, tuple)):
            to_return.append("".join(COLOR_DICT[i] for i in markup))

    except KeyError:
        raise Exception(
            "Could not parse the arguments, please see the documentation over at {}".format(
                GITHUB
            )
        )

    return "".join(to_return) + text + END


def printcolor(colored_kwargs: dict = None, **kwargs) -> None:
    """
    Implements a shortcut for using the builtin function print with this modules colored function.

    Args:
        colored_kwargs (dict): keyword arguments for this modules colored function
        **kwargs: keyword arguments for the builtin print function

    Returns:
        None
    """

    colored_kwargs = colored_kwargs or {}

    print(colored(**colored_kwargs), **kwargs)


# aliases
c, pr, b, pc = colored, prainbow, blink, printcolor
