import os
import os.path
import shutil

print(os.getcwd())
print(os.listdir())

print(os.path.exists('test.py'))

print(os.path.isfile('ex0.py'))

print(os.path.isdir('ex0.py'))

for current_dir, dirs, files in os.walk('c://python311'):
    print(current_dir, dirs, files)

