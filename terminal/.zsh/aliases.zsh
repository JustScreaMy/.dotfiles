alias lg='lazygit'
alias cls='clear'
alias open='xdg-open'
alias fire='firefox'
#alias s='kitty +kitten ssh'
alias la='ls -al --color=auto'

# Git
alias gs='git status'
alias ga='git add'
alias gaa='git add --all'

# Cargo
alias cg-run='cargo run'
alias cg-build='cargo build'
alias cg-test='cargo test'


# Docker Compose
alias dc='docker compose'
alias dc-build='dc build'
alias dc-run='dc run --rm'
alias dc-runr='dc-run -u root'
alias dc-up='dc up'
alias dc-upd='dc up -d'
alias dc-down='dc down'
alias dc-ls='dc ls'
alias dc-pull='dc pull'

# Docker Stack
alias ds-env='env $(cat .env | grep "^[A-Z]" | xargs) docker stack'

# Navigation
alias ..='cd ..'

# Bitwarden
alias bw-unlock='BW_SESSION=$(bw unlock --raw) && export BW_SESSION'

# tmux
alias t="tmux"
