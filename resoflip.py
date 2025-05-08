"""
ResoFlip - Resolution Switcher for Windows
Created by nil
"""

import win32api
import win32con
import pywintypes
import os
import toml

CONFIG_FILE = "resoflip.toml"

# ------------------ Branding ------------------
def print_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 40)
    print("       ResoFlip - by nil")
    print("     Smart Resolution Switcher")
    print("=" * 40)

# ------------------ Load or Create Config ------------------
def load_or_create_config():
    default_config = {
        "native": {
            "width": 1920,
            "height": 1080,
            "refreshrate": 100
        },
        "stretched": {
            "width": 1680,
            "height": 1050,
            "refreshrate": 100
        }
    }

    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            toml.dump(default_config, f)
        print(f"\n🛠️  Created default config: {CONFIG_FILE}")
        return default_config

    try:
        with open(CONFIG_FILE, "r") as f:
            return toml.load(f)
    except Exception as e:
        print(f"❌ Failed to load config: {e}")
        return default_config

# ------------------ Display Functions ------------------
def get_current_settings():
    devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    return devmode.PelsWidth, devmode.PelsHeight, devmode.DisplayFrequency

def change_resolution(width, height, frequency):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = width
    devmode.PelsHeight = height
    devmode.DisplayFrequency = frequency
    devmode.Fields = (
        win32con.DM_PELSWIDTH |
        win32con.DM_PELSHEIGHT |
        win32con.DM_DISPLAYFREQUENCY
    )

    result = win32api.ChangeDisplaySettings(devmode, 0)
    if result == win32con.DISP_CHANGE_SUCCESSFUL:
        print(f"\n✅ Resolution changed to {width}x{height} @ {frequency}Hz")
    else:
        print("\n❌ Failed to change resolution.")

# ------------------ Prompt Fallback ------------------
def prompt_options(config):
    print("\n⚠️ Current resolution is not one of the presets. Choose an option:")
    print("1. Switch to [native] preset")
    print("2. Switch to [stretched] preset")
    print("3. Enter custom resolution")
    print("4. Exit without changes")

    choice = input("\nYour choice: ").strip()

    if choice == "1":
        native = config["native"]
        change_resolution(native["width"], native["height"], native["refreshrate"])
    elif choice == "2":
        stretched = config["stretched"]
        change_resolution(stretched["width"], stretched["height"], stretched["refreshrate"])
    elif choice == "3":
        try:
            w = int(input("  Width: "))
            h = int(input("  Height: "))
            hz = int(input("  Refresh Rate (Hz): "))
            change_resolution(w, h, hz)
        except ValueError:
            print("\n❌ Invalid input.")
    else:
        print("\nℹ️ No changes made.")

# ------------------ Main ------------------
def main():
    print_logo()
    config = load_or_create_config()

    current_width, current_height, current_hz = get_current_settings()
    print(f"Current resolution: {current_width}x{current_height} @ {current_hz}Hz")

    native = config["native"]
    stretched = config["stretched"]

    if (current_width, current_height, current_hz) == (
        native["width"], native["height"], native["refreshrate"]
    ):
        change_resolution(stretched["width"], stretched["height"], stretched["refreshrate"])

    elif (current_width, current_height, current_hz) == (
        stretched["width"], stretched["height"], stretched["refreshrate"]
    ):
        change_resolution(native["width"], native["height"], native["refreshrate"])

    else:
        prompt_options(config)

if __name__ == "__main__":
    main()
