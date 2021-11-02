# -*- coding: utf-8 -*-
# Copyright (c) 2012 by Pablo Martín <goinnn@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this programe.  If not, see <http://www.gnu.org/licenses/>.



import codecs
import os
from setuptools import setup, find_packages


def read(*rnames):
    with codecs.open(
        os.path.join(os.path.dirname(__file__), *rnames),
        'r', 'utf-8',
    ) as f:
        return f.read()


setup(
    name="django-customselectwidget",
    version="0.1.1",
    author="Sayed Hisham",
    author_email="hisham2k9@gmail.com",
    url="https://github.com/hisham2k9/django-customselectwidget",
    description="Django Custom select widget",
    long_description=(read('README.rst')),
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        
    ],
    license="LGPL 3",
    keywords="django,custom,select,field,choices,widget",
    packages=find_packages(),
    include_package_data=True,
    tests_require=[
        'django>=2.0',
        'tox',
        'coverage',
        'flake8',
    ],
    install_requires=[
        'django>=2.0',
    ],
    zip_safe=False,
)