'''
Description: 
Author: F.O.X
Date: 2021-06-10 01:02:37
LastEditor: F.O.X
LastEditTime: 2021-06-14 22:48:55
'''
#!/usr/bin/env python3

import PySimpleGUIWeb as sg
import threading


class CamSrv(threading.Thread):
    def __init__(self):
        super().__init__()
        # self.cam =


def main():
    layout = [
        [sg.T("images", font='Any 20')],
        [sg.B('Capture'), sg.B('Exit')],
    ]

    window = sg.Window('Title', layout, disable_close=True)

    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        if event == 'Capture':
            print("cap")

    window.close()


if __name__ == '__main__':
    main()
