from setuptools import setup
import subprocess


setup(name='scwoaservices',
      version=(subprocess.check_output(['git', 'describe', '--tag'])
               .strip()
               .decode('ascii')
               .replace('-', '_')),
      packages=['scwoaservices', 'scwoaservices/tools'],
      include_package_data=True,
      zip_safe=False)
