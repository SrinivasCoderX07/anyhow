from setuptools import setup, find_packages

setup(
    name="recommender_system",
    version="1.0.0",
    description="A Recommender System for Amazon Electronics Products",
    long_description_content_type="text/markdown",
    author="Boya sai srinniivas",
    author_email="saisrinivas0711@gmail.com",
    url="https://github.com/SrinivasCoderX07/product-recomandation-system.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "pandas",
        "scikit-learn",
        "pytest",
        "flask",
        "gunicorn"
    ],
    entry_points={
        "console_scripts": [
            "recommender-app=app:app.run"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
