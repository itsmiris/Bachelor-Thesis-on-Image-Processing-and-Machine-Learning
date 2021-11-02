import yaml


def load_config(config_path="config.yaml", encoding="utf-8"):
    with open(config_path, "r", encoding=encoding) as config_file:
        return yaml.load(config_file, yaml.Loader)


config = load_config()