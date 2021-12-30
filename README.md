# <p align=center>GDInfo</p>
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/kelptaken/GDInfo) [![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://github.com/kelptaken/GDInfo/releases)

**Geometry Dash swiss knife**

**⚠** This project is not developed anymore.

## But what can it do?
1. check full info about a level (including stars requested by creator, link to raw song MP3 and more)
2. check full info about an account (including unique Player ID)
3. export to JSON
4. download user's icons to PNG

## How to install?
- Ensure Python 3 is installed on your machine.
- Clone the repository (or download as ZIP)
- Go to the project directory
- Execute ``pip3 install -r requirements.txt`` (this is done only once)
- Execute ``python GDInfo.py`` to run the script.

## 2.1 is out!
- Cleaner code
- CLI mode
- OS autodetect
- Better error handling

## CLI mode
GDInfo.py accepts arguments to skip all the boring mode selection.

**1st argument**

Always should be `cli`.

**2nd argument**

Either `level` or `account`.

**3rd argument**

Account: `info` for account info, `json` to export info to JSON, `icon` to download player's icon.

**4th argument**

Player or level's name, unless you want to download an icon.
If you're downloading an icon, 4th argument should be:

1 for Cube

2 for Ship

3 for Ball

4 for UFO

5 for Wave

6 for Robot

7 for Spider


**5th argument**

Only used if you're downloading an icon. Otherwise not needed.

**Examples**

`python GDInfo.py cli level info bloodbath` to retrieve Bloodbath info

`python GDInfo.py cli account json trusta` to export Trusta's info in JSON

`python GDInfo.py cli account icon 2 kelptaken` to download script creator's ship icon.

If no arguments were passed, script will use interactive selector.
## Bugs
Wow, you found it? Issues tab is for you!

## Under the hood
GDInfo is using GDBrowser.com's API
