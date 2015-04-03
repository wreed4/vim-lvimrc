import vim, os.path

cwd = os.getcwd()
homedir = os.path.expandvars("$HOME")

dirnames = [name for name in cwd.split('/') if name not in homedir.split('/')]

curpath = homedir.split('/')
all_files = []
for level in dirnames[:]: # copy dirnames because we're going to be modifying it in this loop 
    curpath.append(dirnames.pop(0))
    lvimrc =  '/{}/.lvimrc'.format('/'.join(curpath))
    if os.path.exists(lvimrc):
        vim.command('source ' + lvimrc)
        all_files.append(lvimrc)
    


def print_files():
    for f in all_files:
        print f
