from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Useful programm to clean and sort your files and folders',
    author = 'Oleksandr Frolov',
    author_email='alexandrgreat07@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean:main']},

    license='MIT'
)
