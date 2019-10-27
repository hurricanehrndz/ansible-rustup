import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_rustup_bin(host, scenario):
    user_home = scenario.get_user_home()
    binary = host.file(f"{user_home}/.cargo/bin/rustup")

    assert binary.exists
    assert binary.mode == 0o755


@pytest.mark.parametrize("crate_name", [
    "fd",
    "rg"
])
def test_rust_crates(host, crate_name, scenario):
    user_home = scenario.get_user_home()
    crate_path = f"{user_home}/.cargo/bin/{crate_name}"
    crate = host.file(crate_path)

    assert crate.exists
    assert crate.mode == 0o755


@pytest.mark.parametrize("system_package", [
    "make",
    "curl",
    "gcc"
])
def test_systems_packages(host, system_package):
    pkg = host.package(system_package)

    assert pkg.is_installed


def test_rustrc(host, scenario):
    user_home = scenario.get_user_home()
    rc = host.file(f"{user_home}/.rustrc")

    assert rc.exists


def test_bashrc(host, scenario):
    user_home = scenario.get_user_home()
    rc = host.file(f"{user_home}/.bashrc")
    rc_content = rc.content_string

    assert f"source {user_home}/.rustrc" in rc_content
