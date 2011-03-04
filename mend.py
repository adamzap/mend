#!/usr/bin/env python

import os
import shutil
import jinja2

try:
    EXTS, DIRS = [l.strip().split(' ') for l in open('mend.conf').readlines()]
except IOError:
    EXTS, DIRS = [], []

try:
    shutil.rmtree('deploy')
except OSError:
    pass

base_tmpl = jinja2.Template(open('base.html').read())

os.mkdir('deploy')

for page_name in os.listdir('.'):
    if page_name.split('.')[-1] not in EXTS or page_name == 'base.html':
        continue

    title = page_name.split('.')[0].replace('_', ' ').title()
    body = open(page_name).read()

    rendered_file = open(os.path.join('deploy', page_name), 'w')
    rendered_file.write(base_tmpl.render(locals()))
    rendered_file.close()

for dir in DIRS:
    shutil.copytree(dir, os.path.join('deploy', dir))
