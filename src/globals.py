from math import exp
from airtest.core.cv import Template
from numpy import choose

DEVICES = {"acc0": "Android://127.0.0.1:5037/emulator-5554",
           "acc1": "Android://127.0.0.1:5037/emulator-5556",
           "acc2": "Android://127.0.0.1:5037/emulator-5558",
           "acc3": "Android://127.0.0.1:5037/emulator-5560"}
DEVICES_NAMES = ['主号', '副号1', '副号2', '副号3']
MAP_TRANSLATE = {"训练": "Training", "重复": "Repeat", "塔": "Tower", "神殿": "Temple"}

passOk=Template(r"screenshot/pass_ok.png", record_pos=(0.0, 0.27), resolution=(400, 700))
resultOk=Template(r"screenshot/result_ok.png", record_pos=(0.0, 0.802), resolution=(400, 700))
Initial=Template(r"screenshot/home.png", record_pos=(-0.415, 0.802), resolution=(400, 700))
Adventure=Template(r"screenshot/adventure.png", record_pos=(-0.003, 0.23), resolution=(400, 700))
Grow=Template(r"screenshot/grow.png", record_pos=(-0.242, 0.203), resolution=(400, 700))
Join=Template(r"screenshot/join.png", record_pos=(0.328, 0.535), resolution=(400, 700))
Training=Template(r"screenshot/training.png", record_pos=(0.005, -0.142), resolution=(400, 700))
Back=Template(r"screenshot/back.png", record_pos=(-0.42, -0.492), resolution=(400, 700))
Exp_exist=Template(r"screenshot/exp_exist.png", record_pos=(-0.31, 0.422), resolution=(400, 700), threshold=0.5)
Exp_stage=Template(r"screenshot/exp_stage.png", record_pos=(-0.228, -0.098), resolution=(400, 700))
multi_player = Template(r"screenshot/multi_player.png", record_pos=(0.228, 0.04), resolution=(400, 700))
single_player = Template(r"screenshot/single_player.png", record_pos=(-0.228, 0.04), resolution=(400, 700))
with_friends = Template(r"screenshot/with_friends.png", record_pos=(-0.33, 0.04), resolution=(400, 700))
new_stage = Template(r"screenshot/new_stage.png", record_pos=(-0.355, 0.163), resolution=(400, 700))
start_point = Template(r"screenshot/start_point.png", record_pos=(-0.335, 0.468), resolution=(400, 700), threshold=0.9)
Consume = Template(r"screenshot/consume.png", record_pos=(-0.383, 0.17), resolution=(400, 700))
Attack = Template(r"screenshot/attack.png", record_pos=(-0.005, 0.33), resolution=(400, 700))
Finished = Template(r"screenshot/finished.png", record_pos=(-0.385, 0.458), resolution=(400, 700))
Waiting = Template(r"screenshot/waiting.png", record_pos=(0.107, -0.13), resolution=(400, 700))
change_order = Template(r"screenshot/change_order.png", record_pos=(0.343, 0.625), resolution=(400, 700))
re_search = Template(r"screenshot/research.png", record_pos=(0.343, 0.625), resolution=(400, 700))
Searching = Template(r"screenshot/searching.png", record_pos=(0.343, 0.625), resolution=(400, 700))
not_search = Template(r"screenshot/not_search.png", record_pos=(0.343, 0.625), resolution=(400, 700))
room_exist = Template(r"screenshot/room_exist.png", record_pos=(-0.47, -0.28), resolution=(400, 700))
exit_join = Template(r"screenshot/exit_join.png", record_pos=(-0.47, -0.28), resolution=(400, 700))
short_cut = Template(r"screenshot/short_cut.png", record_pos=(-0.003, 0.403), resolution=(400, 700))
luck_max = Template(r"screenshot/luck_max.png", record_pos=(0.0, 0.045), resolution=(400, 700))
replace_helper = Template(r"screenshot/replace_helper.png", record_pos=(0.372, 0.095), resolution=(400, 700))
stage_over = Template(r"screenshot/stage_over.png", record_pos=(0.318, 0.105), resolution=(400, 700))
Resurrection = Template(r"screenshot/resurrection.png", record_pos=(0.037, 0.065), resolution=(400, 700))
Yes = Template(r"screenshot/yes.png", record_pos=(0.037, 0.065), resolution=(400, 700))
final_check = Template(r"screenshot/final_check.png", record_pos=(0.0, 0.0), resolution=(400, 700))
Temple = Template(r"screenshot/temple.png", record_pos=(-0.003, -0.128), resolution=(400, 700))
dark_temple = Template(r"screenshot/dark_temple.png", record_pos=(-0.22, 0.477), resolution=(400, 700))
time_temple_second = Template(r"screenshot/time_temple_second.png", record_pos=(-0.315, -0.065), resolution=(400, 700))
choose_fruit = Template(r"screenshot/choose_fruit.png", record_pos=(-0.323, -0.61), resolution=(400, 700))
choose_fruit_done = Template(r"screenshot/choose_fruit_done.png", record_pos=(-0.005, -0.122), resolution=(400, 700))
