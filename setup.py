#!/usr/bin/env python
from setuptools import setup


__version__ = "$Id: setup.py 49 2018-04-23 08:14:29Z lbusoni $"



setup(name='tipico',
      description='useless client of a simulated device with PLICO',
      version='0.11',
      classifiers=['Development Status :: 4 - Beta',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ],
      long_description=open('README.md').read(),
      url='',
      author_email='lbusoni@gmail.com',
      author='Lorenzo Busoni',
      license='',
      keywords='plico, laboratory, instrumentation control',
      packages=['tipico',
                'tipico.calibration',
                'tipico.client',
                'tipico.gui',
                'tipico.types',
                'tipico.utils',
                ],
      entry_points={
          'gui_scripts': [
              'tipico_basic_pyqt5_gui=tipico.gui.basic_pyqt5:main',
              'tipico_basic_pyside2_gui=tipico.gui.basic_pyside2:main',
              'tipico_basic_qt_gui=tipico.gui.basic_qt:main',
          ],
      },
      package_data={
          'tipico': ['conf/tipico.conf'],
      },
      install_requires=["plico>=0.14",
                        "numpy",
                        "psutil",
                        "configparser",
                        "six",
                        "appdirs",
                        "pyfits",
                        "futures",
                        'pyside2',
                        "Qt.py",
                        "pathlib2; python_version < '3'"
                        ],
      include_package_data=True,
      test_suite='test',
      )
