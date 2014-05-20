if !has('python')
    echo "Error: Required vim compiled with +python"
    finish
endif

function! Send()
    python import sys, vim
    python sys.argv = [vim.eval("expand('%:p')")]
    pyfile send.py
endfunc
 
command! Send call Send()
