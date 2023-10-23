source $ZSH/config.zsh
source $ZSH/keybinds.zsh
source $ZSH/aliases.zsh

execifexists() {
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

# Functions
getnvm() {
	execifexists ~/.nvm/nvm.sh nvm
}

getrvm() {
    execifexists ~/.rvm/scripts/rvm rvm
}

getpgadmin() {
	podman run -p8080:80 -ePGADMIN_DEFAULT_EMAIL=krop@krop.cz -ePGADMIN_DEFAULT_PASSWORD=krop --rm dpage/pgadmin4
}

# path updates
if [[ -z "$TMUX" ]]; then
	export BUN_INSTALL="$HOME/.bun"
	export PATH="$BUN_INSTALL/bin:$HOME/.cargo/bin:$HOME/.local/bin:$HOME/.local/share/JetBrains/Toolbox/scripts:/usr/local/go/bin:$PATH"
	export GOPATH="$HOME/Repositories/go"
fi
