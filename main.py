import os
from pathlib import Path

target_char_length = 110


def main():
    path = ""
    subdirectories = None
    remove_files = None
    # enter a path
    while path == "" or Path(path).exists() is False:
        path = input("Enter a valid path to begin:")

    while subdirectories not in [True, False]:
        temp = input("Would you like to search subdirectories of the provided path? [Y/N]:").upper()
        # must be a Y or an N
        if temp == "Y":
            subdirectories = True
        if temp == "N":
            subdirectories = False

    while remove_files not in [True, False]:
        temp = input("Would you like delete original files after processing? [Y/N]:").upper()
        # must be a Y or an N
        if temp == "Y":
            remove_files = True
        if temp == "N":
            remove_files = False

    if subdirectories:
        for dir_path, dirs, files in os.walk(path):
            for name in files:
                if name.endswith(".txt"):
                    print("processing " + os.path.join(dir_path, name))
                    re_format(str(os.path.join(dir_path, name)), remove_files)
    else:
        for file in os.listdir(path):
            if file.endswith(".txt"):
                print("processing " + file)
                re_format(path + file, remove_files)


def re_format(path, delete_file):
    # take path, chop .txt off and add [text reformatted].txt
    new_path = path[:-4] + "[text reformatted].txt"
    new_file = open(new_path, 'w', encoding="utf8")
    old_file_content = open(path, encoding="utf8")
    lines = old_file_content.read().splitlines()
    old_file_content.close()
    # reformat text:
    # every 110 characters, look for the next space and replace it with \r\n
    counter = 0

    for line in lines:
        out = ""
        for c in line:
            counter += 1
            if c.isspace() & (counter > target_char_length):
                out += "\n"
                counter = 0
            else:
                out += c
        new_file.write(out + "\n")
    new_file.close()
    if delete_file:
        os.remove(path)


if __name__ == '__main__':
    main()
