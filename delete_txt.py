import time
import os
import glob
import json
import concurrent.futures

def git_delete_file(file_name):
    print('Removing File {}'.format(file_name))
    command = """ git filter-branch -f --index-filter "git rm  --cached --ignore-unmatch '{}' " HEAD """.format(file_name)
    os.system(command)

count = 0

if __name__ == "__main__":
    file_list = glob.glob('services/*/*/Data/*.txt')
    total_files=len(file_list)
    
    start = time.perf_counter()

    for file_name in file_list:
        git_delete_file(file_name)
        count +=1
        print("Number of files deleted:", count)
        print("number of files left", total_files-count)
    
    finish = time.perf_counter()

    print(f'Finished in {(finish-start)/60} minutes')



