from commands.command import Command


class RemoveTodoCommand(Command):
    
    def execute(self):
        """
        Remove todo in specified index
        """
        self.list_receiver.write_backup()
        self.list_receiver.remove_todo()
        self.builder_receiver.build_wallpaper()
        self.builder_receiver.set_wallpaper()
        print('Removed that for ya!')

    def unexecute(self):
        """
        Im not going to implement this yet
        """
        pass
    
