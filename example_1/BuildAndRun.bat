@echo off
docker build -t "pythonboost" .
docker run -it -v //c/users/alex/dockeumnts/pythonboost:/pythonboost pythonboost /bin/sh
set /p id="Enter to exit"
