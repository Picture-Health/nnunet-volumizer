from setuptools import setup, find_packages

setup(
    name='nnunetv2',
    version='2.5.1',
    description='nnU-Net v2 - Patched for proper packaging',
    author='Rushil Nagabhushan',
    url='https://github.com/Picture-Health/nnunet-volumizer',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        "torch>=2.1.2",
        "acvl-utils>=0.2.3,<0.3",
        "tqdm",
        "dicom2nifti",
        "scipy",
        "batchgenerators>=0.25.1",
        "numpy>=1.24",
        "scikit-learn",
        "scikit-image>=0.19.3",
        "SimpleITK>=2.2.1",
        "pandas",
        "graphviz",
        "tifffile",
        "requests",
        "nibabel",
        "matplotlib",
        "seaborn",
        "imagecodecs",
        "yacs",
        "batchgeneratorsv2 @ git+https://github.com/MIC-DKFZ/batchgeneratorsv2.git",
        "einops",
        "blosc2>=3.0.0b1",
        "dynamic-network-architectures @ git+https://github.com/MIC-DKFZ/dynamic-network-architectures.git"
    ]
)
