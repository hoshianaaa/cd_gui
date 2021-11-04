import PySimpleGUI as sg
import os 

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text('ここは1行目')],
            [sg.Text('ここは2行目：適当に文字を入力してください'), sg.InputText()],
            [sg.Button('OK'), sg.Button('キャンセル')] ]

# ウィンドウの生成
window = sg.Window('サンプルプログラム', layout)

# イベントループ
while True:

    print('あなたが入力した値： ', )
    event, values = window.read()
    if event == 'キャンセル':
        os.system('killall gnome-terminal-server')
        #break

    elif event == 'OK':
        d = values[0]
        print("directory",d)
        os.system('gnome-terminal -- bash -c "cd %s; bash"' % d)

    elif event == sg.WIN_CLOSED:
        break

window.close()

