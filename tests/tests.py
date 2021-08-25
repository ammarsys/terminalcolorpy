import terminalcolorpy.tcp as tp

# most basic cases
print(tp.flip_text('Hello World!'))
print(tp.colored('Hello World!', 'red'))
print(tp.prainbow('Well, hello there!'))

tp.printcolor({'end': ''}, color='red', text='Hello!')
tp.blink('Shhh, I am gone now!')

# more arguments (advanced use cases)
print(tp.colored(text='Hello World!',
                 color='red',
                 markup=['striked', 'framed', 'bold', 'underline', 'italic'],
                 highlight='blue'))

print(tp.colored(text='Hello World! No',
                 color=[122, 122, 0],
                 markup=['striked', 'framed', 'bold', 'underline', 'italic'],
                 highlight=[111, 5, 0]))

print(tp.colored(text='Hello World! Yes',
                 color='#000000',
                 markup=['striked', 'framed', 'bold', 'underline', 'italic', ],
                 highlight='#00bfff'))

tp.blink(message=tp.colored(text='Hello World!',
                            color='#000000',
                            highlight='#00bfff'), new_message='Oh... I am back to normal text!')
tp.printcolor({'end': ''},
              text='Hello World! Hmm',
              color='#000000',
              markup=['striked', 'framed', 'BOLD', 'uNderLine', 'italic'],
              highlight='#00bfff')
