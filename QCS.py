from pathlib import *
import subprocess

def listdir(x):
    a = set(x.iterdir())
    d = x / '.DS_Store'
    a.discard(d)
    return a
def checks(x):
    a = (len(x) == 11)
    b = ((x[2] == '_') and (x[5] == '_'))
    x.pop(2) and x.pop(4)
    c = True
    for y in x:
        if not y.isdigit():
            c = False
            break
    if a + b + c == 3:
        return True
    else:
        return False
def tag(x):
    subprocess.run(['tag', '-a', 'Red', str(x)])

# Setup (target and toTag)
target = Path('/Users/K/Desktop/Example')
paths_contents = listdir(target)
toTag = []

# Type Check -- (make sure only folders ∈ contents)
check1 = True
for x in paths_contents:
    if x.is_file():
        check1 = False  
if not check1:
    toTag.append(x)

# Subfolder Check
for x in paths_contents:
    moveOn = False

    # Setup (contents)
    if x.is_dir(): 
        subfolder_contents = listdir(x)
    subfolder_contents.discard(x / 'CaptureOne')
    subfolder_contents.discard(x / f'{x}_Marking.txt') # Change txt to CR3
    file_stems = [y.stem for y in subfolder_contents]
    file_suffixes = {y.suffix for y in subfolder_contents}

    # Subfolder Name Format
    subfolder_name = [y for y in x.name]
    if checks(subfolder_name) == False:
        toTag.append(x)
        moveOn = True
    if moveOn:
        continue

        # Content Quantity Check
    if len(subfolder_contents) == 0:
        toTag.append(x)
        moveOn = True
    if moveOn:
        continue

        # Contents type check
    for y in subfolder_contents:
        if y.is_dir():
            toTag.append(x)
            moveOn = True
    if moveOn:
        continue
        
        # File Stem length check
    for y in file_stems:
        if not (len(y) == 14):
            toTag.append(x)
            moveOn = True
    if moveOn:
        continue

        # Underscore preceeding numbering check
    for y in file_stems:
        if not (y[11] == '_'):
            toTag.append(x)
            moveOn = True
    if moveOn:
        continue    

        # Suffix Type check
    if not (file_suffixes == {'.txt'}):
         toTag.append(x)
         moveOn = True
    if moveOn:
        continue
       
        # Subfolder & Contents Name Correspondence 
    for y in file_stems:
        if not (y[0:11] == x.name):
            toTag.append(x)
            moveOn = True
    if moveOn:
        continue
            
        # Order of Numbers
    numbering = sorted([y[12:14] for y in file_stems])
    base = []
    for y in range(1,len(numbering)+1):
        base.append(f"{y:02d}")     
    if not (numbering == base):
        toTag.append(x)
        moveOn = True
    if moveOn:  
        continue
 
# Tagging & Result
for y in toTag:
    tag(y)
print(f'\nCheck Complete!\n')

