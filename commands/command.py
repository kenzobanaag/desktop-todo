"""
This is an interface for command
"""
from abc import abstractmethod
from receiver.receiver import Receiver
from receiver.list import List
from receiver.wallpaper_builder import WallpaperBuilder

class Command:
    def __init__(self, list : Receiver, builder : Receiver):
        """
        NOTE: Ideally list and builder should be their own interfaces that are type receiver.
              That is something you can add in the future, if you want to handle different types
              of lists.
        """
        self.list_receiver : List = list
        self.builder_receiver : WallpaperBuilder = builder

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass