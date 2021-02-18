$action = New-ScheduledTaskAction -Execute 'Powershell.exe' -Argument 'C:\it30380c-scripts\Labs\webBrowserCode.py'

$trigger = New-ScheduledTaskTrigger -Daily -At 10:25am 

Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "PythonOpen2" -Description "brandon was here" 