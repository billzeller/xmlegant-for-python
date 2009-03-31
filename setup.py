from setuptools import setup

import sys
if sys.hexversion < 0x02050200:
   raise RuntimeError, "Python 2.5.2 or higher required"


setup(name='XMLegant',
      version='0.8.1',
	  description='A class allowing easy XML generation',
	  #summary='A class allowing easy XML generation. XML can be generated using chaining methods or a succinct accessor syntax.',
	  author='Bill Zeller',
	  author_email='billiam@gmail.com',
	  url='http://xmlegant.from.bz',
	  license='BSD',
      py_modules=['XMLegant'],
      classifiers   = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: XML',
        ],
      
	  )


