import yaml
import sys
import os
from os.path import dirname


def yaml_data_loader(file_name):
    project_root_path = dirname(dirname(__file__))
    yaml_absolute_path = project_root_path + '\\test_data\\' + file_name

    with open(yaml_absolute_path, "r") as stream:
        try:
            return [yaml.safe_load(stream)]
        except yaml.YAMLError as exc:
            print(exc)

