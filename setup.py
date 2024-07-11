from setuptools import setup, find_packages

setup(
    name='devops-friend',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'devops-friend = devops_friend.main:main_function',
        ],
    },
    install_requires=[
        'argparse',     # For parsing command-line arguments
        'termcolor',    # For colored terminal output
        'rarfile'      # For working with RAR archives
    ],
    description='A helpful tool for DevOps tasks',
    author='Wisam idris',
    author_email='unknown@gmail.com', # I can't get my email address here
    url='https://github.com/wisamidris7/devops-friend',
)