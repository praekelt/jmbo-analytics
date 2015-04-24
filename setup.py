from setuptools import setup, find_packages


setup(
    name='jmbo-analytics',
    version='0.1',
    description='Jmbo analytics app.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/jmbo-analytics',
    packages = find_packages(),
    install_requires = [
        'django<1.7',
        'django-celery',
        'httplib2',
    ],
    include_package_data=True,
    tests_require=[
        'django-setuptest>=0.1.4',
        'psycopg2'
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
