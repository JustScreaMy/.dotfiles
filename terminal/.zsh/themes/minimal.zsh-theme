precmd() { vcs_info }

setopt PROMPT_SUBST

zstyle ':vcs_info:git:*' formats '[%b] '

PROMPT='%2~ ${vcs_info_msg_0_}»%b '
# RPROMPT='%D{%I:%M:%S %p}'
