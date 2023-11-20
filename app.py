import argparse
import constants

from commands.command import Command
from commands.add_todo import AddTodoCommand
from commands.clear_bg import ClearBackgroundCommand
from commands.undo_todo import UndoCommand as UndoTodoCommand
from commands.done_todo import DoneCommand as DoneTodoCommand
from commands.edit_todo import EditCommand as EditTodoCommand
from commands.remove_todo import RemoveTodoCommand
from receiver.list import List
from receiver.wallpaper_builder import WallpaperBuilder

def get_command(command) -> Command:
    match command:
        case 'ADD': return AddTodoCommand
        case 'CLS': return ClearBackgroundCommand
        case 'UNDO': return UndoTodoCommand
        case 'DONE': return DoneTodoCommand
        case 'EDIT': return EditTodoCommand
        case 'RM': return RemoveTodoCommand
        case _:
            raise Exception('That command is not supported')

if __name__ == '__main__':
    # Creating a parser
    parser = argparse.ArgumentParser(description=constants.SCRIPT_DESC)

    # Adding arguments
    parser.add_argument('command', type=str, help=constants.COMMAND_DESC)
    parser.add_argument('text', type=str, help=constants.TEXT_DESC)
    parser.add_argument('-i', type=int, help=constants.INDEX_DESC)
    parser.add_argument('-c', type=str, help=constants.COLOR_DESC)

    # Parsing arguments
    args = parser.parse_args()

    command : Command = get_command(args.command.upper())(List(args), WallpaperBuilder(args))
    command.execute()