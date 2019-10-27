# hurricanehrndz.rustup

[![Build Status](https://img.shields.io/travis/hurricanehrndz/ansible-rustups/master.svg?style=for-the-badge&logo=travis)](https://travis-ci.org/hurricanehrndz/ansible-rustup)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](https://raw.githubusercontent.com/hurricanehrndz/ansible-rustup/master/LICENSE)

Install rust and user defined cargo crates via rustup using `https://sh.rustup.rs`.

## Role Variables

|Variable Name           |Default Value     |Value Type |Description                                         |
|---                     |---               |---        |---                                                 |
|rustup_user             |root              |string     |Install rustup, and rust toolchain as defined value.|
|rustup_cargo_crates     |[fd-find, ripgrep]|Array      |List of crates to install from cargo.               |
|rustup_config_user_shell|true              |Boolean    |Adds {HOME/.cargo/bin} to user's PATH               |

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: ansible-rustup
```

## License

[MIT](LICENSE)

## Author Information

[Carlos Hernandez aka HurricaneHrndz](https://github.com/hurricanehrndz)
