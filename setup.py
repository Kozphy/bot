from setuptools import setup
from constants import BOT_NAME

setup(
    name=BOT_NAME,
    version='0.1.0',
    py_modules=[BOT_NAME],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            f'{BOT_NAME} = {BOT_NAME}:cli',
        ],
    },
)