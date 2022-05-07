from setuptools import  setup, find_packages
import pypia

VERSION = pypia.__version__

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()


setup(
    name="pypia",
    version=VERSION,
    download_url=f"https://github.com/EricAn0630/novelpia-python/archive/{VERSION}.tar.gz",
    packages=find_packages(),
    author="Eric_An0630",
    author_email="soochan06@naver.com",
    url="https://github.com/EricAn0630/novelpia-python",
    description="노벨피아 비공식 라이브러리",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT License",
    python_reqires=">=3.6",
    install_requires=requirements
)
