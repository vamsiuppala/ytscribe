from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Transcribe YouTube videos'
LONG_DESCRIPTION = 'Package to transcribe YouTube videos by downloading them in a wav format and using OpenAI Whisper model'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="ytscribe", 
        version=VERSION,
        author="Vamsi Uppala",
        author_email="uvvamsikrishna@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)