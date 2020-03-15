let g:plugged_home = '~/.vim/plugged'

" Plugins List
call plug#begin(g:plugged_home)

  " UI related
  Plug 'chriskempson/base16-vim'
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'
  Plug 'scrooloose/nerdtree'

  " Better Visual Guide
  Plug 'Yggdroot/indentLine'

  " syntax check
  Plug 'w0rp/ale'

  " Autocomplete
  Plug 'ncm2/ncm2'
  Plug 'roxma/nvim-yarp'
  Plug 'ncm2/ncm2-bufword'
  Plug 'ncm2/ncm2-path'
  Plug 'ncm2/ncm2-jedi'

  " Formatter
  Plug 'Chiel92/vim-autoformat'

  " Themes
  Plug 'drewtempelmeyer/palenight.vim'
  Plug 'dylanaraps/wal.vim'
  Plug 'challenger-deep-theme/vim', { 'as': 'challenger-deep' }
  
  " Vim Cheatsheet
  Plug 'liuchengxu/vim-which-key'

  " Vim multi-cursor
  Plug 'terryma/vim-multiple-cursors'

  " UltiSnips vim snippets
  Plug 'SirVer/ultisnips'

  " Devicon glyphs for Nerdtree
  Plug 'ryanoasis/vim-devicons'

call plug#end()

set encoding=UTF-8

filetype plugin indent on

" Configurations Part"

" UI configuration
syntax on
syntax enable

" colorscheme
set background=dark
colorscheme wal

" Italics for palenight
"let g:palenight_terminal_italics = 1

" True Color Support if it's avaiable in terminal
"if has("termguicolors")
"    set termguicolors
"endif
"if has("gui_running")
"  set guicursor=n-v-c-sm:block,i-ci-ve:block,r-cr-o:blocks
"endif

"set termguicolors
set number
set relativenumber
set hidden
set mouse=a
set noshowmode
set noshowmatch
set nolazyredraw

" Turn off backup
set nobackup
set noswapfile
set nowritebackup

" Search configuration
set ignorecase                    " ignore case when searching
set smartcase                     " turn on smartcase

" Tab and Indent configuration
set expandtab
set tabstop=4
set shiftwidth=4

" vim-autoformat
noremap <F3> :Autoformat<CR>

" NERDTree configs
map <C-,> :NERDTreeToggle<CR>
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'

" NCM2
augroup NCM2
  autocmd!
  " enable ncm2 for all buffers
  autocmd BufEnter * call ncm2#enable_for_buffer()
  " :help Ncm2PopupOpen for more information
  set completeopt=noinsert,menuone,noselect
  " When the <Enter> key is pressed while the popup menu is visible, it only
  " hides the menu. Use this mapping to close the menu and also start a new line.
  inoremap <expr> <CR> (pumvisible() ? "\<c-y>\<cr>" : "\<CR>")
  " uncomment this block if you use vimtex for LaTex
  " autocmd Filetype tex call ncm2#register_source({
  "           \ 'name': 'vimtex',
  "           \ 'priority': 8,
  "           \ 'scope': ['tex'],
  "           \ 'mark': 'tex',
  "           \ 'word_pattern': '\w+',
  "           \ 'complete_pattern': g:vimtex#re#ncm2,
  "           \ 'on_complete': ['ncm2#on_complete#omni', 'vimtex#complete#omnifunc'],
  "           \ })
augroup END

" Ale
let g:ale_lint_on_enter = 0
let g:ale_lint_on_text_changed = 'never'
let g:ale_echo_msg_error_str = 'E'
let g:ale_echo_msg_warning_str = 'W'
let g:ale_echo_msg_format = '[%linter%] %s [%severity%]'
let g:ale_linters = {'python': ['flake8']}

" Airline
let g:airline_left_sep  = ''
let g:airline_right_sep = ''
let g:airline#extensions#ale#enabled = 1
let airline#extensions#ale#error_symbol = 'E:'
let airline#extensions#ale#warning_symbol = 'W:'
let g:airline_theme = 'wal' 

" .rasi syntax
au BufNewFile,BufRead /*.rasi setf css

" UltiSnips config
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"
let g:UltiSnipsEditSplit="vertical"

" Control vim window splits with Alt + Arrow
nmap <silent> <A-Up> :wincmd k<CR>
nmap <silent> <A-Down> :wincmd j<CR>
nmap <silent> <A-Left> :wincmd h<CR>
nmap <silent> <A-Right> :wincmd l<CR>
