from setuptools import setup

setup(name = "clean",
      version = "0.1.0",
      license='MIT',
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})