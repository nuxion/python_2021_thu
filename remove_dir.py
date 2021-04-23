"""
Clase 5
Si shutil.rmtree() no existiria, 
como podrias remover una carpeta que tiene archivos?

Actualmente este ejemplo falla si en la carpeta que le paso como argumento
hay subdirectorios con archivos
"""
import os
import sys

def remove_dir(path, recursive=False):
    if recursive:
        files = os.listdir(path)
        for x in files:
            print(f'Deleting {x}')
            os.remove(f'{path}/{x}')

        os.rmdir(path)
    else:
        try:
            os.rmdir(path)
        except OSError:
            print(f'{path} is not empty')


if __name__ == '__main__':
    args = sys.argv
    p = args[1]
    if len(args) > 1:
        remove_dir(p, True)
    else:
        remove_dir(p)