<h1 align="center">terminal<span style="color:#4c5461">color</span>py</h1>
<p align="center"><i>A lightweight, dependency-free package to colorize your terminal text.</i></p>

# Overview

This is a package that utilizes ANSI escape sequences to colorize your stdout, terminal, printed messages and what not. The key-features include,

- Fully tested with pytest
- Fully documented & type-hinted
- Dependency-free

# Installation

> The required Python version for this module is 3.10 or above

```
# Linux/MacOS
python3 -m pip install terminalcolorpy

# Windows
py -m pip install terminalcolorpy
```

# Usage

The package consists of a few functions which are explained down below. In case your terminal
(which is common with Windows) doesn't display the color at all, please run the following code,

```python
import os

os.system('')

# your code onwards
```
<br><br><hr>


`flip_text(text: str) -> str:`
```
->  Flip text to characters that are upsidedown version of that letter.
```
<br><hr>

`prainbow(text: str) -> str:`
```
->  Returns text in colors of the rainbow (RGB 1-255, not CSPRNG).
```
<br><hr>

`blink(message: str, length: float = 1, new_message: str = " ") -> None:`
```
->  Print the message then replace it with a new message.


    Beware, this function is **blocking** because of the print statement. If you need to run this function
    synchronously, please refer to the accepted answer of this S/O question,
    https://stackoverflow.com/questions/54685210/calling-sync-functions-from-async-function

    Args:
        message (str): message to be printed
        length (float): how long should the message stay
        new_message (str): message to be displayed after the timer expires (default is nothing)
```
<br><hr>

`printcolor(colored_kwargs: dict = None, **kwargs) -> None:`
```
->  Implements a shortcut for using the builtin function print with this modules colored function.

    Args:
        colored_kwargs (dict): keyword arguments for this modules colored function
        **kwargs: keyword arguments for the builtin print function
```
<br><hr>

```
def colored(
    text: str,
    color: list | tuple | str,
    highlight: list | tuple | str | None = None,
    markup: list | tuple | None = None,
) -> str:
```
```
->  Parse color arguments and return the applied version to the text.

    Args:
        text (str): text to parse
        color (Union[list, tuple, str]): color for the text, accepts RGB, hex (str) and English words
        highlight ([list, tuple, str]): highlight for the text, accepts RGB, hex (str) and English words
        markup ([list, tuple]): markup from _Colors.color_dict
```
