from receiver.receiver import Receiver

import constants

class List(Receiver):

    def __init__(self, args) -> None:
        super().__init__(args)

    def add_todo(self):
        """
        Its obvious what this does...
        """
        with open(constants.TODO_FILEPATH, 'r') as file:
            file_contents = file.read()

        todo_length = 0
        for index, line in enumerate(file_contents.split('\n')):
            todo_length = index + 2
            if index == 0:
                first_todo_length = len(line)
                if first_todo_length == 0:
                    todo_length -= 1

        with open(constants.TODO_FILEPATH, 'a') as dest_file:
            # Write the content to the destination file
            content = '' if first_todo_length == 0 else '\n'
            color_index = 0
            if self.args.c in constants.VALID_COLORS:
                for index, color in enumerate(constants.VALID_COLORS):
                    if color == self.args.c:
                        color_index = index

            content += f'{constants.TODO} {constants.DELIMETER} {color_index} {constants.DELIMETER} {todo_length}. {self.args.text}'
            dest_file.write(content)

    def _check_index(self):
        if self.args.i == None: 
            raise Exception("Index required for this operation, type -h for help")
        
        if int(self.args.i) <= 0:
            raise Exception("Index is invalid, must be bigger than 0")

    def edit_todo(self):
        self._check_index()

        with open(constants.TODO_FILEPATH, 'r') as source_file:
            # Read the content of the source file
            content = source_file.read()

        new_content = ''
        index = int(self.args.i) - 1

        contents = content.split('\n')
        if index > len(contents)-1:
            raise Exception('Index passed is bigger than todo list length')

        for idx, line in enumerate(contents):
            if index == idx:
                if self.args.c != None and self.args.c in constants.VALID_COLORS:
                    for color_arr_idx, color in enumerate(constants.VALID_COLORS):
                        if color == self.args.c:
                            color_index = color_arr_idx
                else:
                    color_index = int(line[constants.COLOR_INDEX])
                text = line[constants.DELIMETER_LENGTH_INDEX+4:] if self.args.text.strip() == '' else self.args.text
                line = f'0 {constants.DELIMETER} {color_index} {constants.DELIMETER} {index+1}. {text}'
            new_content += f'{line}\n'
            
        with open(constants.TODO_FILEPATH, 'w') as dest_file:
            # Write the content to the destination file
            dest_file.write(new_content[0:-1])

    def done_todo(self):
        """
        Should probably reuse todo? Or does edit todo only change color and text, and probably also done?
        """
        self._check_index()
       
        with open(constants.TODO_FILEPATH, 'r') as source_file:
            # Read the content of the source file
            content = source_file.read()

        new_content = ''
        index = int(self.args.i) - 1
        contents = content.split('\n')
        if index > len(contents)-1:
            raise Exception('Index passed is bigger than todo list length')

        for idx, line in enumerate(contents):
            if index == idx:
                line = f'1{line[1:]}'
            new_content += f'{line}\n'
            
        with open(constants.TODO_FILEPATH, 'w') as dest_file:
            # Write the content to the destination file
            dest_file.write(new_content[0:-1])

    def remove_todo(self):
        self._check_index()

        with open(constants.TODO_FILEPATH, 'r') as source_file:
            # Read the content of the source file
            content = source_file.read()

        new_content = ''
        index = int(self.args.i) - 1
        contents = content.split('\n')
        if index > len(contents)-1:
            raise Exception('Index passed is bigger than todo list length')
        
        curr = 0
        for idx, line in enumerate(contents):
            if index != idx:
                curr += 1
                new_content += f'{line[0:constants.DELIMETER_LENGTH_INDEX]} {curr}. {line[constants.DELIMETER_LENGTH_INDEX+4:]}\n'

        with open(constants.TODO_FILEPATH, 'w') as dest_file:
            # Write the content to the destination file
            dest_file.write(new_content[0:-1])

    def clear_todos(self):
        """
        Clear todo.txt
        Set clear background, default = Black, can also set to different color on the other command
        """
        self.write_backup()

        # Empty the todo list
        with open(constants.TODO_FILEPATH, 'w') as source_file:
            # Write the content to the destination file
            source_file.write('')

    def load_backup(self):
        """
        Load the backup file
        """
        with open(constants.TODO_BACKUP, 'r') as source_file:
            # Read the content of the source file
            content = source_file.read()

        with open(constants.TODO_FILEPATH, 'w') as dest_file:
            # Write the content to the destination file
            dest_file.write(content)

    def write_backup(self):
        """
        Copy the current todo list to the backup so we can undo
        """
        with open(constants.TODO_FILEPATH, 'r') as source_file:
            # Read the content of the source file
            content = source_file.read()

        with open(constants.TODO_BACKUP, 'w') as dest_file:
            # Write the content to the destination file
            dest_file.write(content)