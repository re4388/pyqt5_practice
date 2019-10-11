from os import listdir, rename
from os.path import isfile, join
import subprocess


# return name of file to be kept after conversion.
# we are just changing the extension. azw3 here.
def get_final_filename(f):

    # slit up and get the part excluding extention
    f = f.split(".")
    filename = ".".join(f[0:-1])

    # add new extension
    processed_file_name = filename+".azw3"
    return processed_file_name


# get extension string
def get_file_extension(f):
    return f.split(".")[-1]


# list of extensions that needs to be ignored.
ignored_extensions = ["pdf"]

# here all the downloaded files are kept
mypath = "/home/user/Downloads/ebooks/"

# path where converted files are stored
result_path = "/home/user/Downloads/ebooks/kindle/"

# path where processed files will be moved to, clearing the downloaded folder
file_moved_to = "/home/user/Downloads/ebooks/processed/"

raw_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
converted_files =  [f for f in listdir(result_path) if isfile(join(result_path, f))]

for f in raw_files:
    final_file_name = get_final_filename(f)
    extension = get_file_extension(f)
    if final_file_name not in converted_files and extension not in ignored_extensions:
        print("Converting : " + f )
        try:
            subprocess.call(["ebook-convert", mypath + f, result_path + final_file_name]) 
            s = rename(mypath + f, file_moved_to + f)
            print(s)
        except Exception as e:
            print(e)
    else:
        print("Already exists : " + final_file_name)


def get_final_filename(f):

    # slit up and get the part excluding extention
    f = f.split(".")
    filename = ".".join(f[0:-1])

    # add new extension
    processed_file_name = filename+".mobi"
    return processed_file_name


def converFile(original_filename):
    try:
        subprocess.call(["ebook-convert", original_filename, get_final_filename]) 
        print(get_final_filename)
    except Exception as e:
        print(e)
    
