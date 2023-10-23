DOT_CONFIG_DIR = "~/.config"

mountpoints = {
    "alacritty": {"path": f"{DOT_CONFIG_DIR}/alacritty", "type": "dir"},
    "git": {"path": f"{DOT_CONFIG_DIR}/git", "type": "dir"},
    "gtk-3.0": {"path": f"{DOT_CONFIG_DIR}/gtk-3.0", "type": "dir"},
    "gtk-4.0": {"path": f"{DOT_CONFIG_DIR}/gtk-4.0", "type": "dir"},
    "micro": {"path": f"{DOT_CONFIG_DIR}/micro", "type": "dir"},
    "tmux": {"path": f"{DOT_CONFIG_DIR}/tmux", "type": "dir"},
    "zsh/.zsh": {"path":"~/.zsh", "type": "dir"},
    "zsh/.zshenv":{"path":"~/.zshenv","type": "file"},
}