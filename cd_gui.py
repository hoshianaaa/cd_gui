import PySimpleGUI as sg
import os 
from json_read_write import *

dirs = []

def check_dirs():

  global dirs

  print("*** check directories *** ")
  print(" before", dirs)

  for i in dirs[:]:
    
    if not os.path.exists(i):
      dirs.remove(i)

  print(" after", dirs)

def read_dirs():

  global dirs

  f_name = "config.json"
  data = read_json_file(f_name)
  dirs = data["directories"]
  print("read dirs", dirs)

def add_dirs(directory):

  global dirs

  if(os.path.exists(directory)):
    dirs.append(directory)
    return True
  else:
    return False
    






sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text('ここは1行目')],
            [sg.Text('ここは2行目：適当に文字を入力してください'), sg.InputText()],
            [sg.Button('OK'), sg.Button('add'), sg.Button('Kill all')] ]

# ウィンドウの生成
window = sg.Window('サンプルプログラム', layout)

read_dirs()
check_dirs()

direcotry1 = dirs[0]

# イベントループ
while True:

    print('あなたが入力した値： ', )
    event, values = window.read()
    if event == 'Kill all':
        print("kill all")
        os.system('killall gnome-terminal-server')
        #break

    elif event == 'OK':
        #d = values[0]
        d = direcotry1
        print("directory",d)
        os.system('gnome-terminal -- bash -c "cd %s; bash"' % d)

    elif event == sg.WIN_CLOSED:
        break

window.close()

