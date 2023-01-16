import shutil
import json
import os
from os import path
import re
import sys

from collections import defaultdict
from urllib.parse import urlparse


def is_absolute(url):
    return bool(urlparse(url).netloc)


def front_matter(widget):
    return """+++
"title" = "%s"
"category" = "%s"
+++
""" % (widget["title"], widget["category"])


def copy_images(name, content, source, dest):
    regex_images = "!\[.*\]\((.*?)\)"
    matches = re.findall(regex_images, content)
    for match in matches:
        if not is_absolute(match):
            source_file = path.join(source, match)
            dest_dir = path.dirname(path.join(dest, match))

            if not path.exists(dest_dir):
                os.makedirs(dest_dir)

            try:
                shutil.copy2(source_file, dest_dir)
            except FileNotFoundError:
                print("ERROR (%s): image" % name, source_file, "does not exist")


def change_references(md_file, content, category, dest):
    regex_ref = "\[.*\]\((.*?)\)"
    matches_ref = re.findall(regex_ref, content)
    for ref in matches_ref:
        if not is_absolute(ref):
            if "loading-your-data" in ref:
                content = content.replace(ref, "https://docs.biolab.si/3/visual-programming/loading-your-data/index.html")
            elif ref.endswith(".md") and not ref.startswith("/"):
                new = "../" + ref[:-3] + "/"
                content = content.replace(ref, new)
            elif not ref.startswith("/"):
                new = "../" + ref
                content = content.replace(ref, new)
            else:
                print("WARNING (%s): not handled" % md_file, ref)

    return content


from AnyQt.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QRectF, QSize, QSizeF, QPointF
from PyQt5.QtGui import QColor, QPainter, QImage

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
    widget_description = WidgetDescription("", "", icon=icon, qualified_name="orangecanvas")
    category = CategoryDescription(background=background)
    item = NodeItem(widget_description)
    item.setWidgetCategory(category)
    iconItem = item.icon_item
    shapeItem = item.shapeItem

    shapeSize = export_size
    iconSize = QSize(int(export_size.width() * 3 / 4), int(export_size.height() * 3 / 4))

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

    if not image.save(outname, format, 80):
        print("Failed to save " + outname)


def process_widget(cat, w, webpage_json):

    for c, cat_list in webpage_json:
        if cat == c:
            break
    else:
        cat_list = []
        webpage_json.append((cat, cat_list))

    wd = {}
    wd["title"] = w["text"]
    wd["category"] = cat
    wd["keywords"] = w["keywords"]

    wd["background"] = w["background"]
    icon_svg = path.join(add_doc_path, w["icon"])
    icon_png = "widget-icons/%s-%s.png" % (cat, w["text"])
    icon_file = path.join("static", icon_png)
    if not path.exists(path.dirname(icon_file)):
        os.makedirs(path.dirname(icon_file))
    save_widget_icon(w["background"], icon_svg, icon_file)
    wd["icon"] = icon_png

    if w["doc"]:
        md_file = path.join(add_doc_path, w["doc"])
        md = open(md_file, "rt").read()

        category = cat.lower()
        category = category.replace(" ", "-")

        copy_images(md_file,
                    md,
                    path.dirname(md_file),
                    path.join(to_location_static, category))

        md = change_references(md_file,
                               md,
                               category,
                               path.join(to_location_static, category))

        loc = path.join(to_location, category)
        if not os.path.exists(loc):
            os.makedirs(loc)

        url = path.basename(md_file)[:-3]

        with open(path.join(loc, url + ".md"), 'wt') as of:
            of.write(front_matter(wd) + md)
            of.close()

        wd["url"] = url

    cat_list.append(wd)


print("Copy script: started.")

to_location = "content/widget-catalog/"
to_location_static = "static/widget-catalog/"

from AnyQt.QtWidgets import QApplication
app = QApplication([])

webpage_json = []

for add_doc_path in sys.argv[1:]:
    with open(path.join(add_doc_path, "widgets.json"), 'rt') as f:
        widgets_json = json.loads(f.read())
        for cat, widgets in widgets_json:
            for w in widgets:
                process_widget(cat, w, webpage_json)

s = json.dumps(webpage_json, indent=1)

with open('data/widgets.json', 'w') as outfile:
    json.dump(webpage_json, outfile, indent=1)

with open('static/widgets.json', 'w') as outfile:
    json.dump(webpage_json, outfile, indent=1)

print("Copy script: finished")
