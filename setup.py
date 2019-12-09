from os import path
from setuptools import setup

install_requires = [
    'phonenumbers'
]

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='bizarro',  # alternative name docket
      packages=['bizarro', 'bizarro.utility',
                'bizarro.template', 'bizarro..buttons'],
      version='1.0.2.alpha',
      description='',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/p1r-a-t3/FB_Bot',
      author='p1r-a-t3',
      author_email='ibtehaz.92@gmail.com',
      license='MIT',
      install_requires=[
          install_requires
      ],
      entry_points={
          'console_scripts': [
              'bizarro = bizarro.__init__:create_app'
          ]
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      zip_safe=False)
