from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO


def yaml_loads(content):
    yaml = YAML()
    return yaml.load(content)


def yaml_dumps(data):
    """
    avoid-omap-ruamel
    - https://gist.github.com/monester/3f3bd87a936d1017c1f5089650b79a98
    """
    yaml = YAML()
    stream = StringIO()
    yaml.dump(data, stream=stream)
    return stream.getvalue()