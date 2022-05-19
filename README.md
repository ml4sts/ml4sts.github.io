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


These pages use [sphinx panels]().  Add yourself at the top of the relevant section.

```

:column: col-4

NAME

^^^

Role and optional bio
+++

{link-badge}`https://github.com/gh-username,"GitHub",cls=badge-dark text-white`

---

```

Formatting notes:
- The `^^^` separates your name/title from the body
- `+++` separates the links from the body
- `---` spearates people/projects

For the link badges, look at others on the page to see style conventions.  
```
{link-badge}`http://url/to/site/,"text to display",cls=style-info`
```
