import json
import os
from os import path

import docutils.nodes
import docutils.parsers.rst
import docutils.utils

from AnyQt.QtWidgets import QApplication
from AnyQt.QtCore import Qt
# QWebEngineWidgets must be imported before QCoreApplication is created.
# It will fail with an import error if imported (first time) after.
import AnyQt.QtWebEngineWidgets  # pylint: disable=unused-import

from orangecanvas.resources import icon_loader
from orangecanvas.registry import WidgetRegistry

from Orange.canvas.config import Config as OConfig


class WidgetCatalog:
    def __init__(self, output_dir, categories, doc_dir):
        self.output_dir = output_dir
        self.categories = categories
        self.doc_dir = doc_dir

        self.app = QApplication([])

        print("Generating widget repository")
        self.registry = self.__get_widget_registry()
        print("Locating help files")
        self.help = get_documentation(doc_dir)

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
                icon = path.relpath(iconfn, os.getcwd())
                doc = self.__get_help(widget)
                if doc:
                    doc = path.relpath(doc, os.getcwd())

                widgets.append({
                    "text": widget.name,
                    "doc": doc,
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
        if widget.name in self.help:
            return path.join(self.doc_dir, self.help[widget.name])
        else:
            print("No documentation for", widget.name)
            return None


def parse_rst(text: str) -> docutils.nodes.document:
    parser = docutils.parsers.rst.Parser()
    components = (docutils.parsers.rst.Parser,)
    settings = docutils.frontend.OptionParser(components=components).get_default_values()
    document = docutils.utils.new_document('<rst-doc>', settings=settings)
    parser.parse(text, document)
    return document


def get_title(fn):
    """ Get title (widget name) from Orange's documentation md files """
    for l in open(fn, "rt"):
        l = l.strip()
        if l:
            return l


class LinkCheckerVisitor(docutils.nodes.GenericNodeVisitor):

    def __init__(self, parsed, base_path):
        super().__init__(parsed)
        self.base_path = base_path
        self.results = {}

    def visit_section(self, node):
        if node["ids"] == ["widgets"]:
            lines = str(node).split("\n")
            for l in lines:
                l = l.strip()
                fn = path.join(self.base_path, l + ".md")
                if path.isfile(fn):
                    title = get_title(fn)
                    if title in self.results:
                        raise Exception("widget name is repeated")
                    else:
                        self.results[title] = l + ".md"

    def default_visit(self, node):
        pass


def get_documentation(dpath):
    indexfn = path.join(dpath, "index.rst")
    p = parse_rst(open(indexfn, "rt").read())
    visitor = LinkCheckerVisitor(p, dpath)
    p.walk(visitor)
    return visitor.results


if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser(usage="usage: %prog [options]")
    parser.add_option('--output', dest="output",
                      help="path where widgets.json will be created")
    parser.add_option('--categories', dest="categories",
                      help="An optional comma-separated list of categories")
    parser.add_option('--doc', dest="doc",
                      help="Path to widget documentation")

    options, args = parser.parse_args()
    if not options.output:
        options.output = "."

    if options.categories:
        options.categories = options.categories.split(",")

    w = WidgetCatalog(output_dir=options.output,
                      categories=options.categories,
                      doc_dir=options.doc)
    w.create()

    # usage example
    # ~/orange3/doc$ python ~/orange-hugo/scripts/create_widget_catalog.py --categories Data,Visualize,Model,Evaluate,Unsupervised, --doc visual-programming/source/
