import PySimpleGUI as sg
import os 
from json_read_write import *

config_dirs = None

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text('ここは1行目')],
            [sg.Text('ここは2行目：適当に文字を入力してください'), sg.InputText()],
            [sg.Button('OK'), sg.Button('add'), sg.Button('Kill all')] ]

# ウィンドウの生成
window = sg.Window('サンプルプログラム', layout)

f_name = "config.json"
data = read_json_file(f_name)

print(data["directories"])

config_dirs = data["directories"]

direcotry1 = config_dirs[0]

print("EXIST:",os.path.exists(direcotry1))

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

