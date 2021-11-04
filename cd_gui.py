import PySimpleGUI as sg
import os 
from json_read_write import *

dirs = []

def check_dirs():

  global dirs

  for i in dirs[:]:
    
    if not os.path.exists(i):
      dirs.remove(i)

def read_dirs():

  global dirs

  f_name = "config.json"
  data = read_json_file(f_name)
  dirs = data["directories"]

def add_dirs(directory):

  global dirs

  if(os.path.exists(directory)):
    dirs.append(directory)
    return True
  else:
    return False



sg.theme('DarkAmber')

layout = [  [sg.Text('ここは1行目')],
            [sg.Text('ここは2行目：適当に文字を入力してください'), sg.InputText()],
            [sg.Button('OK'), sg.Button('add'), sg.Button('Kill all')] ]

window = sg.Window('サンプルプログラム', layout)

read_dirs()
check_dirs()

direcotry1 = dirs[0]

while True:

    event, values = window.read()
    if event == 'Kill all':
        os.system('killall gnome-terminal-server')

    elif event == 'OK':
        d = direcotry1
        os.system('gnome-terminal -- bash -c "cd %s; bash"' % d)

    elif event == sg.WIN_CLOSED:
        break

window.close()

