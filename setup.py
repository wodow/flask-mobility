import os
import re
from setuptools import setup


ROOT = os.path.abspath(os.path.dirname(__file__))
VERSIONFILE = os.path.join('flask_mobility', '_version.py')
VSRE = r"""^__version__ = ['"]([^'"]*)['"]"""


def get_version():
    verstrline = open(VERSIONFILE, 'rt').read()
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError(
            'Unable to find version string in {0}.'.format(VERSIONFILE))


setup(
    name='Flask-Mobility',
    version=get_version(),
    url='http://github.com/rehandalal/flask-mobility/',
    license='BSD',
    author='Rehan Dalal',
    author_email='rehan@meet-rehan.com',
    description='A Flask extension to simplify building mobile-friendly sites.',
    long_description=open(os.path.join(ROOT, 'README.rst')).read(),
    packages=['flask_mobility'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'user-agents >= 0.2.0',
    ],
    test_suite='flask_mobility.tests.suite',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
