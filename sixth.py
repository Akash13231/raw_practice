from pathlib import Path

#open file if it is exist else creats new file

# p1 = Path('ghi.txt')
# print(type(p1))
#
# if not p1.exists():
#   with open(p1, 'w') as file:
#     file.write('Content 3')
# print(p1.name)
# print(p1.stem)
# print(p1.suffix)
# p2 = Path('files')
# print(list(p2.iterdir()))


#change file names
root_dir = Path('files')
file_paths = root_dir.iterdir()
print(Path.cwd())
for path in file_paths:
  new_filename = "new-" + path.stem + path.suffix
  new_filepath = path.with_name(new_filename)
  print(new_filepath)
  path.rename(new_filepath)
