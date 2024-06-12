from pyinfra.api import deploy
from pyinfra.operations import dnf
from pyinfra.operations import server


@deploy("Deploy packages")
def install_packages():
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

    pipx_packages = [
        "ansible-core",
        "bumpver",
        "cookiecutter",
        "invoke",
        "mercurial",
        "meson ",
        "ninja",
        "notebook",
        "nox",
        "pip-run",
        "poetry",
        "pre-commit",
        "python-lsp-server",
        "ruff",
        "tox",
        "uv",
        "virtualenv",
        "wlc",
    ]

    server.shell(
        name="Install pipx cli utils",
        commands=[
            f"pipx install {name}" for name in pipx_packages
        ],
    )


"""

"""
