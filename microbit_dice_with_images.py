from microbit import *
import random
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
while True:
  if button_a.was_pressed():
    for i in range(5):
      display.show(random.choice(numbers))
      sleep(750)
      