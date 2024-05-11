@echo off
curl https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts -o %SystemRoot%\System32\drivers\etc\hosts
echo Arquivo hosts atualizado!
pause