"""
Interface of the receiver
"""
import argparse

class Receiver():
    def __init__(self, args : argparse.ArgumentParser) -> None:
        self.args : argparse.ArgumentParser = args