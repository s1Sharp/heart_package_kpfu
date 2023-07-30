"""Скрипт Setup.py для проекта по упаковке."""

import os

from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def read_dependencies(fname):
    """Получаем зависимости по умолчанию."""
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as f:
        return [dependency.rstrip() for dependency in f.readlines()]


if __name__ == '__main__':
    setup(
        name='heart_package_kpfu',
        version=os.getenv('PACKAGE_VERSION', '0.0.1'),
        packages=find_packages(include=[
            'heart_package_kpfu', 'heart_package_kpfu.*'
        ]),
        python_requires='>=3.10',
        description='A demo package.',
        install_requires=read_dependencies('requirements.txt'),
    )
