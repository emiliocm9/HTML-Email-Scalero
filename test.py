import json
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
content = 'This is about page'
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
with open('stack.json') as json_file:
    data = json.load(json_file)
    ids = data["contact"]["recommended_ids"]
template = env.get_template('./about.html')
output = template.render(data=data, ids=ids)
print(output)
