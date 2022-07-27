# hurricanehrndz.rustup

[![Build Status][action-badge]][action-link]
[![Ansible Role][ansible-badge]][ansible-link]
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](https://raw.githubusercontent.com/hurricanehrndz/ansible-rustup/master/LICENSE)

Install rust and user defined cargo crates via rustup using `https://sh.rustup.rs`.

## Role Variables

| Variable Name            | Default Value      | Value Type | Description                                          |
| ------------------------ | ------------------ | ---------- | ---------------------------------------------------- |
| rustup_user              | root               | string     | Install rustup, and rust toolchain as defined value. |
| rustup_home_suffix       | .rustup            | string     | Install destination (~/ + suffix)                    |
| rustup_cargo_home_suffix | .cargo             | string     | Install destination (~/ + suffix)                    |
| rustup_cargo_crates      | [fd-find, ripgrep] | Array      | List of crates to install from cargo.                |
| rustup_configure_shell   | true               | Boolean    | Adds {HOME/.cargo/bin} to user's PATH                |

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: hurricanehrndz.rustup
```

## License

[MIT](LICENSE)

## Author Information

[Carlos Hernandez aka HurricaneHrndz](https://github.com/hurricanehrndz)

[ansible-badge]: https://img.shields.io/ansible/role/d/44247?style=for-the-badge
[ansible-link]: https://galaxy.ansible.com/hurricanehrndz/rustup
[action-badge]: https://img.shields.io/github/workflow/status/hurricanehrndz/ansible-rustup/CI?style=for-the-badge
[action-link]: https://github.com/hurricanehrndz/ansible-rustup/actions?query=workflow%3ACI
