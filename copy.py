import glob
import shutil
import json
import os
import re


"""
Generates string of values which is later added to .md files.

Parameters
----------
filename:
    The location of the widget .md file.
widget: 
    JSON object of widget data.

"""


def add_front_matter(filename,widget):
    front_matter = "+++\n"

    with open(filename, 'r+') as f:
        content = f.read()
        for element in widget:
            if 'url' in element:
                continue
            elif 'file' not in element:
                if element == 'icon':
                    front_matter += '"' + element + '" = "icons/' + str(widget[element].split('/')[-1]) + '"\n'
                else:
                    front_matter += '"'+element+'" = "' + str(widget[element]) + '"\n'
        front_matter += "+++\n"
        front_matter += content.replace("images/", "/images/")
    return front_matter


"""
Copy images for widget catalog from external module.

Parameters
----------
filename:
    Name of the .md file
path:
location of the .md file

"""
def copy_images(path,filename):
    with open(path+filename, 'r+') as f:
        content = f.read()

        regex = "!\[\]\((.*?)\)"
        loc = filename.split("/")
        # visual-programming/source/widgets/data/color.md
        location = ""
        for element in loc[:-1]:
            location+=element+"/"
            # print(element)

        
        locationFrom = path+location
        print(locationFrom," ---- ",filename)
        locationTo = "static/images/"
        matches = re.findall(regex,content)
        for match in matches:
            print(match)
            try:
                shutil.copy2(locationFrom+match, locationTo+match)
            except IOError as e:
                folders = '/'.join(match.split("/")[:-1])
                os.makedirs(locationTo+folders)
                shutil.copy2(locationFrom+match, locationTo+match)


"""
Build json file for widget catalog from widget_data.json.

Parameters
----------
filename:
    The location of the file widget_data.json

"""


def build_json(filename):
    json_content = {}
    widgets = {}
    with open(filename, 'r+') as f:
        # print(f.read())
        widgets = json.loads(f.read())
        for widget in widgets:
            widget_obj = widgets[widget]
            if widget_obj["category"] not in json_content:
                json_content[widget_obj["category"]] = []
            json_content[widget_obj["category"]].append(widget_obj)
            widget_obj['url'] = url = widget_obj['title'].lower().replace(" ", "_")


    with open('data/widgets.json', 'w') as outfile:
        json.dump(json_content, outfile)
        outfile.close()

    with open('static/widgets.json', 'w') as outfile:
        json.dump(json_content, outfile)
        outfile.close()

    return widgets


# find widgets_data.json file in submodule
files = glob.glob('external/**/widget_data.json', recursive=True)
print(files)
# if no file found, exit
if len(files) < 1:
    print("Can't find widget_data.json file.")
    exit()
json_content = {}

path = files[0].split("widget_data")[0]
file = files[0]
location = "content/widget-catalog/"

widgets_data = build_json(file)

# open widget_data.json file
with open(file, 'r+') as f:
    widgets = json.loads(f.read())
    # for each widget in widget_data.json file generate FrontMatter and copy .md file and icon image
    for widget in widgets:
        widget_data = widgets[widget]
        text = add_front_matter(path+widget_data['file'], widgets_data[widget_data['title']])
        copy_images(path,widget_data['file'])
        with open(location+widget_data['file'].split("/")[-1], 'w') as tmp:
            tmp.write(text)
            tmp.close()
        image_path = "static/"+'/'.join(widget_data['icon'].split('/')[:-1])+"/"
        print(image_path)
        try:
            shutil.copy2(path + widget_data['icon'], image_path)
        except IOError as e:
            os.makedirs(image_path)
            shutil.copy2(path + widget_data['icon'], image_path)
