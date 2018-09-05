import pandas as pd
import tabulate as tabulate

import nbconvert


def to_md(self):
    print("Markdowning.")
    return tabulate.tabulate(self.head(), self.columns, tablefmt="pipe")


class PandasToMarkdown(nbconvert.preprocessors.Preprocessor):
    def preprocess(self, nb, resources):
        print(resources)
        nb.display_formatter.formatters["text/html"].for_type(pd.DataFrame, to_md)
        return nb, resources

from nbconvert.preprocessors.execute import ExecutePreprocessor
from traitlets import List, Unicode

class Preambler(ExecutePreprocessor):
    extra_arguments = ["--profile-dir=/Users/jono/flowkit/docs/nbconvert_config/default"]
