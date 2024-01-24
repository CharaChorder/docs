{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {inherit system;};
    in {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          python311
          python311Packages.sphinx
          python311Packages.sphinx-autobuild
          python311Packages.sphinx-rtd-theme
          python311Packages.sphinx-design
          python311Packages.myst-parser
        ];
      };
    });
}
