let g:plugged_home = '~/.config/nvim/plugged'

" Plugins List
call plug#begin(g:plugged_home)

" UI related
Plug 'itchyny/lightline.vim'
Plug 'scrooloose/nerdtree'

" Better Visual Guide
Plug 'Yggdroot/indentLine'

" Syntax
Plug 'numirias/semshi', {'do': ':UpdateRemotePlugins'}
Plug 'kovetskiy/sxhkd-vim'
Plug 'sheerun/vim-polyglot'
Plug 'pearofducks/ansible-vim'

" Intellisense Autocomplete
Plug 'neoclide/coc.nvim', {'branch': 'release'}

" FZF file finder
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Formatter
Plug 'Chiel92/vim-autoformat'

" Themes
Plug 'drewtempelmeyer/palenight.vim'
Plug 'CaptainEureka/moonlight.vim'
Plug 'altercation/vim-colors-solarized'
Plug 'arzg/vim-substrata'
Plug 'ntk148v/vim-horizon'
Plug 'dylanaraps/wal.vim'
Plug 'morhetz/gruvbox'

" UltiSnips vim snippets
Plug 'SirVer/ultisnips'

" Devicon glyphs for Nerdtree
Plug 'ryanoasis/vim-devicons'

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
colorscheme wal

" Tokyo-Night
" let g:tokyonight_style = 'night' " available: night, storm
" let g:tokyonight_transparent_background = 1
" colorscheme tokyonight

hi Normal guibg=NONE ctermbg=NONE

" Italics for moonlight
" let g:moonlight_terminal_italics = 1

" Italics for palenight
"let g:palenight_terminal_italics = 1

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
" let g:Hexokinase_highlighters = [ 'virtual' ]
let g:Hexokinase_optInPatterns = 'full_hex,rgb,rgba,hsl,hsla,colour_names'

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

" QuickScope configuration
let g:qs_highlight_on_keys = ['f', 'F', 't', 'T']
augroup qs_colors
  autocmd!
  autocmd ColorScheme * highlight QuickScopePrimary guifg='#c3e88d' gui=underline ctermfg=155 cterm=underline
  autocmd ColorScheme * highlight QuickScopeSecondary guifg='#86e1fc' gui=underline ctermfg=81 cterm=underline
augroup END

" LUA syntax
let g:lua_syntax_someoption = 1 
