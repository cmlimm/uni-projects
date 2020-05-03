from distutils.core import setup, Extension

modules = Extension(
	'matrixman',
	sources = ['python/matrix.c', 'c/base_matrix.c']
)

setup(
	name = 'matrixman',
	version = '0.1',
	description = 'Module dedicated to working with matrixes',
    author = 'Ekaterina Motyleva, Alexander Erofeevsky',
    author_email = 'example@ex.zone',
	ext_modules = [modules]
)
