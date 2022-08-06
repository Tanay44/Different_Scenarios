import yaml

yaml_file = open("learn_yaml.yaml", 'r')
yaml_content = yaml.load(yaml_file, Loader=yaml.FullLoader)

# print("Key: Value")
# for key, value in yaml_content.items():
#     print(f"{key}: {value}")
c = yaml_content['list']
d = 3

if d == 2: 
    print(c[1])
else:
    print(c[2]) 
