from pathlib import Path

path = Path('package')
print(path.exists())

#path = Path('emails')
#print(path.mkdir()) # create folder
#print(path.rmdir()) # delete folder

path = Path()
for file in path.glob('*.py'):
    print(file)