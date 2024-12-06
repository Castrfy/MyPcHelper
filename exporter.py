import os
os.system("start cmd /k pyinstaller main.py --noconsole --onefile")
os.rename(f'dist/main.exe',f'../MyPcHelper EXPORT/main.exe')
