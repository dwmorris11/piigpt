from setuptools import setup, find_packages

setup(
    name='piigpt',
    version='0.12',
    description='Provides a mechanism to anonymize PII and PHI before sending to a LLM API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Dustin Morris',
    author_email='dustinnuc@gmail.com',
    url='https://github.com/dwmorris11/piigpt',
    packages=find_packages(),
    install_requires=[
        "azure-ai-textanalytics==5.3.0",
        "azure-common==1.1.28",
        "azure-core==1.30.0",
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "exrex==0.11.0",
        "idna==3.6",
        "isodate==0.6.1",
        "python-dotenv==1.0.1",
        "requests==2.31.0",
        "six==1.16.0",
        "toml==0.10.2",
        "typing_extensions==4.9.0",
        "urllib3==2.2.1",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
)