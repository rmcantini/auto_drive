""" Python script to synch folders on command """


# origin path


from csv import list_dialects


PATH_ORIGIN = '/Users/rodrigocantini/Documents/Angeloni'

# destination path
PATH_DESTINATION = '/Volumes/GoogleDrive-105809374960814147854/My Drive/Angeloni'

# get string with folder names
TASKS_PAUTA = input('Cole as tasks da pauta aqui: ')
# loop to copy files from origin to destination joining the path + folder name
