source $ZSH/config.zsh
source $ZSH/keybinds.zsh
source $ZSH/aliases.zsh

function execifexists() {
	if [ -e $1 ]; then
		. "$1"
	else
		if [ -n "$2" ]; then
			echo "$2 not installed"
		else
			echo "$1 not installed"
		fi
	fi
}

function addtopathifexists() {
	if [[ -d "$1" ]]; then
		export PATH="$1:$PATH"
	fi
}

# Functions
function getnvm() {
	execifexists ~/.nvm/nvm.sh nvm
}
execifexists ~/.nvm/nvm.sh nvm

function getrvm() {
    execifexists ~/.rvm/scripts/rvm rvm
}
execifexists ~/.rvm/scripts/rvm rvm

# Zoxide
# TODO: exec only if installed

which zoxide >/dev/null 2>&1
ret=$?
if [[ $ret == 0 ]]; then
	eval "$(zoxide init zsh --cmd cd)"
fi

# Theme
source $ZSH/themes/minimal.zsh-theme

# bun completions
[ -s "/home/krop/.bun/_bun" ] && source "/home/krop/.bun/_bun"

# path updates
if [[ -z "$TMUX" ]]; then

	addtopathifexists ~/Android/Flutter/bin
	addtopathifexists ~/.local/share/JetBrains/Toolbox/scripts

	export BUN_INSTALL="$HOME/.bun"
	export PATH="$BUN_INSTALL/bin:$HOME/.cargo/bin:$HOME/.local/bin:/usr/local/go/bin:$PATH"
	export GOPATH="$HOME/Repositories/go"
fi
