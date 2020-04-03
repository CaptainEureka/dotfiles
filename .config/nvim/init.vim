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

  " Syntax
  Plug 'w0rp/ale'
  Plug 'hail2u/vim-css3-syntax'
  Plug 'numirias/semshi', {'do': ':UpdateRemotePlugins'}
  Plug 'vim-python/python-syntax'
  Plug 'kovetskiy/sxhkd-vim'

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
  Plug 'CaptainEureka/moonlight.vim'

  " Vim Cheatsheet
  Plug 'liuchengxu/vim-which-key'

  " Vim multi-cursor
  Plug 'terryma/vim-multiple-cursors'

  " UltiSnips vim snippets
  Plug 'SirVer/ultisnips'

  " Devicon glyphs for Nerdtree
  Plug 'ryanoasis/vim-devicons'

  " YAML support
  Plug 'stephpy/vim-yaml'

   " Hexokinase
   Plug 'RRethy/vim-hexokinase', { 'do': 'make hexokinase' }

  " Commentary (auto comment)
  Plug 'tpope/vim-commentary'

  " Tabular (easy vertical alignment)
  Plug  'godlygeek/tabular' 
  
  " QuickScope easy hoirzontal motions
  Plug 'unblevable/quick-scope'

  " Goyo minimal distraction free writing (고요)
  Plug 'junegunn/goyo.vim'

  call plug#end()

set encoding=UTF-8

filetype plugin indent on

" Configurations Part"

" UI configuration
syntax on
syntax enable

" True Color Support if it's avaiable in terminal
if has("termguicolors")
   set termguicolors
endif

" colorscheme
set background=dark
" colorscheme wal
colorscheme moonlight

" Italics for moonlight
let g:moonlight_terminal_italics = 1

" Italics for palenight
"let g:palenight_terminal_italics = 1

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
let g:airline_theme = 'moonlight' 

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

" Hexokinase configuration
let g:Hexokinase_highlighters = ['backgroundfull']
" let g:Hexokinase_highlighters = [ 'virtual' ]
let g:Hexokinase_optInPatterns = 'full_hex,rgb,rgba,hsl,hsla,colour_names'

" vim-python/python syntax
let g:python_highlight_all = 1

" Semshi semantic python syntax
let g:semshi#filetypes = ['python']
let g:semshi#excluded_hl_groups = ['local']
let g:semshi#mark_selected_nodes = 1
let g:semshi#no_default_builtin_highlight = v:true
let g:semshi#simplify_markip = v:true
let g:semshi#error_sign = v:true
let g:semshi#error_sign_delay = 1.5
let g:semshi#always_update_all_highlights = v:false
let g:semshi#tolerate_syntax_errors = v:true
let g:semshi#update_delat_factor = 0.0

function MyCustomSemshiHighlights()
    hi semshiLocal           ctermfg=209 guifg=#ff757f
	hi semshiGlobal          ctermfg=214 guifg=#ff995e
	hi semshiImported        ctermfg=214 guifg=#ff995e cterm=bold gui=bold
	hi semshiParameter       ctermfg=75  guifg=#82aaff
	hi semshiParameterUnused ctermfg=117 guifg=#86e1fc cterm=underline gui=underline
	hi semshiFree            ctermfg=218 guifg=#fca7ea
	hi semshiBuiltin         ctermfg=207 guifg=#c597f9
	hi semshiAttribute       ctermfg=49  guifg=#4fd6be
	hi semshiSelf            ctermfg=249 guifg=#a9b8e8
	hi semshiUnresolved      ctermfg=226 guifg=#c3e88d cterm=underline gui=underline
	hi semshiSelected        ctermfg=231 guifg=#ffffff ctermbg=161 guibg=#ff5370

	hi semshiErrorSign       ctermfg=231 guifg=#ffffff ctermbg=160 guibg=#ff2046
	hi semshiErrorChar       ctermfg=231 guifg=#ffffff ctermbg=160 guibg=#ff2046
    sign define semshiError text=E> texthl=semshiErrorSign
endfunction
autocmd FileType python call MyCustomSemshiHighlights()

" QuickScope configuration
let g:qs_highlight_on_keys = ['f', 'F', 't', 'T']
augroup qs_colors
  autocmd!
  autocmd ColorScheme * highlight QuickScopePrimary guifg='#c3e88d' gui=underline ctermfg=155 cterm=underline
  autocmd ColorScheme * highlight QuickScopeSecondary guifg='#86e1fc' gui=underline ctermfg=81 cterm=underline
augroup END
