{pkgs, ...}: {
  env.GREET = "ansible-rustup role's dev environment";

  packages = with pkgs; [
    git
  ];

  scripts.hello.exec = "echo Welcome to $GREET";

  enterShell = ''
    hello
  '';

  languages.python = {
    enable = true;
    poetry.enable = true;
  };

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}
