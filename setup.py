from setuptools import setup

def slurp(path):
    with open(path) as infile:
        return infile.read()

setup(
    name='gentools',
    version='0.1',
    description='The next generation of GNU Autotools',
    long_description=slurp('README.rst'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Text Processing :: Markup :: XML',
    ],
    keywords='gentools build',
    url='https://github.com/dutch/gentools',
    author='Chris Lamberson',
    author_email='clamberson@gmail.com',
    license='GPLv3+',
    packages=['gentools'],
    install_requires=['lxml'],
    entry_points={
        'console_scripts': [
            'genconf=gentools.command_line:genconf',
        ]
    },
    include_package_data=True,
    zip_safe=False
)
