import os

folder = "Renamed"
deleted = "Repeated"

if not os.path.exists(folder):
	os.mkdir(folder)
	print(f"created {folder} folder")

if len(os.listdir(f"{folder}")) == 0:
	os.system(f"move ..\\*.* .\\{folder}")

if len(os.listdir(folder)) != 0:
	_dir = os.listdir(folder)
	number = len(_dir)
	os.chdir(folder)
	# print("current directory is:", os.getcwd())

	counter = 0
	for i in _dir:
		counter += 1
		if counter < 100:
			digits = 2
		elif counter < 1000:
			digits = 3
		elif counter < 10000:
			digits = 4
		elif counter < 100000:
			digits = 5
		elif counter < 1000000:
			digits = 6

		new_name = f"{i[-12:-4]}{i[digits:-13]}{i[-4:]}"
		_numbers = list(range(0, 10))
		date = ""

		for x in i[digits + 3: digits + 3 + 8]:
			if x not in str(_numbers):
				if new_name not in os.listdir("./"):
					os.rename(i, new_name)
					break
				else:
					if not os.path.exists(f"..\\{deleted}"):
						os.mkdir(f"..\\{deleted}")
						print(f"created {deleted} folder")
					os.system(f'move ".\\{i}" ..\\{deleted}\\')
			else:
				date += x
				if len(date) == 8:
					new_name = f"{i[digits + 3:]}"
					if new_name not in os.listdir("./"):
						os.rename(i, new_name)
					else:
						if not os.path.exists(f"..\\{deleted}"):
							os.mkdir(f"..\\{deleted}")
							print(f"created {deleted} folder")
						os.system(f'move ".\\{i}" ..\\{deleted}\\')

	_dir = os.listdir("./")
	number = 1
	print()
	for x in _dir:
		if number < 10:
			new_name = f"0{number} - {x}"
		else:
			new_name = f"{number} - {x}"
		print(new_name)
		os.rename(x, new_name)
		number += 1

print()
if len(os.listdir("./")) != 0:
	print("current directory is:", os.getcwd())
	os.system(f"move .\\*.* ..\\..\\")


if len(os.listdir("./")) == 0:
	os.chdir("../")
	print("current directory is:", os.getcwd())
	os.system(f"rmdir .\\{folder}")
