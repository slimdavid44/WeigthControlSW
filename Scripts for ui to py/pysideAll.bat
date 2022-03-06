mkdir ..\Generated
echo. 2>..\Generated\__init__.py

for /r ..\GUI %%F in (*.ui) do C:\Users\nadav\anaconda3\envs\nadav_project\Scripts\pyside2-uic %%F -o ..\Generated\%%~nF.py
pause