from setuptools import setup, find_packages

setup(
    name="backend",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'flask-cors',
        'mysqlclient',
        'flask-sqlalchemy',
        'passlib',
        'flask-httpauth',
        'itsdangerous'
    ]
)
