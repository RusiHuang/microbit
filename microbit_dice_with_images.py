from microbit import *
import random
import music
numbers = [Image('00000:'
                 '00900:'
                 '00900:'
                 '00900:'
                 '00900:'),
          Image('09900:'
                '90090:'
                '00900:'
                '09000:'
                '99990:'),
          Image('00999:'
                '00009:'
                '00999:'
                '00009:'
                '00999:'),
          Image('90090:'
                '90090:'
                '99990:'
                '00090:'
                '00090:'),
          Image('09990:'
                '90000:'
                '09900:'
                '00090:'
                '99900:'),
          Image('99990:'
                '90000:'
                '99990:'
                '90090:'
                '99990:')]
GREENSLEEVES = ['A:2', 'C5:4', 'D:2', 'E:3', 'F:1', 'E:2', 'D:4', 'B4:2', 'G:3', 'A:1', 'B:2', 'C5:4', 'A4:2', 'A:3', 'G#:1', 'A:2', 'B:4', 'G#:2', 'E:4', 'A:2', 'C5:4', 'D:2', 'E:3', 'F:1', 'E:2', 'D:4', 'B4:2', 'G:3', 'A:1', 'B:2', 'C5:3', 'B4:1', 'A:2', 'G#:3', 'F#:1', 'G#:2', 'A:4', 'A:2', 'A:6']
POP_WEASEL = ['G:2', 'G:1', 'A:2', 'A:1', 'B', 'D5', 'B4', 'G:3', 'G:2', 'G:1', 'A:2', 'A:1', 'B:3', 'G', 'G:2', 'G:1', 'A:2', 'A:1', 'B', 'D5', 'B4', 'G:3', 'E5:3', 'A4:2', 'C5:1', 'B4:3', 'G']
BLUE_DANUBE = ['C4:2', 'E', 'G', 'G', 'R', 'G5', 'G', 'R', 'E', 'E', 'R', 'C4', 'C', 'E', 'G', 'G', 'R', 'G5', 'G', 'R', 'F', 'F', 'R', 'B3', 'B', 'D4', 'A', 'A', 'R', 'A5', 'A', 'R', 'F', 'F', 'R', 'B3']

pieces  =[GREENSLEEVES, POP_WEASEL, BLUE_DANUBE]
while True:
  if accelerometer.was_gesture('shake'):
    display.show(random.choice(numbers))
    music.play(random.choice(pieces), wait=False, loop=False)


