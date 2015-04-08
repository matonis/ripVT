from setuptools import setup, find_packages

setup(
    name='ripVT',
    author='@matonis',
    version='1.0',
    author_email='dfir.matonis@gmail.com',
    description='VT transforms',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
