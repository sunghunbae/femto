from setuptools import setup
if __name__ == '__main__':
    setup(
        install_requires=[
            'openmm>=8',
            'numpy<=1.25',
            'ParmEd',
            'omegaconf',
            'pydantic',
            'tensorboardX',
            'GPUtil',
            'pyarrow',
            'tqdm',
            ],
        package_data={
            },
        scripts=[]
    )
