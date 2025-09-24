from pathlib import *
import subprocess

# Setup Facility
def listdir(x):
    a = set(x.iterdir())
    d = x / '.DS_Store'
    a.discard(d)
    return a
def dir_setup(x):
    subfolder_contents = listdir(x)
    subfolder_contents.discard(x / 'CaptureOne')
    subfolder_contents.discard(x / f'{x.name}_Marking.txt') # txt ↔ CR3
    file_stems = [y.stem for y in subfolder_contents]
    file_suffixes = {y.suffix for y in subfolder_contents}
    return subfolder_contents, file_stems, file_suffixes
# Error Marking
def tag(x):
    subprocess.run(['tag', '-a', 'Red', str(x)])
def error(x,y):
    toTag.append(x)
    issues.append(f"{x.name.strip()} triggered {y} Error")
# Checks
def subfolder_form(x):
    subfolder_name = [y for y in x.name]
    if not (len(subfolder_name) == 11):
         return True
    if not (((subfolder_name[2] == '_') and (subfolder_name[5] == '_'))):
         return True
    subfolder_name.pop(2) and subfolder_name.pop(4) 
    for y in subfolder_name:
        if not y.isdigit():
            return True
    return False
def content_exists(x):
        return (len(x) == 0)          
def content_type(x):
         for y in x:
            if y.is_dir():
                return True
def stem_len(x):
        for y in x:
            if not (len(y) == 14):
                return True
def underscore(x):
        for y in x:
            if not (y[11] == '_'):
                return True
def suffix(x):
        if not (x == {'.txt'}):  # txt ↔ CR3
            return True
def correspond(x,z):
        for y in x:
            if not (y[0:11] == z.name):
                 return True
def numbering(x):
        numbering = sorted([y[12:14] for y in x])
        base = []
        for y in range(1,len(numbering)+1):
            base.append(f"{y:02d}")     
        if not (numbering == base):
            return True
def Internal_Checks(x,z):
    # Content Setup
    contents, stems, suffixes = dir_setup(x)

    # Subfolder Name Format
    if subfolder_form(z):
        error(z, 'Subfolder Name Format')

    # Content Existence Check
    if content_exists(contents):
        error(z,'Content Availability')
        
    # Contents type check
    if content_type(contents):
        error(z,'Content Type')   
    
    # File Stem length check
    if stem_len(stems):
        error(z,'Name Length')            

    # Underscore preceeding numbering check
    if underscore(stems):
        error(z,'Formatting')

    # Suffix Type check
    if suffix(suffixes):
        error(z,'Suffix')
    
    # Subfolder & Contents Name Correspondence 
    if correspond(stems,z):
        error(z,'Correspondence')        
        
    # Order of Numbers
    if numbering(stems):
        error(z, 'Numbering')    
                 
# Initial Setup
target = Path(input("\nTarget : "))
paths_0 = listdir(target)
invalid_paths = []
toTag = []
issues = []
section_choice = 'Editing'

# External Type Check
for path in paths_0:
    if path.is_file():
        invalid_paths.append(path)
        error(target, 'Content Type')
for x in invalid_paths:
     paths_0.remove(x)    

# External Subfolder Checks
if section_choice == 'Editing':
    for path in paths_0:
        
        # Setup
        contents, stems, suffixes = dir_setup(path)

        # Subfolder Quantity
        if not (len(contents) == 3):
            error(path, 'Content Availability') 

        # Subfolder Content Naming
        if not (sorted(stems) == ['JPG', 'RAW', 'TIFF']):
            error(path, 'Subfolder Contents Naming')
            continue

        # Suffix/Subfolder Correspondence
        jpg = {x.suffix.lower() for x in listdir(path / 'JPG')}
        raw = {x.suffix.lower() for x in listdir(path / 'RAW')}
        tiff = {x.suffix.lower() for x in listdir(path / 'TIFF')}
        if not (jpg == {'.jpg'} and raw == {'.txt'} and tiff == {'.tiff'}):
             error(path, 'Suffix Correspondence')
             continue

        # Subfolder Content Correspondence
        JPG = [x.stem for x in listdir(path / 'JPG')]
        RAW = [x.stem for x in listdir(path / 'RAW')]
        TIFF = [x.stem for x in listdir(path / 'TIFF')]
        if not (sorted(JPG) == sorted(RAW) == sorted(TIFF)):
            error(path, 'Subfolder Correspondence')
            continue
               
        # Internal Checks Prep
        raw_folder = path / 'RAW' 
        # Internal Subfolder Checks
        Internal_Checks(raw_folder, path)     
else:
     for x in paths_0:
        Internal_Checks(x,x)

# Tagging & Result
for y in toTag:
    tag(y)
issues.sort()
print(f'\nCheck Complete!\n')
for x in issues:    
    print(x)
