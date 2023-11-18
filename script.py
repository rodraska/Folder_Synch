import os
import filecmp
import shutil
from datetime import datetime
import sys
import time

def compare_dir(src_path, rep_path):
    
    with open(sys.argv[4], 'a') as f:

        cmp = filecmp.dircmp(src_path, rep_path)

        for file in cmp.left_only:
            shutil.copy2(os.path.join(src_path, file), os.path.join(rep_path, file))
            date = datetime.now()
            f_date = date.strftime("%Y/%m/%d %H:%M:%S")
            print(f'{f_date} - File Created: {os.path.join(rep_path, file)}')
            f.write(f'{f_date} - File Created: {os.path.join(rep_path, file)}\n')

        for file in cmp.right_only:
            os.remove(os.path.join(rep_path, file))
            date = datetime.now()
            f_date = date.strftime("%Y/%m/%d %H:%M:%S")
            print(f'{f_date} - File Deleted: {os.path.join(rep_path, file)}')
            f.write(f'{f_date} - File Deleted: {os.path.join(rep_path, file)}\n')

        for file in cmp.diff_files:
            shutil.copy2(os.path.join(src_path, file), os.path.join(rep_path, file))
            date = datetime.now()
            f_date = date.strftime("%Y/%m/%d %H:%M:%S")
            print(f'{f_date} - File Copied: {os.path.join(rep_path, file)}')
            f.write(f'{f_date} - File Copied: {os.path.join(rep_path, file)}\n')

        f.close()

        for sub_dir in cmp.common_dirs:
            compare_dir(os.path.join(src_path, sub_dir), os.path.join(rep_path, sub_dir))
        

def main():

    while (1):
        compare_dir(sys.argv[1], sys.argv[2])
        time.sleep(int(sys.argv[3]))

main()

#args: script, source_folder, replica_folder, synch interval, log file