import glob
import shutil
import json
import os
from os import path
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

def add_front_matter(filename, widget):
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


from AnyQt.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QRectF, QSize, QSizeF, QPointF
from PyQt5.QtGui import QColor, QPainter, QImage, QIcon

from orangecanvas.registry import (
    WidgetDescription,
    CategoryDescription,
)

from orangecanvas.canvas.items import NodeItem

def save_widget_icon(
    background,
    icon: str,
    outname: str,
    export_size=QSize(100, 100),
    format="png",
):
    # create fake windget and category descriptions
    widget_description = WidgetDescription("", "", icon=None, qualified_name="orangecanvas")
    category = CategoryDescription(background=background)
    item = NodeItem(widget_description)
    qicon = QIcon()
    qicon.addFile(icon)
    item.setIcon(qicon)
    item.setWidgetCategory(category)
    iconItem = item.icon_item
    shapeItem = item.shapeItem

    shapeSize = export_size
    iconSize = QSize(export_size.width() * 3 / 4, export_size.height() * 3 / 4)

    rect = QRectF(
        QPointF(-shapeSize.width() / 2, -shapeSize.height() / 2), QSizeF(shapeSize)
    )
    shapeItem.setShapeRect(rect)
    iconItem.setIconSize(iconSize)
    iconItem.setPos(-iconSize.width() / 2, -iconSize.height() / 2)

    image = QImage(export_size, QImage.Format_ARGB32)
    image.fill(QColor("#00FFFFFF"))
    painter = QPainter(image)

    painter.setRenderHint(QPainter.Antialiasing, 1)

    scene = QGraphicsScene()
    scene.addItem(shapeItem)

    scene.render(painter, QRectF(image.rect()), scene.sceneRect())
    painter.end()

    if not image.save(outname, format, 100):
        print("Failed to save " + outname)


add_doc_path = sys.argv[1]

to_location = "content/widget-catalog/"

from AnyQt.QtWidgets import QApplication
app = QApplication([])

with open(path.join(add_doc_path, "widgets.json"), 'rt') as f:
    widgets_json = json.loads(f.read())

    from collections import defaultdict
    webpage_json = defaultdict(list)

    for cat, widgets in widgets_json:
        for w in widgets:
            print(w)
            wd = {}
            wd["order"] = len(webpage_json[cat])
            wd["title"] = w["text"]
            wd["category"] = cat
            wd["keywords"] = w["keywords"]

            wd["background"] = w["background"]
            icon_svg = path.join(add_doc_path, w["icon"])
            icon_png = "widget-icons/%s-%s.png" % (cat, w["text"])
            save_widget_icon(w["background"], icon_svg, "static/" + icon_png)
            wd["icon"] = icon_png

            wd["file"] = "visual-programming/source/widgets/data/color.md"  # FIXME
            wd["url"] = "color"  # FIXME

            webpage_json[cat].append(wd)

    s = json.dumps(webpage_json, indent=1)

    with open('data/widgets.json', 'w') as outfile:
        json.dump(webpage_json, outfile, indent=1)

    with open('static/widgets.json', 'w') as outfile:
        json.dump(webpage_json, outfile, indent=1)

    sys.exit(0)

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