precmd() {
    vcs_info
    is_toolbx_container
}

setopt PROMPT_SUBST

zstyle ':vcs_info:git:*' formats '[%b] '

is_toolbx_container() {
    if [[ -f /run/.containerenv ]]; then
        CONTAINER_NAME=$(grep -oP 'name="\K[^"]+' /run/.containerenv)
        TOOLBX_INDICATOR="[%F{magenta}${CONTAINER_NAME}%f] "
    else
        TOOLBX_INDICATOR=""
    fi
}

PROMPT='%2~ ${TOOLBX_INDICATOR}${vcs_info_msg_0_}»%b '
# RPROMPT='%D{%I:%M:%S %p}'
