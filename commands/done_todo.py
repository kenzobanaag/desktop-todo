from commands.command import Command

class DoneCommand(Command):

    def execute(self):
        """
        Edit the indexed todo for a strikethrough
        """
        self.list_receiver.write_backup()
        self.list_receiver.done_todo()
        self.builder_receiver.build_wallpaper()
        self.builder_receiver.set_wallpaper()
        print('Set that to done for ya ;)')
    
    def unexecute(self):
        pass