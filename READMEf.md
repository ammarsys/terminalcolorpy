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

<<<<<<< HEAD

`flip_text(text: str) -> str:`
=======
TerminalColorPy has 4 main functions,
- prainbow
- colored
- blink
- printcolor
- flip_text

**prainbow** Its alias is *pr*, takes a single parameter and returns text formatted in rainbow colors.

**colored** Its alias is *c*, takes 4 parameters, which are:
 - text (mandatory)
 - color (mandatory)
 - highlight (optional)
 - markup (optional)

**blink** Its alias is *b*, takes 2 parameterers, which are:
- message (mandatory),
  - initial message to print
- length (optional)
  - how long until the initial message should change
- new_message (optional)
  - what to replace the initial message with, defaulting to ''

**printcolor** Its alias is *pc*, takes 2 parameters, which are:
- print_arguments (optional) 
  - arguments for the builtin python3 print function
- kwargs (mandatory)
  - keyword arguments for the terminalcolorpy.colored function

Message is the string to print to the console, length is how long it should stay and 
new message is what it should be replaced with.

HighLight & Color take either a string, a RGB value or even a hex code. For example,
    
```python
from terminalcolorpy import colored, blink, printcolor

print(colored('Hello', color='#42f5d7',
         markup=['striked', 'bold', 'underline', 'italic'],
         highlight='#42f5d7')
      )

print(colored('World', color='red',
         markup=['striked', 'bold'],
         highlight='blue')
      )

blink(colored('!', color=[122, 99, 0],
         markup=['bold'],
         highlight=[122, 100, 78])
      )
      
printcolor({'end': ''}, color='blue', text='Hello')
>>>>>>> f705321cabfd356765f69be4e99a37852c1c550d
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

<<<<<<< HEAD
    Args:
        message (str): message to be printed
        length (float): how long should the message stay
        new_message (str): message to be displayed after the timer expires (default is nothing)
```
<br><hr>

`printcolor(colored_kwargs: dict = None, **kwargs) -> None:`
```
->  Implements a shortcut for using the builtin function print with this modules colored function.
=======
It works on any terminals that support ASCII codes, includes but not limited to:

To use this in a Windows terminal, simply make an empty system call which enables colors in the terminal:
>>>>>>> f705321cabfd356765f69be4e99a37852c1c550d

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
