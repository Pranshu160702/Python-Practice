import os

cur_dir = str(os.getcwd())
files = os.listdir(cur_dir + "/png_files")

i = 1
for file in files:
    print(f"{file}")
    os.rename(f"png_files/{file}", f"png_files/{i}.png")
    i += 1