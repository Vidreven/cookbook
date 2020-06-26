from setuptools import setup, find_packages

setup(
    name="cookbook",
    version="0.3.2",
    author="Vidreven",
    description="Store, read, edit, comment and search your favorite recipes.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="MIT license",
    install_requires=["setuptools>=46.1.3", "click>=7.1.2"],
    extras_require={"dev": ["pytest>=5.4.1", "pre-commit>=2.5.1"]},
    entry_points="""
        [console_scripts]
        cookbook=cookbook.cookbook:cookbook
    """,
)
