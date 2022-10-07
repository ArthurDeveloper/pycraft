from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

game = Ursina()
window.fullscreen = True

current_block_color = color.white

class Block(Button):
    def __init__(self, position):
        super().__init__(           
            parent=scene,
            model='cube',
            color=current_block_color,
            position=position,
            shader=lit_with_shadows_shader
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
            elif key == 'right mouse down':
                new_block = Block(position=self.position + mouse.normal)


def generate_blocks():
    for z in range(20):
        for x in range(20):
            Block(position = (x, 0, z))

def change_current_block_color_on_key_press(key, new_color):
    global current_block_color
    if held_keys[key]:
        current_block_color = new_color


generate_blocks()

player = FirstPersonController()
player.speed = 10
player.gravity = 0

def update():
    fly_speed = 20
    if held_keys['space']:
        player.y += fly_speed * time.dt
    elif held_keys['control']:
        player.y -= fly_speed * time.dt

    for i, new_color in enumerate([color.white, color.green, color.red, color.blue, color.yellow, color.black, color.magenta, color.brown]):
        change_current_block_color_on_key_press(str(i+1), new_color)

pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, 45, 45))
game.run()
