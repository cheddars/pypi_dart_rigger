import setuptools

setuptools.setup(
    name="dartrig",
    version="0.0.2",
    license='MIT',
    author="cheddars",
    author_email="nezahrish@gmail.com",
    description="dart api wrapper",
    long_description=open('README.md').read(),
    url="https://github.com/cheddars/dart_rigger",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)