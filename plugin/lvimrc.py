import vim, os.path

cwd = os.getcwd()
homedir = os.path.expandvars("$HOME")

dirnames = [name for name in cwd.split('/') if name not in homedir.split('/')]

for level in dirnames[:]: # copy dirnames because we're going to be modifying it in this loop 
    curdir = homedir + '/' + '/'.join(dirnames)
    lvimrc =  curdir + "/.lvimrc"
    if os.path.exists(lvimrc):
        vim.command('source lvimrc')
    
    dirnames.pop()
