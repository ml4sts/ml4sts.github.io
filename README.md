# ML4STS lab website

This is our lab website, built with Sphinx! Based on [Chris Holdgraf's](https://github.com/choldgraf/choldgraf.github.io)


The easiest way to build the website is to use `nox`, which handles all of the environment generation automatically.
To do so, follow these steps:

1. Install `nox`.

   ```shell
   pip install -U nox
   ```
2. Run `tox`

   ```shell
   nox -s docs
   ```

this should install a Sphinx environment and build the site, putting the output files in `_build/html`.

To run a live webserver that will auto-build and reload when you make changes, run:

```shell
nox -s docs-live
```

## Add a Person or Project

Follow the new member code tour using vscode. 
