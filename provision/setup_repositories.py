from pyinfra.api import deploy
from pyinfra.operations import dnf
from pyinfra.operations import server


@deploy("Deploy repositories")
def setup_repos():
    required_packages = [
        "dnf-plugins-core",
    ]

    dnf.packages(
        name="Installing required packages for repo setup",
        packages=required_packages,
        update=True,
        _sudo=True,
    )

    coprs = [
        "atim/lazygit",
        "atim/lazydocker",
    ]

    server.shell(
        name="Installing coprs",
        commands=[
            f"dnf copr enable -y {copr}" for copr in coprs
        ],
        _sudo=True,
    )

    repo_cfg_manager = [
        ("Docker", "https://download.docker.com/linux/fedora/docker-ce.repo"),
        ("Tailscale", "https://pkgs.tailscale.com/stable/fedora/tailscale.repo"),
        ("HashiCorp", "https://rpm.releases.hashicorp.com/fedora/hashicorp.repo"),
    ]

    for repo_name, repo in repo_cfg_manager:
        dnf.repo(
            name=f"Adding {repo_name} repository",
            src=repo,
            _sudo=True,
        )

    repo_url = [
        {
            "name": "trivy", "baseurl": "https://aquasecurity.github.io/trivy-repo/rpm/releases/$basearch/",
            "gpgkey": "https://aquasecurity.github.io/trivy-repo/rpm/public.key",
        },
        {
            "name": "vscode", "baseurl": "https://packages.microsoft.com/yumrepos/vscode",
            "gpgkey": "https://packages.microsoft.com/keys/microsoft.asc",
        },
    ]

    for repo in repo_url:
        dnf.repo(
            name=f"Adding {repo.get('name')} repository",
            src=repo.get("name"),
            baseurl=repo.get("baseurl"),
            gpgcheck=repo.get("gpgcheck", True),
            gpgkey=repo.get("gpgkey"),
            _sudo=True,
        )
