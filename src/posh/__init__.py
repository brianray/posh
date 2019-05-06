from .session import Session
from . import system_setup


def setup(download=True):
	system_setup.full_setup(download)
