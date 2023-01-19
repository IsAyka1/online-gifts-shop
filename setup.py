from pkg_resources import parse_requirements
from setuptools import setup


def load_requires(file_name: str) -> list:
    requirements = []
    with open(file_name, 'r') as fp:
        for req in parse_requirements(fp.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


setup(packages=load_requires('requirements.txt'), extract_require={'dev': load_requires('requirements.dev.txt')})
