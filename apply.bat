@echo off
echo If asked to overwrite, type Y.
xcopy "options.xml" "%LOCALAPPDATA%\Teardown\"
echo Done! Now you can start the game.
pause