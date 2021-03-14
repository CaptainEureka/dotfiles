let g:plugged_home = '~/.config/nvim/plugged'

" Plugins List
call plug#begin(g:plugged_home)

" UI related
Plug 'itchyny/lightline.vim'
Plug 'scrooloose/nerdtree'

" Better Visual Guide
Plug 'Yggdroot/indentLine'

" Syntax
Plug 'sheerun/vim-polyglot'

" Intellisense Autocomplete
Plug 'neoclide/coc.nvim', {'branch': 'release'}

" FZF file finder
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Formatter
Plug 'Chiel92/vim-autoformat'

" Themes
Plug 'arcticicestudio/nord-vim'
Plug 'morhetz/gruvbox'
Plug 'dylanaraps/wal.vim'
Plug 'rayes0/blossom.vim'

" UltiSnips vim snippets
Plug 'SirVer/ultisnips'

" Devicon glyphs for Nerdtree
Plug 'ryanoasis/vim-devicons'

" Hexokinase
Plug 'RRethy/vim-hexokinase', { 'do': 'make hexokinase' }

" Commentary (auto comment)
Plug 'tpope/vim-commentary'

" Tabular (easy vertical alignment)
Plug 'godlygeek/tabular'

" QuickScope easy horizontal motions
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
colorscheme blossom

hi Normal guibg=NONE ctermbg=NONE

" set number
" set relativenumber
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
set tabstop=2
set shiftwidth=2

" FZF keybindings
noremap <C-f> :Files<CR>

" vim-autoformat
noremap <F3> :Autoformat<CR>

" NERDTree configs
map <C-t> :NERDTreeToggle<CR>
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'

" Lightline
let g:lightline = {
      \ 'colorscheme': 'wal',
      \ }

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
let g:Hexokinase_optInPatterns = 'full_hex,rgb,rgba,hsl,hsla,colour_names'

" QuickScope configuration
let g:qs_highlight_on_keys = ['f', 'F', 't', 'T']
