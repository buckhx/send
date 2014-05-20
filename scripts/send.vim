if !has('python')
    echo "Error: Required vim compiled with +python"
    finish
endif

function! Send()
  ech bufname('%')
  ech bufname('')
  python import sys
  python sys.argv = [bufname('%')]
  pyfile send.py
endfunc
 
command! Send call Send()
