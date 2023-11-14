from setuptools import setup, find_packages

setup(
    name='src',
    version='0.1.14',
    keywords='wheel',
    description='a library for Python wheel',
    license='MIT License',
    url='https://github.com/jiangxiaoqiang/rdpywheel',
    author='jiangxiaoqiang',
    author_email='jiangtingqiang@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[],
)