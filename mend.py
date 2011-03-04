#!/usr/bin/env python

import os
import shutil
import jinja2
import markdown

IGNORE = ('base.html', 'deploy')

base_tmpl = jinja2.Template(open('base.html').read())

md = markdown.Markdown()

try:
    shutil.rmtree('deploy')
except OSError:
    pass

os.mkdir('deploy')

ls = [x for x in os.listdir('.') if not x[0] == '.' and x not in IGNORE]

for page_name in [x for x in ls if os.path.isfile(x)]:
    title = page_name.split('.')[0].replace('_', ' ').title()
    body = open(page_name).read()

    if page_name.endswith('.md'):
        body = md.convert(body)
        page_name = page_name.replace('.md', '.html')

    rendered_file = open(os.path.join('deploy', page_name), 'w')
    rendered_file.write(base_tmpl.render(locals()))
    rendered_file.close()

for dir in [x for x in ls if os.path.isdir(x)]:
    shutil.copytree(dir, os.path.join('deploy', dir))
