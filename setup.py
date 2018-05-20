import setuptools


setuptools.setup(
    name='jenkins-test',
    version='0.0.1',

    author='Max Zheng',
    author_email='maxzheng.os @t gmail.com',

    description='Test project for Jenkins',
    long_description=open('README.md').read(),

    url='https://github.com/maxzheng/jenkins-test',

    install_requires=open('requirements.txt').read(),

    license='MIT',

    packages=setuptools.find_packages(),
    include_package_data=True,

    setup_requires=['setuptools-git'],

    # entry_points={
    #    'console_scripts': [
    #        'script_name = package.module:entry_callable',
    #    ],
    # },

    classifiers=[
      'Development Status :: 5 - Production/Stable',

      'Intended Audience :: Developers',
      'Topic :: Software Development :: Testing',

      'License :: OSI Approved :: MIT License',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],

    keywords='<KEYWORDS>',
)
