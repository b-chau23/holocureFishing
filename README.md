# holocureFishing
Automatic fishing in Holocure. Simply execute and start fishing!

Uses MSS to take small screenshots (like 1x10 pixels small) of the fishing zone and reads those pixels to search for certain colours. Press certain keys depending on which colour was detected.


# Usage
1. Download the ZIP file or clone the repository
2. Exucute main.py in either a console or by double-clicking the file
3. Launch Holocure and enter Holo house to start fishing

To quit, close the Python window that opened when main.py was executed.

## Usage Notes
Only works on 1280x720 resolution and windowed (not fullscreen). Any other game settings are fine. __Do not__ move the Holocure window after 
the first time the fishing minigame is entered. However, you can still move around in-game and come back to fish without needing to restart the script.  

Unfortunately does not work when minimised or in background.

# Requirements 
## System
Currently works with [Python 3.9 or later](https://www.python.org/downloads/).

Packages
- [MSS: 9.0.1 or later](https://pypi.org/project/mss/)
- [PyAutoGui: 0.9.54 or later](https://pypi.org/project/PyAutoGUI/)

Or run: `pip install -r requirements.txt` 

## Holocure
- 1280x720 Resolution on windowed mode
- Not minimised or in background

Key Bindings:
| Key | Action |
|:---:|:------:|
| w   |   up   |
| a   |  left  |
| s   |  down  |
| d   |  right |
| space   | confirm |
