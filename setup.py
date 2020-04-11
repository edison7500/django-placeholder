from setuptools import setup

import placeholder

with open("README.md") as readme_file:
    readme = readme_file.read()

install_requires = (["Django>=2.2", "pillow>=6.0.0"],)

setup(
    name="django-placeholder",
    version=placeholder.__version__,
    description="""Django PlaceHolder""",
    long_description=readme,
    packages=[
        "placeholder",
        "placeholder.management",
        "placeholder.management.commands",
    ],
    install_requires=install_requires,
    include_package_data=True,
    license="GNU License",
    zip_safe=False,
    keywords="django-geoip",
)
