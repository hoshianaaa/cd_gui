import PySimpleGUI as sg
import os 
from json_read_write import *

dirs = []

class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'

def printRed(text):
  print(pycolor.RED + text + pycolor.END)

def check_dirs():

  global dirs

  for i in dirs[:]:
    
    if not os.path.exists(i):
      dirs.remove(i)

def read_dirs():

  global dirs

  f_name = "config.json"
  data = read_json_file(f_name)
  dirs = data

def write_dirs():

  global dirs

  f_name = "config.json"
  write_json_file(f_name, dirs)

def add_dirs(directory):

  global dirs

  d = directory
  if(os.path.exists(d)):
    if not (d in dirs):
      dirs.append(directory)
      print("[Sucess] add exist directory:" + d)
      return True
    else:
      printRed("[Failed] Already exist directory: " + d)
      return False
  else:
    printRed("[Failed] No such a directory: " + d)
    return False

def buttons():
  list = []
  for i in dirs:
    list.append([sg.Button('Button')])

  return list

read_dirs()
check_dirs()

direcotry1 = dirs[0]

sg.theme('DarkAmber')

layout =  [  
            [sg.Text('Input directory: '), sg.InputText(), sg.Button('add')],
            buttons(),
            [sg.Button('Kill all')] 
          ]

window = sg.Window('サンプルプログラム', layout)

try:

  while True:

      event, values = window.read()
      if event == 'Kill all':
          os.system('killall gnome-terminal-server')

      elif event == 'open':
          d = direcotry1
          os.system('gnome-terminal -- bash -c "cd %s; bash"' % d)

      elif event == 'add':
          d = values[0]
          add_dirs(d)

      elif event == sg.WIN_CLOSED:
          break

  window.close()

finally:
  
  write_dirs()
  
  
