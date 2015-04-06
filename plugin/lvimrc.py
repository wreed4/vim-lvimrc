import vim, os.path


All_Files = []



def source_files():
    global All_Files
    All_Files = [] # empty All_Files

    cwd = os.getcwd()
    homedir = os.path.expandvars("$HOME")

    dirnames = [name for name in cwd.split('/') if name not in homedir.split('/')]

    def _source_file_in_path(path):
        lvimrc =  '{}/.lvimrc'.format('/'.join(path))
        if os.path.exists(lvimrc):
            vim.command('source ' + lvimrc)
            All_Files.append(lvimrc)

    curpath = homedir.split('/')

    # source any .lvimrc in home directory first (user system-specific settings) 
    _source_file_in_path(curpath) 
    # then loop over the rest of the path
    for level in dirnames[:]: # copy dirnames because we're going to be modifying it in this loop 
        curpath.append(dirnames.pop(0))
        _source_file_in_path(curpath)
    


def print_files():
    for f in All_Files:
        print f
