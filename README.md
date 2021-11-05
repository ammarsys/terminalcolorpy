# terminalcolorpy


[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

This is a simple package to print colored messages using ASCI to the terminal built with python 3.

# Installation

```py
# Linux/MacOS
python3 -m pip install terminalcolorpy

# Windows
py -m pip install terminalcolorpy
```

For the dev version, do:
```
git clone https://github.com/ammarsys/terminalcolorpy
cd terminalcolorpy
```

# Usage of terminalcolorpy


Usage of it is pretty straight-forward,
```py
import terminalcolorpy as tp

print(tp.colored('Hello', color='#42f5d7',
         markup=['striked', 'bold', 'underline', 'italic'],
         highlight='#a8328b')
      )
```

TerminalColorPy has 4 main functions,
- prainbow
- colored
- blink
- printcolor
- flip_text

**prainbow** Its alias is *pr*, takes a single parameter which is text to return as rainbow.

**colored** Its alias is *c*, takes 4 parameteres, which are:
 - text (mandatory)
 - color (mandatory)
 - highlight (optional)
 - markup (optional)

**blink** Its alias is *b*, takes 2 parameterers, which are:
- message (mandatory),
  - initial message to print
- lenght (optional)
  - how long til the initial message should change
- new_message (optional)
  - what to replace initial message with, default ''

**printcolor** Its alias is *pc*, takes 2 parameters, which are:
- print_arguments (optional) 
  - arguments for the builtin python3 print function
- kwargs (mandatory)
  - keyword arguments for the terminalcolorpy.colored function

Message is the string to print to the console, lenght is how long it should stay and 
new message is what it should be replaced with.

HighLight & Color take either a string, an RGB value or even a hex code. For example,
    
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
```

For more examples check **tests/tests.py** (github)

# List of accepted values
```python
    
    # these aren't CaSe SeNsItIvE!
    
highlight_values = [
        'gray',
        'pink',
        'black',
        'yellow',
        'green',
        'blue',
        'red'
]

color_values = [
        'pink',
        'blue',
        'cyan',
        'green',
        'yellow',
        'red',
        'black',
        'orange'
]

text_markup_values = [
        'bold',
        'underline',
        'italic',
        'striked'
]
```

**Hex Generator** https://www.google.com/search?q=hex+color

**RGB Generator** https://www.w3schools.com/colors/colors_rgb.asp

It works on any terminals that support ASCII codes, include but not limited to:

To use this in a Windows terminal, simply make a empty system call which enables colors in the terminal:

`import os; os.system('')'`

| Terminals      | Works On |
| ----------- | ----------- |
| PyCharm      | True       |
| Python IDLE   | False        |
| Windows CMD    | True (limited!)  |
| Mac-OS iTerm2         | True |
| VSCode | True
|  Visual Studio Code | True

