from commands.command import Command


class AddTodoCommand(Command):
    
    def execute(self):
        """
        Add to the list
        Build the image
        Set the wallpaper
        """
        self.list_receiver.write_backup()
        self.list_receiver.add_todo()
        self.builder_receiver.build_wallpaper()
        self.builder_receiver.set_wallpaper()
        print('Added that for ya!')

    def unexecute(self):
        """
        Im not going to implement this yet
        """
        pass
    
