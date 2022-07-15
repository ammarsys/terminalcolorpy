import terminalcolorpy

control = [
    terminalcolorpy.colored(
        text="wee",
        color="red",
        markup=["striked", "framed", "bold", "underline", "italic"],
        highlight="blue",
    ),
    terminalcolorpy.colored(
        text="woo",
        color=[122, 122, 0],
        markup=["striked", "framed", "bold", "underline", "italic"],
        highlight=[111, 5, 0],
    ),
    terminalcolorpy.colored(
        text="!",
        color="#000000",
        markup=[
            "striked",
            "framed",
            "bold",
            "underline",
            "italic",
        ],
        highlight="#00bfff",
    ),
]

print(control)

for thing in control:
    print(thing)
