import typing
import random
import time

GITHUB = 'https://www.github.com/ammar-sys/terminalcolorpy'
END = '\033[0m'

class _Colors:
    """
    The class containing all necessary things in order for this module to work. This is an private class.
    All highlights are formatted in the following way: color + hl (ex: grayhl)
    """
    color_dict = {
        # color
        'pink': '\033[95m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'red': '\033[91m',
        'black': '\x1b[30m',
        'orange': '\033[38;2;255;69;0m',
        # highlight
        'grayhl': '\x1b[7m',
        'pinkhl': '\x1b[45m',
        'blackhl': '\x1b[40m',
        'yellowhl': '\x1b[43m',
        'greenhl': '\x1b[42m',
        'bluehl': '\x1b[44m',
        'redhl': '\x1b[41m',
        # markup
        'bold': '\033[1m',
        'underline': '\033[4m',
        'italic': '\x1B[3m',
        'striked': '\033[9m',
        'framed': '\033[52m'
    }

    def hex_to_rgb(self, hexcode: str) -> list:
        """
        Convert a hex code (string) to RGB. Source: https://gist.github.com/matthewkremer/3295567

        :param str hexcode: hexcode to convert
        """
        hexcode = hexcode.lstrip('#')
        hlen = len(hexcode)
        return list(int(hexcode[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))

    def rgb_to_ansii(self, rgb: typing.Union[list, tuple], num: int) -> str:
        """
        Convert RGB list/tuple to a ANSI string.

        :param rgb: list to convert
        :param num: 38 or 48. represents whether the string should be a highlight or a color
        """
        return f"\033[{num};2;{rgb[0]};{rgb[1]};{rgb[2]}m"

colors = _Colors()

def flip_text(text: str) -> str:
    """Flip text to characters that are upside down version of that letter."""
    return text.translate(str.maketrans(r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""",
                                        r"""ɐqɔpǝɟƃɥᴉɾʞꞁɯuodbɹsʇnʌʍxʎzⱯᗺƆᗡƎᖵ⅁HIᒋ⋊ꞀWNOԀꝹᴚS⊥∩ɅMX⅄Z0ІᘔƐᔭ59Ɫ86¡„#$%⅋,)(*+'-˙/:؛>=<¿@]\[ᵥ‾`}|{~"""))[::-1]

def prainbow(text: str) -> str:
    """Print text in rainbow colors."""
    return ''.join([colors.rgb_to_ansii((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), 38) + i
                    for i in text]) + END


def blink(message: str, lenght: float = 1.0, new_message: str = ' ') -> None:
    """
    Print a text then replace it with something else.

    :param message: initial message to print
    :param lenght: how long the initial message should stay
    :param new_message: what should the initial message be replaced with
    """
    print(message, end='')
    time.sleep(lenght)
    print(f'\r{new_message}')

def colored(
        text: str,
        color: typing.Union[list, tuple, str],
        highlight: typing.Union[list, tuple, str] = None,
        markup: typing.Union[list, tuple] = None
) -> str:
    """
    Return colored text from the _Colors.color_dict dictionary as well as highlight and markup.

    :param str text: text to colorify
    :param list, tuple, str color: color for the text. accepts RGB, hex (in string form) and values from the dict
    :param list, tuple, str highlight: highlight for the text. accepts RGB, hex (in string form) and values from the dict
    :param list, tuple markup: markup from _Colors.color_dict
    """
    to_return = []
    try:
        color = color.lower() if isinstance(color, str) else color
        highlight = highlight.lower() if isinstance(highlight, str) else highlight
        markup = map(str.lower, markup) if isinstance(markup, (list, tuple)) else markup

        for k, v in ((color, 38), (highlight, 48)):
            if isinstance(k, str):
                if '#' in k:
                    to_return.append(colors.rgb_to_ansii(colors.hex_to_rgb(k), v))
                else:
                    to_return.append(colors.color_dict[k if k == 38 else k + 'hl'])

            elif isinstance(k, (list, tuple)):
                if max(k) > 255:
                    raise Exception('The RGB values must be inbetween 1 and 255.')
                to_return.append(colors.rgb_to_ansii(k, v))

        if isinstance(markup, (list, tuple)):
            to_return.append(''.join(colors.color_dict[i] for i in markup))

    except KeyError:
        raise Exception('Could not find the provided element, please look at the acceptable options over at: {}'.format(GITHUB))

    return ''.join(to_return) + text + END

def printcolor(print_arguments: dict = None, **kwargs) -> None:
    """
    Print colored text.

    :param print_arguments: arguments for the builtin print function (py3+)
    :param kwargs: keyword arguments for the colored function
    """
    print(colored(**kwargs), **print_arguments if print_arguments is not None else {})

# aliases
c, pr, b, pc = colored, prainbow, blink, printcolor
