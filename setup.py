from setuptools import setup
import os
print("DEBUG: ENVIRONMENT VARIABLES START")
for k, v in os.environ.items():
    print(f"{k}={v}")
print("DEBUG: ENVIRONMENT VARIABLES END")

from setuptools import setup
setup(name="pwned", version="0.0.1")
