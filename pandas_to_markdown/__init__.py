import pandas as pd
import tabulate as tabulate

import nbconvert


def to_md(self):
    print("Markdowning.")
    return tabulate.tabulate(self.head(), self.columns, tablefmt="pipe")


class PandasToMarkdown(nbconvert.preprocessors.Preprocessor):
    def preprocess(self, nb, resources):
        nb.display_formatter.formatters["text/html"].for_type(pd.DataFrame, to_md)
        return nb, resources
