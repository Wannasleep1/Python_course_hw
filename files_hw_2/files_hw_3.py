import os


dir_path = os.path.join(os.getcwd(), 'files')
txt_files = [elem for elem in os.listdir(dir_path)
             if os.path.isfile(os.path.join(dir_path, elem)) and
             elem.endswith('.txt')]
files_lst = []
for file_name in txt_files:
	with open(os.path.join(dir_path, file_name), encoding='utf-8') as f:
		files_lst.append((f.readlines(), file_name))
files_lst.sort(key=lambda elem: len(elem[0]))
new_file = os.path.join(os.getcwd(), 'final_file.txt')
with open(new_file, 'w', encoding='utf-8') as f:
	for i, elem in enumerate(files_lst):
		name = ('\n' + elem[1] + '\n') if i != 0 else (elem[1] + '\n')
		f.write(name)
		f.write(str(len(elem[0])) + '\n')
		for string in elem[0]:
			f.write(string)