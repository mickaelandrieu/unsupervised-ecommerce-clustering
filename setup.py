from setuptools import setup, find_packages

setup(
    name='ecommerce-segmentation',
    version='0.1.0',
    description='Olist Ecommerce segmentation model',
    author='Mickaël Andrieu',
    author_email='mickael.andrieu@solvolabs.com',
    url='https://github.com/mickaelandrieu/unsupervised-ecommerce-scoring/setup-py',
    packages=find_packages(),
     install_requires=[
        'matplotlib==3.4.3',
        'pandas==1.3.4',
        'plotly==5.6.0',
        'scikit-learn==1.0',
        'scipy==1.7.1',
        'streamlit==1.1.0',
        'joblib==1.1.0',
    ],
    setup_requires=['black'], 
)