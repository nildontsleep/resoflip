![resoflip_branded](https://github.com/user-attachments/assets/29ccdbfa-6bb1-4434-a12b-eed960334b22)

# 🖥️ ResoFlip

**ResoFlip** is a smart Windows resolution switcher that lets you toggle between two display modes: `native` and `stretched`. It also supports hotkeys, GUI confirmations, and system notifications — ideal for gamers, streamers, and productivity users.

Created by [nil](https://github.com/nildontsleep)  
🔗 https://github.com/nildontsleep/resoflip

---

## ✨ Features

- 🔁 Toggle between `[native]` and `[stretched]` resolutions
- 🖱️ GUI confirmation before switching (optional)
- 🔔 Desktop notifications with app icon
- 🎯 Global hotkey support (e.g. `Ctrl+Alt+R`)
- ⚙️ Configurable via `resoflip.toml`
- 📏 Manual input option for custom resolution
- 🧠 Auto-creates config file on first run
- 🪵 Logging to `resoflip.log`
- ✅ Built for Windows using `pywin32`

---

## 📦 Installation

### 1. Clone or download
```bash
git clone https://github.com/nildontsleep/resoflip
cd resoflip
````

### 2. Install dependencies

```bash
pip install pywin32 toml keyboard plyer pillow
```

> ✅ If you're missing `tkinter`, install it via your Python distribution or OS package manager.

### 3. Run

```bash
python resoflip.py
```

---

## 🛠️ Configuration: `resoflip.toml`

On first run, a configuration file is created:

```toml
[native]
width = 1920
height = 1080
refreshrate = 100

[stretched]
width = 1680
height = 1050
refreshrate = 100

logging = true
confirm_before_switch = true
enable_hotkeys = true
hotkey = "ctrl+alt+r"
```

### Options:

* `confirm_before_switch`: Show a GUI confirmation before changing resolution
* `enable_hotkeys`: Enable resolution toggle via keyboard
* `hotkey`: Set your preferred key combo (e.g. `"ctrl+shift+f"`)

---

## 🧠 Behavior

* If your current resolution matches `[native]`, ResoFlip switches to `[stretched]`, and vice versa.
* If you're using a different resolution, you'll be prompted with:

  1. Switch to `[native]`
  2. Switch to `[stretched]`
  3. Enter a custom resolution
  4. Exit without changes

---

## 🔔 Notifications

ResoFlip shows a Windows notification when switching resolutions and uses a custom icon hosted on GitHub. The icon is automatically downloaded and cached as `resoflip.ico`.

---

## ⌨️ Hotkey Support

ResoFlip listens for a **global hotkey** to instantly toggle resolutions. The default is `Ctrl + Alt + R`.

> Press **ESC** to quit hotkey mode.

---

## 🧪 Optional: Build to `.exe`

To create a standalone `.exe` for easy use:

```bash
pip install pyinstaller
pyinstaller --onefile --icon=resoflip.ico resoflip.py
```

---

## 🧠 Credits

Made with 💻 and 🧠 by [nil](https://github.com/nildontsleep)
Logo included in repo (AI-generated)

---

## 📃 License

MIT License
