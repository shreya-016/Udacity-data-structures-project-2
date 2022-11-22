# File Recursion
import os
    
def find_files(suffix, path):
    answer = list()
    listOfFiles = os.listdir(path)
    
    for file in listOfFiles:
        newPath = os.path.join(path, file)
        if os.path.isdir(newPath):
            answer += find_files(suffix, newPath)
        else:
            if newPath.endswith(suffix):
                answer.append(newPath)
    return answer

# Test were run locally on my windows laptop where I saved the testdir locally.
#path_base = os.getcwd()
#print(path_base)
#C:\Users\shrey\home\workspace\testdir

print(find_files('.c', '.'))
# output1
#['.\\subdir1\\a.c', '.\\subdir3\\subsubdir1\\b.c', '.\\subdir5\\a.c', '.\\t1.c']

print(find_files('.h', '.'))
# output2
# ['.\\subdir1\\a.h', '.\\subdir3\\subsubdir1\\b.h', '.\\subdir5\\a.h', '.\\t1.h']

print(find_files('.m', '.'))
# output3
# []
