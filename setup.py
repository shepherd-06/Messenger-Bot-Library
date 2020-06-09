from os import path
from setuptools import setup

install_requires = [
    'phonenumbers'
]

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='messenger_bot_library',  # alternative name docket
      packages=['messenger_bot', 'messenger_bot.utility',
                'messenger_bot.template', 'messenger_bot.buttons'],
      version='2.0.1.beta',
      description='A python package that helps you to create payload for facebook messenger bot.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/p1r-a-t3/Messenger-Bot-Library',
      author='p1r-a-t3',
      author_email='ibtehaz.92@gmail.com',
      license='MIT',
      install_requires=[
          install_requires
      ],
      entry_points={
          'console_scripts': [
              'messenger_bot = messenger_bot.__init__:create_app'
          ]
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      zip_safe=False)
