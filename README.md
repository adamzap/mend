# Mend

`mend` is a simple static site generator that I use for a few projects.

- Create a base.html jinja2 template
- Create html or md (markdown) files that will inherit from base.html
- Put all media (css, js, images, etc) in one or more folders
- Run `mend`
- View your newly created site in the `deploy` directory

## Requirements

Python modules:

- `jinja2`
- `markdown`

## Setup

`$ ln -s /path/to/mend.py /usr/local/bin/mend`

## Usage

`$ mend`
