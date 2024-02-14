{
  description = "My Blog built with Hugo";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/release-23.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        pythonEnv = pkgs.python3.withPackages (ps: with ps; [
          arrow
          python-frontmatter
          pytz
          sqlite-utils
        ]);
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            pythonEnv
            hugo
          ];
        };
      });
}
