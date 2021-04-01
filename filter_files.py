import os
import sys
import shutil

source_path = sys.argv[1]

# return last directory in path
last_dir = os.path.basename(os.path.normpath(source_path))


# create directories for target files
def create_target_directories(target_dir):
    if os.path.isdir(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    os.mkdir(target_dir+"/text_files")
    os.mkdir(target_dir+"/pdf_files")
    os.mkdir(target_dir+"/doc_files")
    os.mkdir(target_dir+"/xls_files")


# copy files to their respective directories.
def filter_files():
    current_dir = os.getcwd()
    target_dir = os.path.join(current_dir, last_dir)+"_filtered"

    create_target_directories(target_dir)

    paths_dict = {"text_files": target_dir+"/text_files", "pdf_files": target_dir +
                  "/pdf_files", "doc_files": target_dir+"/doc_files", "xls_files": target_dir+"/xls_files"}

    # r=root, d=directories, f = files
    for r, d, f in os.walk(source_path):
        for file in f:
            destination_path = None
            if file.endswith(".txt"):
                destination_path = paths_dict["text_files"]
            elif file.endswith(".xls") or file.endswith(".xlsx"):
                destination_path = paths_dict["xls_files"]
            elif file.endswith(".pdf"):
                destination_path = paths_dict["pdf_files"]
            elif file.endswith("doc") or file.endswith(".docx"):
                destination_path = paths_dict["doc_files"]

            if destination_path is not None:
                source = os.path.join(r, file)
                destination = os.path.join(destination_path, file)
                try:
                    shutil.copyfile(source, destination)
                except:
                    continue

def main():
    filter_files()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        raise Exception("Invalid number of arguments")
