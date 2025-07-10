from setuptools import setup, find_packages

setup(
    name="drf-common-exceptions",
    version="0.1.0",
    description="Reusable custom exception handler for Django REST Framework",
    author="Shabbir Habib",
    author_email="84226838+shabbir98@users.noreply.github.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=3.2",
        "djangorestframework>=3.12",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
