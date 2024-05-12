import pyfiglet
from termcolor import colored
import random

def get_random_font_style():
    # List of available Figlet font styles
    font_styles = pyfiglet.FigletFont.getFonts()
    # Choose a random font style from the list
    return random.choice(font_styles)

def get_random_color():
    # List of available colors
    colors = ["red", "green", "yellow", "blue", "magenta", "chartreuse", "cyan", "white"]
    # Chose a random color from the list
    return random.choice(colors)

def wish_mothers_day():
    # Get a random font style and color
    random_font_style = get_random_font_style()
    random_color = get_random_color()
    # Create a Figlet font object with the random style
    font = pyfiglet.Figlet(font=random_font_style)
    # Print the decorative greeting in the chosen color
    print(colored(font.renderText("Happy Mother's Day!"), random_color))

wish_mothers_day()