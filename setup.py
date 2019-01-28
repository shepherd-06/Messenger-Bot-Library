from setuptools import setup

install_requires = [
    'Zathura',
]

setup(name='bizarro',  # alternative name docket
      packages = ['BotLib'],
      version='0.0.1.dev1',
      description='',
      url='https://github.com/ibtehaz-shawon/bizarro',
      author='Ibtehaz Shawon',
      author_email='ibtehaz.92@gmail.com',
      license='MIT',
      install_requires=[
            install_requires
      ],
      entry_points={
        'console_scripts': [
            'bizarro = BotLib.__init__:create_app'
        ]
        },
       classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
      zip_safe=False)
