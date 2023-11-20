from commands.command import Command

class EditCommand(Command):

    def execute(self):
        """
        Edit the indexed todo for a strikethrough
        """
        self.list_receiver.write_backup()
        self.list_receiver.edit_todo()
        self.builder_receiver.build_wallpaper()
        self.builder_receiver.set_wallpaper()
        print('Edited that for ya ;)')
    
    def unexecute(self):
        pass