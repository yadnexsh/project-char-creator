import os
import sys

package_path = os.path.dirname(__file__)
print(f"Package path > {package_path}")

if package_path not in sys.path:
    sys.path.append(package_path)
    
    
from character_package import warrior
