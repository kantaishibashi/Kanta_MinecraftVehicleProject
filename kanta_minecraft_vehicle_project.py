from mcpi.minecraft import Minecraft
from time import sleep
from pynput import keyboard

mc = Minecraft.create()
#prepare_site(mc, 32, 40, 41, is_player_teleport=True)

START_X = 0
START_Y = 0
START_Z = 0

AIR_ID = 0
WOOL_ID = 35
GRAY_WOOL_DATA = 7
QUARTZ_ID = 155
STONE_SLAB_DATA = 44

mode = "west"

def vehicle_east(mc, x, y, z):
    # car
    coordslayer = [
        [[0, 0], [44, 8], [0, 0]],
        [[43, 6], [109, 1], [43, 6]],
        [[44, 8], [44, 0], [44, 8]],
        [[44, 8], [44, 0], [44, 8]],
        [[44, 0], [44, 8], [44, 0]]
    ]

    coordslayer2 = [
        [[0, 0], [43, 6], [0, 0]],
        [[44, 7], [0, 0], [44, 6]],
        [[0, 0], [0, 0], [0, 0]],
        [[0, 0], [20, 0], [0, 0]]
    ]

    coordslayer3 = [
        [[0, 0], [43, 6], [0, 0]],
        [[0, 0], [44, 8], [0, 0]]
    ]

    #eastmode
    if mode == "east":
        for coords_xnum, coords_x in enumerate(coordslayer):
            for coords_znum, coords_z in enumerate(coords_x, 1):
                # print(coords_xnum, coords_znum, coords_z)
                # print(coords_xnum + x,  coords_znum, *coords_z)
                mc.setBlock(x + coords_xnum, y, z + coords_znum, *coords_z)

        for coords2_xnum, coords2_x in enumerate(coordslayer2):
            for coords2_znum, coords2_z in enumerate(coords2_x, 1):
                mc.setBlock(x + coords2_xnum, y + 1, z + coords2_znum, *coords2_z)

        for coords3_xnum, coords3_x in enumerate(coordslayer3):
            for coords3_znum, coords3_z in enumerate(coords3_x, 1):
                mc.setBlock(x + coords3_xnum, y + 2, z + coords3_znum, *coords3_z)

        # ladders
        mc.setBlock(x + 1, y, z, 65, 1)
        mc.setBlock(x + 1, y, z + 4, 65, 3)

        #wheels
        for x_width in [0, 5]:
            for y_height in [0]:
                for z_length in [0, 4]:
                    mc.setBlock(x + x_width, y + y_height, z +z_length, WOOL_ID, GRAY_WOOL_DATA)

    if mode == "south":
        for coords_znum, coords_z in enumerate(coordslayer):
            for coords_xnum, coords_x in enumerate(coords_z, 1):
                mc.setBlock(x + coords_xnum, y, z + coords_znum, *coords_x)

        for coords2_znum, coords2_z in enumerate(coordslayer2):
            for coords2_xnum, coords2_x in enumerate(coords2_z, 1):
                mc.setBlock(x + coords2_xnum, y + 1, z + coords2_znum, *coords2_x)

        for coords3_znum, coords3_z in enumerate(coordslayer3):
            for coords3_xnum, coords3_x in enumerate(coords3_z, 1):
                mc.setBlock(x + coords3_xnum, y + 2, z + coords3_znum, *coords3_x)

        #ladders
        #mc.setBlock(x + 4, y, z + 1, 65, 2) (なぜか向きが北向き強制)
        mc.setBlock(x, y, z + 1, 65, 4)

        #wheelsタイヤが一つない
        #wheels
        for x_width in [0, 4]:
            for y_height in [0]:
                for z_length in [0, 5]:
                    mc.setBlock(x + x_width, y + y_height, z +z_length, WOOL_ID, GRAY_WOOL_DATA)

    if mode == "west":
        for coords_xnum, coords_x in enumerate(coordslayer):
            for coords_znum, coords_z in enumerate(coords_x, 1):
                mc.setBlock(x - coords_xnum, y, z - coords_znum, *coords_z)

        for coords2_xnum, coords2_x in enumerate(coordslayer2):
            for coords2_znum, coords2_z in enumerate(coords2_x, 1):
                mc.setBlock(x - coords2_xnum, y + 1, z - coords2_znum, *coords2_z)

        for coords3_xnum, coords3_x in enumerate(coordslayer3):
            for coords3_znum, coords3_z in enumerate(coords3_x, 1):
                mc.setBlock(x - coords3_xnum, y + 2, z - coords3_znum, *coords3_z)

def make_car_east():
    pos = mc.player.getTilePos()
    vehicle_east(mc, pos.x - 2, pos.y, pos.z - 2)
    mc.player.setTilePos(pos.x, pos.y + 1, pos.z)

def delete_back(coordsx, coordsy, coordsz):
    pos = mc.player.getTilePos()
    print(pos)
    for i in range(len(coordsx)):
        mc.setBlock(pos.x + coordsx[i] , pos.y + coordsy[i] - 1, pos.z + coordsz[i], AIR_ID)

def on_press(key):
    #row below debug
    print(f'Key pressed: {key}')
    pos = mc.player.getTilePos()

    if str(key) == "Key.esc":
        return

    if key.char == 't':
        exit()

    if mode == "east":
        if key.char == 'w':
        #if mode == 0:
            coordsfx = [2, 2, -3, -3, -3, -3, -3]
            coordsfy = [0, 0, 0, 0, 0, 1, 2]
            coordsfz = [2, -2, 2, 0, -2, 0, 0]
            mc.player.setTilePos(pos.x +1, pos.y, pos.z) #X+1
            make_car_east()
            delete_back(coordsfx,coordsfy,coordsfz)

        if key.char == 's':
            coordsbx = [4, 4, 3, 3, 3, 2, 0]
            coordsby = [0, 0, 0, 0, 0, 1, 2]
            coordsbz = [2, -2, 1, 0, -1, 0, 0]
            mc.player.setTilePos(pos.x -1, pos.y, pos.z) #x-1
            make_car_east()
            delete_back(coordsbx,coordsby,coordsbz)

        if key.char == 'a':
            coordslx = [3, 3, 2, 1, 0, -2, -1]
            coordsly = [0, 0, 0, 0, 0, 0, 1]
            coordslz = [-1, 3, 2, 2, 2, 3, -2]
            mc.player.setTilePos(pos.x, pos.y, pos.z -1) #z-1
            make_car_east()
            delete_back(coordslx,coordsly,coordslz)

        if key.char == 'd':
            coordsrx = [3, 3, 2, 1, 0, -2, -1]
            coordsry = [0, 0, 0, 0, 0, 0, 1]
            coordsrz = [1, -3, -2, -2, -2, -3, -2]
            mc.player.setTilePos(pos.x, pos.y, pos.z +1) #z+1
            make_car_east()
            delete_back(coordsrx,coordsry,coordsrz)

    if mode == "south":
        if key.char == 'w':
            coordsfx = [2, -2, 2, 0, -2, 0, 0]
            coordsfy = [0, 0, 0, 0, 0, 1, 2]
            coordsfz = [2, 2, -3, -3, -3, -3, -3]
            mc.player.setTilePos(pos.x, pos.y, pos.z +1) #z+1
            make_car_east()
            delete_back(coordsfx,coordsfy,coordsfz)

        if key.char == 's':
            coordsbx = [2, -2, 1, 0, -1, 0, 0, +2]
            coordsby = [0, 0, 0, 0, 0, 1, 2, 0]
            coordsbz = [4, 4, 3, 3, 3, 2, 0, -1] #2, 0, -1ははしごがおかれないから置いてるだけ。
            mc.player.setTilePos(pos.x, pos.y, pos.z - 1) #z-1
            make_car_east()
            delete_back(coordsbx,coordsby,coordsbz)

        if key.char == 'a':
            coordslx = [-2, -2, -2, -2, -3, +1, -3]
            coordsly = [0, 0, 0, 1, 0, 0, 0]
            coordslz = [0, 1, 2, -1, +3, +3, -2]
            mc.player.setTilePos(pos.x +1, pos.y, pos.z) #x +1
            make_car_east()
            delete_back(coordslx,coordsly,coordslz)

        if key.char == 'd': #2, 0, -1ははしごがおかれないから置いてるだけ。
            coordsrx = [2, 2, 2, 2, 3, 3, 2, -1]
            coordsry = [0, 0, 0, 1, 0, 0, 0, 0]
            coordsrz = [0, 1, 2, -1, 3, -2, -1, 3]
            mc.player.setTilePos(pos.x - 1, pos.y, pos.z) #x-1
            make_car_east()
            delete_back(coordsrx,coordsry,coordsrz)

    if mode == "west":
        if key.char == 'w':
            mc.player.setTilePos(pos.x -1, pos.y, pos.z) #X+1
            make_car_east()



#    if key.char == "o":
#        mode = higasi

#    if key.char == "p":

    if key.char == ",":
        return False  # ,キーが押されたらリスナーを停止

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


#メモ
#south 向きのモードの消すコード、前、後、右 を作る。
#他の方向も作る




# def road():

#前に進み続けるだけのプログラム
#def repeat():
#    pos = mc.player.getTilePos()
#    mc.player.setTilePos(pos.x +1, pos.y, pos.z)
#    makecar()
#    deleteback()
#    sleep(0.5)

#一回車を作るだけ
#def dontrepeat():
#    pos = mc.player.getTilePos()
#    mc.player.setTilePos(pos.x +1, pos.y, pos.z)
#    makecar()
#    deleteback()

#while True:
#    repeat()



#kesu block
#playerpos + (2, 0, -2), (2, 0, 2), (-3, 0, -2), (-3, 0, 2), (-3, 0, 0), (-3, 1, 0), (-3, 2, 0)

#    coords = mc.player.getTilePos()
#    AirblockCoords = [[2, 0, -2], [2, 0, 2],[-2, 0, -1], [-3, 0, -2], [-2, 0, 1], [-3, 0, 2], [0, 1, 0],[-3, 1, 0], [-3, 1, -1], [-3, 1, 1], [-3, 3, 0]]
#    for i,pos in enumerate(AirblockCoords):
#        mc.setBlock(coords.x + pos[0], coords.y + pos[1], coords.z + pos[2], AIR_ID)

#while True:
#    carrepeat()

# carrepeat()
