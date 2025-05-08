![resoflip_branded](https://github.com/user-attachments/assets/29ccdbfa-6bb1-4434-a12b-eed960334b22)

# 🖥️ ResoFlip


**ResoFlip** is a simple Windows utility that toggles between two predefined screen resolutions or allows you to set a custom one. It's especially useful for gamers or creators who switch between native and stretched displays.

Created by [nil](https://github.com/nildontsleep)  
🔗 https://github.com/nildontsleep/resoflip

---

## ✨ Features

- 🔁 Toggle between `[native]` and `[stretched]` resolutions
- ⚙️ Resolutions are configurable via `resoflip.toml`
- 📏 Manual input option for custom resolution
- 🪄 Auto-creates config file on first run
- 🧠 Remembers your resolution preferences
- ✅ Built for Windows (via `pywin32`)

---

## 📦 Installation

### 1. Clone or download
```bash
git clone https://github.com/nildontsleep/resoflip
cd resoflip
````

### 2. Install dependencies

```bash
pip install pywin32 toml
```

### 3. Run

```bash
python resoflip.py
```

---

## 🛠️ Config: `resoflip.toml`

On first run, a file called `resoflip.toml` will be created in the same directory:

```toml
[native]
width = 1920
height = 1080
refreshrate = 100

[stretched]
width = 1680
height = 1050
refreshrate = 100
```

Edit these values to match your preferred resolutions.

---

## 💡 Behavior

* If you're using the `[native]` resolution, it switches to `[stretched]`, and vice versa.
* If your current resolution doesn't match either, it prompts you with 4 options:

  1. Switch to `[native]`
  2. Switch to `[stretched]`
  3. Enter a custom resolution
  4. Exit without changing

---

## 📦 Build to .exe (optional)

To create a standalone `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile resoflip.py
```

Place your custom icon with the name `resoflip.ico` if desired:

```bash
pyinstaller --onefile --icon=resoflip.ico resoflip.py
```

---

## 🧠 Credits

Made with 💻 and 🧠 by [nil](https://github.com/nildontsleep)
Logo included in repo (AI)

---

## 📃 License

MIT License
