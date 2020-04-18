COLOUR_HEX = {"blue1": "#0000ff", "chartreuse1": "#7fff00", "burlywood3": "#cdaa7d", "cyan1": "#00ffff",
              "DarkOrchid": "#9932cc",
              "DodgerBlue1": "#1e90ff", "firebrick1": "#ff3030", "gold1": "#ffd700", "green1": "#00ff00",
              "HotPink": "#ff69b4",
              "IndianRed1": "#ff6a6a", "ivory1": "#fffff0", "khaki": "#f0e68c", "beige": "#f5f5dc",
              "bisque1": "#ffe4c4"}
COLOUR_NAME = input("Enter a colour: ")

while COLOUR_NAME != "":
    print("The code for \"{}\" is {}".format(COLOUR_NAME, COLOUR_HEX.get(COLOUR_NAME)))
    COLOUR_NAME = input("Enter a colour name: ")
