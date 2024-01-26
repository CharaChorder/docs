# docs

CharaChorder documentation

## Dependencies

Install `sphinx`, `sphinx_rtd_theme`, `sphinx-design`, and `myst-parser` using `pip` or your preferred package manager.

```sh
pip install sphinx sphinx_rtd_theme myst-parser sphinx-design
```

### Nix/NixOS

With flakes enabled, run `nix develop` or use [nix-direnv](https://github.com/nix-community/nix-direnv) with `direnv allow`

## Development

For development, you should also install `sphinx-autobuild` and then start the dev server using

```sh
sphinx-autobuild docs _build
```

## Building

```sh
sphinx-build docs _build
```

## Adding a new top level page

If you are adding or editing an under construction top level page, make sure to
add it to index.rst if you'd like to have it shown on the left side bar.

## Linking

.. \_Slow Speed: = Anchor to same section in same doc
:ref:`slow speed <Slow Speed>` = link to anchor

## Tables

.. csv-table::
:header: "Device", "Default", "Min. Value", "Max. Value", "Increments"

    "CharaChorder One", ""
    "CharaChorder Lite", ""
    "CharaChorder X", ""
    "CharaChorder Engine", ""

## Dropdown

.. dropdown:: Title of the Dropdown, visible with the DD closed.

    Text inside the dropdown should skip a line then indent once (4 spaces).

## Images

.. \_Reference Name:
.. image:: /assets/images/PATH-TO-IMAGE.jpg
:width: 1200
:alt: Alt text for screen readers
