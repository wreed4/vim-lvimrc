import vim, os.path, itertools


All_Files = []



def source_files():
    def _source_file_in_path(path):
        lvimrc =  '{}/.lvimrc'.format('/'.join(path))
        if os.path.exists(lvimrc):
            vim.command('source ' + lvimrc)
            All_Files.append(lvimrc)


    global All_Files
    All_Files = [] # empty All_Files

    cwd = os.getcwd()
    homedir = os.path.expandvars("$HOME")


    if cwd.startswith(homedir):
        dirnames = [name for name in cwd.split('/') if name not in homedir.split('/')]
    else:
        dirnames = []
    

    curpath = homedir.split('/')

    # source any .lvimrc in home directory first (user system-specific settings) 
    _source_file_in_path(curpath) 
    # then loop over the rest of the path
    for level in dirnames[:]: # copy dirnames because we're going to be modifying it in this loop 
        curpath.append(dirnames.pop(0))
        _source_file_in_path(curpath)
    


def print_files():
    for num, fname in enumerate(All_Files):
        print "{}: {}".format(num, fname)


def edit_file():
    print_files()
    options = '\n'.join(('&{}'.format(num) for num, fname in enumerate(All_Files)))
    vim.command('let choice = confirm("Choose a file to edit", "{}")'.format(options))
    choice = int(vim.eval('choice')) - 1  # confirm() indexes options at 1 
    print choice
    if choice >= 0:
        vim.command('tabedit {}'.format(All_Files[choice]))
