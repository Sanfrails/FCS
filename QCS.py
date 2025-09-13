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
    for y in x:
        if y.isdigit():
            c = True
        else: 
            c = False
            break
    if a + b + c == 3:
        return True
    else:
        return False
def tag(x):
    subprocess.run(['tag', '-a', 'Red', str(x)])

# target & contents extract
target = Path('/Users/K/Desktop/Example')
paths_contents = listdir(target)
names_contents = sorted([x.name for x in paths_contents])

# check#1 Type -- (make sure only folders ∈ contents)
check1 = True
for x in paths_contents:
    if x.is_file():
        check1 = False  
if not check1:
    tag(x)

# check#2 Type & Naming Format -- (subfolders & contents)

for x in names_contents:

    # (Subfolder Name Format)
    subfolder_name = [y for y in x]
    if checks(subfolder_name) == False:
        tag(target / x)

    # (Contents ∈ Subfolder)
    subfolder_path = target / x
    if subfolder_path.is_dir(): 
        subfolder_contents = listdir(subfolder_path)
    subfolder_contents.discard(subfolder_path / 'CaptureOne')
    subfolder_contents.discard(subfolder_path / f'{x}_Marking.txt') # Change txt to CR3
    file_stems = [y.stem for y in subfolder_contents]
    file_suffixes = {y.suffix for y in subfolder_contents}

        # Contents type check
    for y in subfolder_contents:
        if y.is_dir():
            tag(subfolder_path)
        
        # File Stem length check
    moveOn = False
    for y in file_stems:
        if not (len(y) == 14):
            tag(subfolder_path)
            moveOn = True
    if moveOn:
        continue

        # Underscore preceeding numbering check
    for y in file_stems:
        if not (y[11] == '_'):
            tag(subfolder_path)

        # Suffix Type check
    if not (file_suffixes == {'.CR3'}):
        #tag(subfolder_path)
        pass

        # Subfolder & Contents Name Correspondence 
    for y in file_stems:
        if not (y[0:11] == x):
            tag(subfolder_path)
        
        # Order of Numbers
    base = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 
 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
 '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
 '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']
    numbering = sorted([y[12:14] for y in file_stems])
    del base[len(numbering):50]      
    if not (numbering == base):
        tag(subfolder_path)

print(f'\nCheck Complete!\n')
    

  
