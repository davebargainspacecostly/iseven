from jinja2 import Template

animals = ["dog", "cat", "frog", "hamster"]

all_animals_page_template = """# All animals

This is where you will find a list of all our animals

{% for animal in animals %}
[Deploy a {{ animal }}](https://giphy.com/{{ animal }})

{% endfor %}
"""

animal_page_template = """# {{ animal }}

This is where you will find out about a {{ animal }}

[{{ animal }}](https://giphy.com/{{ animal }})

[Search for {{ animal }}](https://google.com/search?q={{ animal }})

[Deploy a {{ animal }}](https://giphy.com/{{ animal }})
"""

mkdocs_template = """site_name: 'Example with Animals'
site_description: An informative description
plugins:
  - techdocs-core
nav:
  - Overview: \'index.md\'
  - What is a fish: \'fish.md\'
  - All the Animals: \'animals/all.md\'
  - Each Animal:
{%- for animal in animals %}
    - {{ animal }}: \'animals/{{ animal }}.md\'
{%- endfor %}
"""

j2_template = Template(animal_page_template)
for animal in animals:
  print(f'saving to filename docs/animals/{animal}.md')
  with open('docs/animals/'+animal+'.md', "w") as text_file:
    text_file.write(j2_template.render(animal=animal))

j2_template = Template(all_animals_page_template)
print('saving to filename docs/animals/all.md')
with open('docs/animals/all.md', "w") as text_file:
  text_file.write(j2_template.render(animals=animals))

j2_template = Template(mkdocs_template)
print('saving to filename mkdocs.yml')
with open('mkdocs.yml', "w") as text_file:
  text_file.write(j2_template.render(animals=animals))
  #print(j2_template.render(animals=animals))
