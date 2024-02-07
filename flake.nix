{
  description = "My Blog built with Hugo";
  inputs.nixpkgs.url = "github:nixos/nixpkgs/release-23.11";

  outputs = inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = inputs.nixpkgs.lib.systems.flakeExposed;

      perSystem = { self', pkgs, ... }:
        let
          inherit (pkgs) hugo python3;
          pythonEnv = pkgs.python3.withPackages (ps: with ps; [ arrow python-frontmatter pytz sqlite-utils ]);
        in
        {
          devShells.default = pkgs.mkShell {
            buildInputs = [ hugo pythonEnv ];
          };
        };
    };
}