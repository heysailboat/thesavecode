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
        pass
    elif mode == "read":
        
        key_string = input("Enter key: ")
        key = key_string.split("/")
        
        code = input("Enter save code: ")
        split_code = code.split("/")
        
        if len(split_code) > len(key):
            print(f"Note: entered code has {len(split_code) - len(key)} more blocks than the key. Only the first {len(key)} blocks will be read.")
        
        for k, val in zip(key, split_code):
            print(f"{k}: {val}\n")
    elif mode == "help":
        print("""Help:
              This program generates and reads slash-separated save codes. 
              """)
