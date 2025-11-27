from pynput import keyboard

code = def on_press(key):
    print(f"{key}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
