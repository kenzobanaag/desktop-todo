import ctypes
import constants

from PIL import Image, ImageDraw, ImageFont
from receiver.receiver import Receiver

class WallpaperBuilder(Receiver):

    EMPTY_PATH = constants.SRC_PATH + constants.EMPTY_BG_IMG_FILENAME
    TODO_PATH = constants.SRC_PATH + constants.TODO_BG_IMG_FILENAME

    def __init__(self, args) -> None:
        super().__init__(args)
        
        self.image_path = WallpaperBuilder.EMPTY_PATH if args.command.lower() == 'cls' else WallpaperBuilder.TODO_PATH
            
    def build_wallpaper(self):
        background = Image.new('RGB', (constants.WIDTH, constants.HEIGHT), color='black')

        font = ImageFont.truetype("arial.ttf", constants.FONT_SIZE)
        line_height = font.getlength("A")

        draw = ImageDraw.Draw(background)

        text_widths = []
        text_height = 0
        lines = []

        with open(constants.TODO_FILEPATH, 'r') as file:
            for line in file:
                text = line.strip()[constants.DELIMETER_LENGTH_INDEX:]
                text_length = draw.textlength(text, font=font)
                text_widths.append(text_length)
                text_height += line_height
                lines.append(line)

        # This is where we know that theres nothing inside the file
        if not lines: # Stop the program from erroring when theres nothing on the list
            self.image_path = WallpaperBuilder.EMPTY_PATH
            return

        max_text_width = max(text_widths)

        # Calculate text position in the center
        x = (constants.WIDTH - max_text_width) / 2  # Center align horizontally
        y = (constants.HEIGHT - text_height) / 2    # Center align vertically

        for line in lines:
            is_done = int(line[0]) # 1 = done | 0 = todo  
            text = line.strip()[constants.DELIMETER_LENGTH_INDEX:]
            color = constants.VALID_COLORS[int(line[constants.COLOR_INDEX])]
            text_length = draw.textlength(text, font=font)
            draw.text((x, y), text, fill=color, font=font)
            if is_done == constants.DONE:
                draw.line((x, y+line_height, x + text_length, y+line_height), fill=color, width=2)
            y += line_height + constants.PADDING_TOP # Move to the next line

        # TODO: Fix this. If you run this outside the directory, it saves it where you ran it.
        background.save(constants.TODO_BG_IMG_FILENAME[1:])

    def set_wallpaper(self):
        """
        Set the desktop wallpaper using ctypes
        """
        image_path = self.image_path

        # SPI_SETDESKWALLPAPER code
        SPI_SETDESKWALLPAPER = 20

        # Update the wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)