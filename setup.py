from setuptools import setup, find_packages
setup(
    name='k8sfoams',
    version='1.0.3',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mmpyro/k8s-pod-foamtree',

    description='K8s pod foamtree visualizer',
    author="Michal Marszalek",
    author_email="mmpyro@gmail.com",
    license='Apache 2.0',

    scripts=['k8sfoams'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'attrs==21.2.0',
        'bandit==1.7.0',
        'bitmath==1.3.3.1',
        'cachetools==4.2.2',
        'certifi==2021.5.30',
        'chardet==4.0.0',
        'click==8.0.1',
        'flake8==3.9.2',
        'flask==2.0.1',
        'gitdb==4.0.7',
        'gitpython==3.1.18',
        'google-auth==1.32.1',
        'gunicorn==20.1.0',
        'idna==2.10',
        'iniconfig==1.1.1',
        'itsdangerous==2.0.1',
        'jinja2==3.0.1',
        'kubernetes==17.17.0',
        'markupsafe==2.0.1',
        'mccabe==0.6.1',
        'mock==4.0.3',
        'mypy==0.910',
        'mypy-extensions==0.4.3',
        'oauthlib==3.1.1',
        'packaging==21.0',
        'pbr==5.6.0',
        'pluggy==0.13.1',
        'py==1.10.0',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'pycodestyle==2.7.0',
        'pydash==5.0.1',
        'pyflakes==2.3.1',
        'pyparsing==2.4.7',
        'pytest==6.2.4',
        'python-dateutil==2.8.1',
        'pyyaml==5.4.1',
        'requests==2.25.1',
        'requests-oauthlib==1.3.0',
        'rsa==4.7.2',
        'six==1.16.0',
        'smmap==4.0.0',
        'stevedore==3.3.0',
        'toml==0.10.2',
        'typing-extensions==3.10.0.0',
        'urllib3==1.26.6',
        'websocket-client==1.1.0',
        'werkzeug==2.0.1',
    ],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Topic :: Scientific/Engineering :: Visualization',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3.8',
  ],
  keywords = ['foamtree', 'k8s', 'visualization']
)
