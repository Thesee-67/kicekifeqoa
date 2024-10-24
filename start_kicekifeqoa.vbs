Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "Docker\start.bat" & chr(34), 0
Set WshShell = Nothing
