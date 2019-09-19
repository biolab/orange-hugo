import json
import os
from os import path
from pathlib import Path

from AnyQt.QtWidgets import QGraphicsScene, QApplication
from AnyQt.QtCore import Qt, QTimer
# QWebEngineWidgets must be imported before QCoreApplication is created.
# It will fail with an import error if imported (first time) after.
import AnyQt.QtWebEngineWidgets  # pylint: disable=unused-import

from orangecanvas.resources import icon_loader
from orangecanvas.help import HelpManager
from orangecanvas.registry import WidgetRegistry

from Orange.canvas.config import Config as OConfig


class WidgetCatalog:
    def __init__(self, output_dir, image_url_prefix, categories):
        self.output_dir = output_dir
        self.image_url_prefix = image_url_prefix
        self.categories = categories

        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
        QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
        self.app = QApplication([])

        print("Generating widget repository")
        self.registry = self.__get_widget_registry()
        print("Locating help files")
        self.help_manager = HelpManager()
        self.help_manager.set_registry(self.registry)

        # Help manager needs QApplication running to get the urls
        # of widget documentation. 5 seconds should be enough.
        QTimer.singleShot(5000, self.app.quit)
        self.app.exec()

        self.__scene = QGraphicsScene()
        self.__nodes = []
        print("Ready to go")

    def create(self):
        print("Generating catalog")

        result = []
        for category in self.registry.categories():
            if self.categories is not None and category.name not in self.categories:
                continue
            widgets = []
            result.append((category.name, widgets))
            for widget in category.widgets:
                iconfn = icon_loader.from_description(widget).find(widget.icon)
                icon = Path(iconfn).relative_to(os.getcwd()).as_posix()
                widgets.append({
                    "text": widget.name,
                    "doc": self.__get_help(widget),
                    "icon": icon,
                    "background": category.background,
                    "keywords": widget.keywords,
                })

        with open(path.join(self.output_dir, "widgets.json"), 'wt') as f:
            json.dump(result, f, indent=1)
        print("Done")

    @staticmethod
    def __get_widget_registry():
        widget_registry = WidgetRegistry()
        widget_discovery = OConfig.widget_discovery(widget_registry)
        widget_discovery.run(OConfig.widgets_entry_points())

        # Fixup category.widgets list
        for cat, widgets in widget_registry._categories_dict.values():
            cat.widgets = widgets
        return widget_registry

    def __get_help(self, widget):
        query = dict(id=widget.qualified_name)
        try:
            return self.help_manager.search(query).url()
        except KeyError:
            return None


if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser(usage="usage: %prog --output <outputdir> [options]")
    parser.add_option('--url-prefix', dest="prefix",
                      help="prefix to prepend to image urls")
    parser.add_option('--output', dest="output",
                      help="path where widgets.json will be created")
    parser.add_option('--categories', dest="categories",
                      help="An optional comma-separated list of categories")

    options, args = parser.parse_args()
    if not options.output:
        options.output = "."

    categories = None
    if options.categories:
        categories = options.categories.split(",")

    w = WidgetCatalog(output_dir=options.output, image_url_prefix=options.prefix,
                      categories=categories)
    w.create()
