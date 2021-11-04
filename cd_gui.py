import PySimpleGUI as sg
import os 
from json_read_write import *

config_dirs = []

def check_dirs():

  global config_dirs

  print("*** check directories *** ")
  print(" before", config_dirs)

  for i in config_dirs[:]:
    exist = os.path.exists(i)

    if not exist:
      config_dirs.remove(i)

  print(" after", config_dirs)

def read_dirs():

  global config_dirs

  f_name = "config.json"
  data = read_json_file(f_name)
  config_dirs = data["directories"]
  print("read dirs", config_dirs)

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text('ここは1行目')],
            [sg.Text('ここは2行目：適当に文字を入力してください'), sg.InputText()],
            [sg.Button('OK'), sg.Button('add'), sg.Button('Kill all')] ]

# ウィンドウの生成
window = sg.Window('サンプルプログラム', layout)

read_dirs()
check_dirs()

direcotry1 = config_dirs[0]

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

