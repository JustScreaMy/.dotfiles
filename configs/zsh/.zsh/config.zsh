fpath+=$ZSH/completions
fpath+=/home/krop/.local/pipx/venvs/argcomplete/lib64/python3.11/site-packages/argcomplete/bash_completion.d

#zshconf
autoload -Uz vcs_info
autoload -U compinit; compinit -d $ZSH/.zcompdump
setopt auto_menu
setopt complete_in_word
setopt always_to_end


# zstyle command format
# zstyle :<namespace>:<function>:<completer>:<command>:<argument>:<tag> <style> <value>
zstyle ':completion:*' menu select
zstyle ':completion:*' special-dirs true
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'r:|=*' 'l:|=* r:|=*'
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path "$ZSH/.zsh/.zcompcache"


# History config
export HISTFILE=$ZSH/.zsh_history
export HISTSIZE=10000
export SAVEHIST=10000
setopt HIST_SAVE_NO_DUPS


# Editor config
export EDITOR=$(which micro)

# Theme
source $ZSH/themes/minimal.zsh-theme
