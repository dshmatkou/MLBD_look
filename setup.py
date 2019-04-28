from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


with open('requirements.txt') as f:
    required = f.read().splitlines()


ext = Extension(
    'pyindex',
    [
        'pyindex.pyx',
        'index/index.cpp'
    ],
    language='c++',
    extra_compile_args=['-std=c++14'],
    include_dirs=['index'],
)


setup(
    name='web',
    version='0.1',
    packages=['web', 'feature_extractor'],
    license='MIT',
    cmdclass={'build_ext': build_ext},
    ext_modules=[ext],
    install_requires=required,
)
