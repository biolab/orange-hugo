import glob
import shutil
import json
import os
import re
import sys

"""
Generates string of values which is later added to .md files.

Parameters
----------
filename:
    The location of the widget .md file.
widget: 
    JSON object of widget data.

"""
print("Copy script: started.")

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
    category = filename.split("/")[-2]
    with open(path+filename, 'r+') as f:
        content = f.read()

        regex_images = "!\[\]\((.*?)\)"
        loc = filename.split("/")
        location = ""
        for element in loc[:-1]:
            location+=element+"/"

        
        locationFrom = path+location
        locationTo = "static/images/"
        regex_ref = "\[.*?\]\((..\/.*?)\)"
        matches_ref =  re.findall(regex_ref,content)
        matches = re.findall(regex_images,content)
        for match in matches:
            if ".." in match:
                tmp = match.split("/")
                # st = "/images/"+tmp[1]+"/"+tmp[-1]
                try:
                    shutil.copy2(locationFrom+match, locationTo+tmp[1]+"/"+match.split("/")[-1])
                except IOError as e:
                    folders = '/'.join(match.split("/")[:-1])
                    os.makedirs(locationTo+tmp[1])
                    shutil.copy2(locationFrom+match,locationTo+tmp[1]+"/"+match.split("/")[-1])
            else:

                try:
                    shutil.copy2(locationFrom+match, locationTo+category+"/"+match.split("/")[-1])
                except IOError as e:
                    folders = '/'.join(match.split("/")[:-1])
                    os.makedirs(locationTo+category)
                    shutil.copy2(locationFrom+match,locationTo+category+"/"+match.split("/")[-1])


"""
Change image and link references to new strucutre.

Parameters
----------
filename:
    Name of the .md file
content:
    content of the .md file

"""
def change_references(content, filename):
    regex_ref = "\[.*?\]\((..\/.*?)\)"
    matches_ref =  re.findall(regex_ref,content)
    for ref in matches_ref:
        if ".png" in ref or ".jpg" in ref:
            continue
        elif "loading-your-data" in ref:
            content = content.replace(ref, "https://docs.biolab.si//3/visual-programming/loading-your-data/index.html")
        else:
            tmp = ref.split("/")
            # if "-" in tmp[0]:
            st = "/".join(tmp[1:])
            if ".md" in st:
                st = "/widget-catalog/"+st[:-3].lower().replace(" ", "").replace("-","")
            else: 
                st = "/widget-catalog/"+st.lower().replace(" ", "").replace("-","")
            content = content.replace(ref, st)
        
    category = filename.split("/")[-2]
    regex_images = "!\[\]\((.*?)\)"
    matches = re.findall(regex_images,content)
    # print(matches)
    for ref in matches:
        if ".." in ref:
            tmp = ref.split("/")
            st = "/images/"+tmp[1]+"/"+tmp[-1]
            content = content.replace(ref, st)
        else:
            tmp = ref.split("/")
            st = "/".join(tmp[1:])
            st = "/images/"+category+"/"+tmp[-1]
            content = content.replace(ref, st)
    return content

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
        widgets = json.loads(f.read())
        for widget in widgets:
            widget_obj = widgets[widget]
            if widget_obj["category"] not in json_content:
                json_content[widget_obj["category"]] = []
            json_content[widget_obj["category"]].append(widget_obj)
            widget_obj['url'] = url = widget_obj['title'].lower().replace(" ", "").replace("-","")
            # widget_obj['order'] = 1

    with open('data/widgets.json', 'w') as outfile:
        json.dump(json_content, outfile)
        outfile.close()

    with open('static/widgets.json', 'w') as outfile:
        json.dump(json_content, outfile)
        outfile.close()

    return widgets

if len(sys.argv) <2:
    print("No args given")

# find widgets_data.json file in submodule
files = glob.glob('external/'+sys.argv[1]+'/**/widget_data.json', recursive=True)
# if no file found, exit
if len(files) < 1:
    print("Can't find widget_data.json file.")
    exit()
json_content = {}

path = files[0].split("widget_data")[0]+"widgets"
file = files[0]

location = "content/widget-catalog/"

widgets_data = build_json(file)

# open widget_data.json file
with open(file, 'r+') as f:
    widgets = json.loads(f.read())
    # for each widget in widget_data.json file generate FrontMatter and copy .md file and icon image
    for widget in widgets:
        widget_data = widgets[widget]
        s = widget_data['file'].split("widgets")[1]
        text = add_front_matter(path+s, widgets_data[widget_data['title']])
        copy_images(path,s)

        loc = location+s.split("/")[0]
        if not os.path.exists(loc):
            os.makedirs(loc)
        with open(location+s, 'w') as tmp:
            text = change_references(text, s)
            tmp.write(text)
            tmp.close()
        icons = widget_data['icon'].split("/")[-3:]
        b = "/"
        icons_path = b.join(icons)
        image_path = "static/"+'/'.join(widget_data['icon'].split('/')[:-1])+"/"
        try:
            shutil.copy2(path+"/" + icons_path, image_path)
        except IOError as e:
            os.makedirs(image_path, exist_ok=True)
            shutil.copy2(path+"/" +icons_path, image_path)

print("Copy script: finished. \nAll wdigets have been copied.")