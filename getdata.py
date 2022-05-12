import yaml, os, json


def get_image_name():
    image_dict = {}
    with open('test.yaml') as f:
        dc = yaml.safe_load(f)
        services = dc['services']
        for name, svc  in services.items():
            image_dict[svc['image'].split(':')[0]] = svc['build']
    return image_dict
op = get_image_name()
# print(op)
