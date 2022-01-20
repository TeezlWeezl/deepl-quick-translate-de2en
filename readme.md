# Steps to activate the Script
1. Copy the following AutoHotkey (AHK) Snippet to your runninig AHK Script
```
; Pressing Alt + e to activate the HotKey
!e::
; Copying Selection
SendInput {LCtrl down}{x down}
Sleep 100
SendInput {x up}{LCtrl up}
ClipWait, 1
; Replacing all Whitespaces with · necessary, because Input String seperating at Whitespace when running script
ipt := StrReplace(Format("{1:s}", Clipboard)," ","·")
; Run the Python script
RunWait, C:\Users\thies\AppData\Local\Microsoft\WindowsApps\pythonw.exe "C:\Users\thies\PycharmProjects\deepl-quick-translate-de2en\main.pyw" %ipt%
; Pasting Selekction
SendInput {LCtrl down}{v down}
Sleep 100
SendInput {v up}{LCtrl up}
ClipWait, 1
return
```
2. Install the required Python packages by running the following command
`
pip install -r C:\Users\thies\PycharmProjects\deepl-quick-translate-de2en\requirements.txt
`

3. Add the Deepl Pro authentication key to as an environment variable. The variable must be named "DEEPL_AUTH".

# How to use the script
Select the text you want to translate and press Alt + e and let the script do its magic ;) .