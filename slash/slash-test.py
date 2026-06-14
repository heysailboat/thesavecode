"""
basic-slash library.
generates and reads slash-separated save codes.
"""
import os

def write(values):
    """takes a list of values and returns the save code string."""
    return "/".join(values)
    
def read(keys, savecode):
    """takes a list of keys and a save code, returns a dictionary of the parsed data."""
    split_code = savecode.split("/")
    
    # keeping your warning, though usually libraries might raise an Exception instead!
    if len(split_code) > len(keys):
        print(f"note: entered code has {len(split_code) - len(keys)} more blocks than the key. only the first {len(keys)} blocks will be read.")
        
    # zip is goated here, we turn it straight into a python dictionary
    return dict(zip(keys, split_code))


# --- CLI MODE ---
# this block is the secret sauce for making a library.
if __name__ == "__main__":
    os.system('clear')
    
    while True:
        mode = input("enter mode (read/write/help): ").lower()

        if mode == "write":
            key_string = input("enter desired key (e.g. a/b/c): ")
            keys = key_string.split("/")
            
            # grab values for each key
            values = [input(f"enter value for {k}: ") for k in keys]
            
            # pass the list of values to your clean library function
            savecode = write(values)
            print(f"save code: {savecode}")
            
        elif mode == "read":
            key_string = input("enter key (e.g. a/b/c): ")
            keys = key_string.split("/")
            
            code = input("enter save code: ")
            
            # pass both to the library function, get a dictionary back
            parsed_data = read(keys, code)
            
            # loop through the returned dictionary to show the user
            for k, val in parsed_data.items():
                print(f"{k}: {val}")
                
        elif mode == "help":
            print("help:\nthis program generates and reads slash-separated save codes.")