from pyinfra.api import deploy
from pyinfra.operations import dnf


@deploy("Deploy packages")
def deploy_packages():
    docker = [
        "docker-ce",
        "docker-ce-cli",
        "containerd.io",
        "docker-buildx-plugin",
        "docker-compose-plugin",
    ]

    cli_apps = [
        "zsh",
        "tmux",
        "lazygit",
        "lazydocker",
        "zoxide",
        "terraform",
        "vagrant",
        "code",
        "trivy",
        "tailscale",
        "rsync",
        "python3.11",
        "python3.10",
        "podman-compose",
        "fzf",
        *docker,
    ]

    dnf.packages(
        name="Installing cli applications",
        packages=cli_apps,
        _sudo=True,
    )

    gui_apps = [
        "ulauncher",
        "alacritty",
    ]

    dnf.packages(
        name="Installing gui applications",
        packages=gui_apps,
        _sudo=True,
    )

    # TODO: add flatpaks too


"""
ansible-core 2.17.0
argcomplete 3.3.0
babi 1.5.6
bandit 1.7.8
black 24.4.2
bumpver 2023.1129
cookiecutter 2.6.0
invoke 2.2.0
ipython 8.25.0
mercurial 6.7.3
meson 1.4.1
ninja 1.11.1.1
notebook 7.2.1
nox 2024.4.15
pip-run 12.6.1
poetry 1.8.3
pre-commit 3.7.1
python-lsp-server 1.11.0
random-scripts 0.2.0
reorder-python-imports 3.13.0
ruff 0.4.8
tox 4.15.1
uv 0.2.10
virtualenv 20.26.2
wlc 1.14
"""
