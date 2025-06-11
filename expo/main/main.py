from ursina import *
import subprocess
from sys import exit


def main_menu():
    def start_singleplayer():
        print("Starting Singleplayer Game!")
        #destroy(singleplayer_button)
        #destroy(options_button)
        #destroy(quit_button)
        #destroy(background_panel) # Destroy the panorama

        # Load game scene
        #EditorCamera()

        subprocess.Popen(["python", "../example/UrsaCraft_video.py"])
        

    def open_options():
        print("Opening Options!")
        subprocess.Popen(["python", "options.py"])

    def quit_game():
        print("Quitting Game!")
        application.quit()

    button_y_start = 0.1
    button_spacing = 0.1

    singleplayer_button = Button(text="Start Game",
                                 scale=(0.3, 0.07),
                                 y=button_y_start,
                                 on_click=start_singleplayer,
                                 color=color.azure,
                                 highlight_color=color.gold)

    options_button = Button(text="Help",
                            scale=(0.3, 0.07),
                            y=button_y_start - (button_spacing * 2),
                            on_click=open_options,
                            color=color.azure,
                            highlight_color=color.gold)

    quit_button = Button(text="Quit Game",
                         scale=(0.3, 0.07),
                         y=button_y_start - (button_spacing * 3),
                         on_click=quit_game,
                         color=color.red,
                         highlight_color=color.gold)

    background_panel = Entity(model='quad', scale_x=camera.aspect_ratio, scale_y=1,
                              texture='assets_main/back_ground.png',
                              parent=camera.ui, z=1) # Render behind UI elements

    # Simple animation for the background
    # We'll just shift the texture coordinates slightly over time
    def update():
        # This will simulate a slow panning effect on the background texture
        background_panel.texture_offset = (background_panel.texture_offset[0] + time.dt * 0.005, 0)
        # Wrap around to keep it continuous
        if background_panel.texture_offset[0] > 1:
            background_panel.texture_offset = (background_panel.texture_offset[0] - 1, 0)

    def update():
        if held_keys["escape"]: application.quit()


if __name__ == '__main__':
    app = Ursina()
    main_menu()
    app.run()