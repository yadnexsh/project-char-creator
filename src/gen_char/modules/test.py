
import os

cur_file_path = os.path.abspath(__file__)
package_path = os.path.abspath(cur_file_path + "/../..")

print(cur_file_path, package_path)