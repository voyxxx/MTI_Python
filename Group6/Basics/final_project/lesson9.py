"""
Важно, не используйте команду print(f'{os.system("taskkill /im autohotkey.exe")}') с 
другими процессами, используйте только для завершения процесса AHK. Это может привести к проблемам.
"""


from ahk import AHK 
import os

def my_callback():
    print(f'{os.system("taskkill /im autohotkey.exe")}')

ahk = AHK()

ahk.add_hotkey('#n', callback=my_callback)
ahk.start_hotkeys()
ahk.block_forever()


"""

Если хотите использовать другие клавиши для завершения:
Чтобы изменить горячую клавишу на "Ctrl + N" в вашем коде, вы должны заменить #n на ^n, где ^ обозначает клавишу Ctrl. Вот как будет выглядеть измененная строка:

ahk.add_hotkey('^n', callback=my_callback)


"""