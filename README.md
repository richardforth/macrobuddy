# macrobuddy
A 9 key macro keyboard emulator

# Screenshot

![MacroBuddy Interface Screenshot](/MacroBuddy.png?raw=true "MacroBuddy Interface Screenshot")

# About

A 9 key programmable* software based macro keyboard.

* Edit any one of the 9 macro functions using python code / pyautogui key combinations
* 1, 2, 3 are preset samples

# Usage

Keys 1, 2 and 3 come pre set as examples (you can edit these as you see fit, see Programming Macros)

Keys 1 and 2:

Open an editor
Open MacroBuddy
Press key one, you have 5 seconds to click  on to the editor window / text input
wait 5 seconds
macro will play

Key 3: See Advanced Macros

# Advanced Macros
Example in slot 3 as a preset
- Uses pyautogui

Open up Excel / LibreOffice Calc / OpenOffice Calc
Add a range of values across a few columns
Click on Macrobuddy Preset 3
Before the 5 second timer finishes, click on Top right most cell of the range., eg Cell A1 or A2
Macro will start
- Presses CTRL+SHIFT+RIGHT
- Presses CTRL+SHIFT+DOWN
- Presses CTRL+C

For more advanced macro python code see the pyautogui documentation: https://pyautogui.readthedocs.io/en/latest/

# OS Support

Should work fine across Windows, Mac, linux

Requirements
python3-tk (Linux / Mac)
python3-tkinter (Windows)
pyautogui (pip3 install pyutogui)


# Programming Macros

Each Button on the keypad has a corresponding macroN function, eg Button "1"  maps to "macro1" and so on.
Edit the nine corresponding functions using python code and pyautogui functions to acheive complex, time saving macros.


# Notes

Unless to program in all of the hotkeys and shortcuts required for all of the steps to open up a program and focus on a text field or cell or do what you need to do correctly, you cant just press a button and sit back, you will have 5 seconds to put the mouse pointer / cursor where it needs to be and cick, hence the 5 second delay before the macro starts.

# Testing Macros can cause undefined behaviour / data loss

If you mis-time an action, it is possible that undefined behaviour can occur when running macros, including data loss. 

If the macro isnt too long you can usually back out changes to files with CTRL+z,
providing the file hasnt been saved /closed as part of the macro

I am not going to be held liable for your mistakes in programming your macros or your use of this program.

See MIT License Terms in "LICENSE"
