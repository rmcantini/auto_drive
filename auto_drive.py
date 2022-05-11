""" Python script to synch folders on command """


# origin path
PATH_ORIGIN = '/Users/rodrigocantini/Documents/Angeloni'

# destination path
PATH_DESTINATION = '/Volumes/GoogleDrive-105809374960814147854/My Drive/Angeloni'

# get string with folder names
TASKS_PAUTA = input('Cole as tasks da pauta aqui: ')
lista_tasks = TASKS_PAUTA.split('#')
# print(lista_tasks)


# clean folder names

# loop to copy files from origin to destination joining the path + folder name


# >>> mystr = "L1\nL2\n\nL3\nL4\n  \n\nL5"
# >>> mystr.split('\n')
# ['L1', 'L2', '', 'L3', 'L4', '  ', '', 'L5']
# >>> [line for line in mystr.split('\n') if line.strip() != '']
# ['L1', 'L2', 'L3', 'L4', 'L5']
