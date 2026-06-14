"""
Basic-slash. Generates standard unencrypted save code with user input. 
This is a work-in-progress version of the unnamed save code system. It is currently in development and may contain bugs.
This generates multiple blocks split with slashes.
"""

import os

savecode = None

os.system('clear')

while True:
    mode = input("Enter mode (read/write/help): ").lower()

    if mode == "write":
        key_string = input("Enter desired key: ")
        key = key_string.split("/")
        
        savecode = "/".join([input(f"Enter value for {k}: ") for k in key])
        
        print(f"Save code: {savecode}")
    elif mode == "read":
        
        key_string = input("Enter key: ")
        key = key_string.split("/")
        
        code = input("Enter save code: ")
        split_code = code.split("/")
        
        if len(split_code) > len(key):
            print(f"Note: entered code has {len(split_code) - len(key)} more blocks than the key. Only the first {len(key)} blocks will be read.")
        
        for k, val in zip(key, split_code):
            print(f"{k}: {val}")
    elif mode == "help":
        print("""Help:
              This program generates and reads slash-separated save codes. 
              """)
