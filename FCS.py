from pathlib import *
import subprocess

# Setup Facility
def listdir(x):
    a = set(x.iterdir())
    d = x / '.DS_Store'
    a.discard(d)
    return a
def dir_setup(outer):
    subfolder_contents = listdir(outer)
    subfolder_contents.discard(outer / 'CaptureOne')
    subfolder_contents.discard(outer / f'{outer.name}_Marking.txt') # txt ↔ CR3
    file_stems = [y.stem for y in subfolder_contents]
    file_suffixes = {y.suffix for y in subfolder_contents}
    return subfolder_contents, file_stems, file_suffixes
# Error Marking
def tag(outer, color):
    subprocess.run(['tag', '-a', color, str(outer)])
def error(outer,error_type):
    toTag.append(outer)
    issues.append(f"{outer.name.strip()} triggered {error_type} Error")
# Checks
def subfolder_form(outer):
    subfolder_name = [y for y in outer.name]
    if not (len(subfolder_name) == 11):
         return True
    if not (((subfolder_name[2] == '_') and (subfolder_name[5] == '_'))):
         return True
    subfolder_name.pop(2) and subfolder_name.pop(4) 
    for y in subfolder_name:
        if not y.isdigit():
            return True
    return False
def content_exists(contents):
        return (len(contents) == 0)          
def content_type(contents):
         for y in contents:
            if y.is_dir():
                return True
def stem_len(stems):
        for y in stems:
            if not (len(y) == 14):
                return True
def underscore(stems):
        for y in stems:
            if not (y[11] == '_'):
                return True
def suffix(suffixes):
        if not (suffixes == {'.txt'}):  # txt ↔ CR3
            return True
def correspond(outer,stems):
        for y in stems:
            if not (y[0:11] == outer.name):
                 return True
def numbering(stems):
        numbering = sorted([y[12:14] for y in stems])
        base = []
        for y in range(1,len(numbering)+1):
            base.append(f"{y:02d}")     
        if not (numbering == base):
            return True
def trio_exists(contents):
             return not (len(contents) == 3)
def subfolder_trio(stems):
            return not (sorted(stems) == ['JPG', 'RAW', 'TIFF'])
def suffixes_correspond(outer):
            jpg = {x.suffix.lower() for x in listdir(outer / 'JPG')}
            raw = {x.suffix.lower() for x in listdir(outer / 'RAW')}
            tiff = {x.suffix.lower() for x in listdir(outer / 'TIFF')}
            return not (jpg == {'.jpg'} and raw == {'.txt'} and tiff == {'.tiff'})
def trio_correspond(outer):
            JPG = [x.stem for x in listdir(outer / 'JPG')]
            RAW = [x.stem for x in listdir(outer / 'RAW')]
            TIFF = [x.stem for x in listdir(outer / 'TIFF')]
            return not (sorted(JPG) == sorted(RAW) == sorted(TIFF))
# Composite Checks
def parent(paths, target):
    invalid_paths = []
    for path in paths:
        if path.is_file():
            invalid_paths.append(path)
            error(target, 'Content Type')
    for x in invalid_paths:
        paths.remove(x)  
def Internal_Checks(outer,inner):
    # Content Setup
    contents, stems, suffixes = dir_setup(inner)

    # Subfolder Name Format
    if subfolder_form(outer):
        error(outer, 'Subfolder Name Format')

    # Content Existence Check
    if content_exists(contents):
        error(outer,'Content Availability')
        
    # Contents type check
    if content_type(contents):
        error(outer,'Content Type')   
    
    # File Stem length check
    if stem_len(stems):
        error(outer,'Name Length')            

    # Underscore preceeding numbering check
    if underscore(stems):
        error(outer,'Formatting')

    # Suffix Type check
    if suffix(suffixes):
        error(outer,'Suffix')
    
    # Subfolder & Contents Name Correspondence 
    if correspond(outer, stems):
        error(outer,'Correspondence')        
        
    # Order of Numbers
    if numbering(stems):
        error(outer, 'Numbering')    
def External_Checks(path):
    # Setup
    contents, stems, suffixes = dir_setup(path)

    # Subfolder Quantity
    if trio_exists(contents):
            error(path, 'Content Availability') 
            return None
            
    # Subfolder Content Naming    
    if subfolder_trio(stems):
        error(path, 'Subfolder Contents Naming')            
        return None
    
    # Suffix/Subfolder Correspondence        
    if suffixes_correspond(path):
        error(path, 'Suffix Correspondence')
        return None
    
    # Subfolder Content Correspondence        
    if trio_correspond(path):
        error(path, 'Subfolder Correspondence')    
# Running
def run_process(target, section_choice, color):
   
    # Setup
    global toTag, issues
    toTag = []
    issues = []
    paths = listdir(Path(target))
    
    # Folder Check
    parent(paths, target)

    # Subfolder Checks
    if section_choice.strip() == 'Editing Section':  
        for path in paths: 
            External_Checks(path)
            if not (path in toTag):
                Internal_Checks(path, path / 'RAW')  

    elif section_choice.strip() == 'Photography Section':
        for path in paths:
            Internal_Checks(path,path)

    # Tagging & Result
    for y in toTag:
        tag(y,color.strip())
    issues.sort()
    return issues, set(toTag)
