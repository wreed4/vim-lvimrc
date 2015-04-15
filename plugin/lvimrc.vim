pyfile <sfile>:p:h/lvimrc.py

" Print all files loaded by this plugin
command! LvimrcPrint python print_files()

" Reload all files
command! LvimrcReload python source_files()

" Edit files
command! LvimrcEdit python edit_file()


python source_files()
