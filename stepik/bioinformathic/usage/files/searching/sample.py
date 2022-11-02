#  Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
#
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
# в которых есть хотя бы один файл с расширением ".py".

import os
import os.path


def sample_test(folder):
    pathes = []
    used = set()
    for current_dir, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.py'):
                pathes.append(current_dir.replace('\\', '/').rstrip('/'))
                used.add(current_dir.replace('\\', '/').rstrip('/'))

    print(pathes)
    print(*sorted(used), sep='\n', file=open(f'{folder.rstrip("/")}_ans.txt', 'w'))


sample_test('main/')
