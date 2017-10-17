
"""
POSH : Parts of Speach Heuristics

"""
from __future__ import absolute_import  # noqa
from .session import Session  # noqa
from . import system_setup


def setup(download=True):
    system_setup.full_setup(download)
