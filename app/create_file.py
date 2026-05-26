import sys
import os
from datetime import datetime


args = sys.argv[1:]
dirs = []

if "-d" in args:
    for folder in args[args.index("-d") + 1:]:
        if folder == "-f":
            break
        dirs.append(folder)
    if dirs:
        os.makedirs("/".join(dirs), exist_ok=True)


file_name = None
if "-f" in args:
    file_name = args[args.index("-f") + 1]

if file_name:
    if dirs:
        path = "/".join(dirs) + "/" + file_name
    else:
        path = file_name

    count = 1
    line = input("Enter content line: ")

    if os.path.exists(path):
        output_file = open(path, "a")
        output_file.write("\n")
    else:
        output_file = open(path, "w")
    output_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    output_file.write(f"{count} {line}\n")
    output_file.close()

    while line != "stop":
        count += 1
        line = input("Enter content line: ")
        if line != "stop":
            output_file = open(path, "a")
            output_file.write(f"{count} {line}\n")
            output_file.close()
        else:
            continue
