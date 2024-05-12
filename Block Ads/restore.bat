@echo off
REM Este script substitui o arquivo hosts pelo arquivo hosts_bak do diretório onde o script está localizado

copy /Y "%~dp0hosts_bak" "%SystemRoot%\System32\drivers\etc\hosts"
if %ERRORLEVEL% == 0 (
    echo Arquivo hosts substituido com sucesso!
) else (
    echo Falha ao substituir o arquivo hosts!
)
pause