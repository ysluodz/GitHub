@echo off
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TCPIP\Parameters" /v "KeepAliveTime" /t reg_dword /d "30000" /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TCPIP\Parameters" /v "KeepAliveInterval" /t reg_dword /d "5000" /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TCPIP\Parameters" /v "MaxDataRetries" /t reg_sz /d "5" /f
pause