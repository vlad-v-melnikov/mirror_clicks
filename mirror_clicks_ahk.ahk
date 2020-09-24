#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.

SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;to save the file
!r::
Run, c:\Users\olga.melnikova\Documents\__ERT\Testing\AHK Scripts\test.ahk
return

;check if the script is working
#c::
MsgBox, The script is working
return

Esc::
MsgBox, Exiting Script
ExitApp

Space::
;MsgBox, You pressed 'Space'
shift := A_ScreenWidth / 2
Click
Click, Relative, %shift%, 0
shift := -shift
Click, Relative, %shift%, 0
return