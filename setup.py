from setuptools import  setup, find_packages
import novelpia_python

VERSION = novelpia_python.__version__

def file(path: str) -> str:
    with open('README.md', encoding='utf8') as f:
        description = f.read()
    return description

setup(
    name="novelpia_python",
    version=VERSION,
    download_url=f"https://github.com/EricAn0630/novelpia-python/archive/{VERSION}.tar.gz",
    packages=find_packages(),
    author="Eric_An0630",
    author_email="soochan06@naver.com",
    url="https://github.com/EricAn0630/novelpia-python",
    description="노벨피아 비공식 라이브러리",
    long_description=file('README.md'),
    long_description_content_type="text/markdown",
    license="MIT License",python_reqires=">=3.6"
)