import subprocess

subprocess.run(["pdf2txt.py", "-o", "output", "/home/alan/Workspace/Python/SO/so_file_serach_project/6-Strings-Pesquisa-Digital.pdf"])
# print(r'cara\n')

with open("output", 'r') as fhand:
    # data = fhand.read()
    # for x in data:
        # print(x)

    for line in fhand:
        print(line)
