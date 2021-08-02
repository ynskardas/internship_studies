#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^1::
Send, 	^+Q{Enter}{Ctrl down}{Delete down}{Delete up}{Ctrl up}^+I{Alt down}{Delete down}{Delete up}{Alt up}{Ctrl down}{d down}{d up}{Ctrl up}{Ctrl down}{s down}{s up}{Ctrl up}