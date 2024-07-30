@echo off 
cls
title Soha Mobile Importer
Echo Hosgeldiniz. 
Echo ------------------------------------------------------------
Echo Uygulama	: Soha Mobile Data Importer "'data.csv' -> 'firestore database'"
Echo Fatih internet agindan baglanildiginda sertifika sorunlari yasanabilir.
Echo SSL Sertifika sorunu cikartmayacak bir ag kullanmaniz tavsiye edilir.
Echo Gelistiren	: Yasin Bal, ybal@hotmail.com
Echo Tarih		: Mart, 2023
Echo ------------------------------------------------------------
cd C:\Users\ybal\codePython\importFirestone

Set "VIRTUAL_ENV=Env"

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
	pip.exe install virtualenv
	python.exe -m venv %VIRTUAL_ENV%
)

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" Exit /B 1

cmd "/c .\%VIRTUAL_ENV%\Scripts\activate [Env] 
cmd "/c .\%VIRTUAL_ENV%\Scripts\pip install firebase-admin google-cloud-firestore"
Echo ------------------------------------------------------------
cmd "/c .\%VIRTUAL_ENV%\Scripts\python 2.py"
cmd "/c .\%VIRTUAL_ENV%\Scripts\deactivate [Env]"



Exit /B 0
