# Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка files
# уникальные имена файлов c расширением .png, независимо от регистра имен и расширений.
# Имена файлов вывести вместе с расширением, все на одной строке, в нижнем регистре, в алфавитном порядке через пробел.

files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG', 'solution.Py', 'stepik.org', 'kotlin.ko',
         'github.git', 'ZeBrA.PnG']

png_files = {file.lower() for file in files if file.lower().endswith('.png')}
print(*sorted(png_files))