from commands.command import Command

class UndoCommand(Command):

    def execute(self):
        self.list_receiver.load_backup()
        self.builder_receiver.build_wallpaper()
        self.builder_receiver.set_wallpaper()
        print('Loaded the todo list backup for ya! ;p')
    
    def unexecute(self):
        pass