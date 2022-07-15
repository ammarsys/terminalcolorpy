# Standard library imports

from typing import Any
from io import StringIO

import sys

# Local application/library specific imports

import terminalcolorpy as tcp


class Teststdout(object):
    def __init__(self) -> None:
        self.printed: list[Any] = []

    def write(self, string) -> None:
        self.printed.append(string)


def test_flixtext() -> None:
    assert (
        tcp.flip_text(
            r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        )
        == r"""ɐqɔpǝɟƃɥᴉɾʞꞁɯuodbɹsʇnʌʍxʎzⱯᗺƆᗡƎᖵ⅁HIᒋ⋊ꞀWNOԀꝹᴚS⊥∩ɅMX⅄Z0ІᘔƐᔭ59Ɫ86¡„#$%⅋,)(*+'-˙/:؛>=<¿@]\[ᵥ‾`}|{~"""[
            ::-1
        ]
    )


def test_prainbow() -> None:
    assert len(tcp.prainbow("gay")) != 3


def test_blink() -> None:
    before = sys.stdout
    sys.stdout = Teststdout()  # type: ignore

    tcp.blink("wee")

    if not len(sys.stdout.printed):  # type: ignore
        sys.stdout = before
        raise AssertionError("nothing printed to stdout")

    sys.stdout = before


def test_printcolor() -> None:
    before = sys.stdout
    sys.stdout = Teststdout()  # type: ignore

    tcp.printcolor({"text": "hello", "color": "red"}, flush=False)

    if not len(sys.stdout.printed):  # type: ignore
        sys.stdout = before
        raise AssertionError("nothing printed to stdout")

    sys.stdout = before


def test_colored() -> None:
    assert (
        tcp.colored(
            text="wee",
            color="red",
            markup=["striked", "framed", "bold", "underline", "italic"],
            highlight="blue",
        )
        == "\x1b[91m\x1b[44m\x1b[9m\x1b[52m\x1b[1m\x1b[4m\x1b[3mwee\x1b[0m"
    )

    assert (
        tcp.colored(
            text="woo",
            color=[122, 122, 0],
            markup=["striked", "framed", "bold", "underline", "italic"],
            highlight=[111, 5, 0],
        )
        == "\x1b[38;2;122;122;0m\x1b[48;2;111;5;0m\x1b[9m\x1b[52m\x1b[1m\x1b[4m\x1b[3mwoo\x1b[0m"
    )

    assert (
        tcp.colored(
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
        )
        == "\x1b[38;2;0;0;0m\x1b[48;2;0;191;255m\x1b[9m\x1b[52m\x1b[1m\x1b[4m\x1b[3m!\x1b[0m"
    )
