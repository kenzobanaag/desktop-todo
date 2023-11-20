from commands.command import Command

class ClearBackgroundCommand(Command):
    
    def execute(self):
        self.list_receiver.clear_todos()
        self.builder_receiver.set_wallpaper()
        print('Cleared the background for ya! ;)')

    def unexecute(self):
        """
        How do you unclear? Just run the current file again, but the list will be clear...

        For this to work, you need a memento pattern that kind of stores the previous state,
        this is something that we can implement in the future, and not now
        """
        pass