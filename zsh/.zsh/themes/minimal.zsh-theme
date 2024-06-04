precmd() { vcs_info }

setopt PROMPT_SUBST

zstyle ':vcs_info:git:*' formats '[%b] '
if [[ -n "$SSH_TTY" ]]
then
	PROMPT='(SSH) %2~ ${vcs_info_msg_0_}»%b '
else
	PROMPT='%2~ ${vcs_info_msg_0_}»%b '
fi
