from ursina import *
from sys import exit


app = Ursina()

def exit_options():
    application.quit()

button_y_start = 0.1
button_spacing = 0.1

title = Button(text="HELP MENU",
               scale=(0.3,0.07),
               y=button_y_start + (button_spacing * 3),
               color=color.light_gray)

movement = Button(text="MOVEMENT: WASD",
                             scale=(0.3, 0.07),
                             y=button_y_start,
                             color=color.azure)

jump = Button(text="JUMP: SPACE",
                            scale=(0.3, 0.07),
                            y=button_y_start - (button_spacing * 2),
                            color=color.azure)

block = Button(text="1: GRASS 2: DIRT 3: STONE 4: BRICK",
                         scale=((0.3 * 1.5), 0.07),
                         y=button_y_start - (button_spacing * 3),
                         color=color.azure)

exit_button = Button(text="EXIT HELP MENU",
                     scale=(0.3,0.07),
                     y=button_y_start - (button_spacing * 4),
                     on_click=exit_options,
                     color = color.red)

background_panel = Entity(model='quad', scale_x=camera.aspect_ratio, scale_y=1,
                              texture='assets_main/back_ground.png',
                              parent=camera.ui, z=1) # Render behind UI elements


app.run()