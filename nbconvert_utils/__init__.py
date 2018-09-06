from textwrap import dedent

import nbformat
from nbconvert.preprocessors.execute import ExecutePreprocessor
from traitlets import List, Unicode


class ExecuteWithPreamble(ExecutePreprocessor):
    preamble_scripts = List(Unicode).tag(
        config=True,
        help=dedent(
            """
            A list of python scripts to run _before_ running any notebook, which will
            be run in the same kernel as the notebook. The path must be relative to
            the location of the _notebook_.
            Should be provided as [\\"path/to/script\\""].
            (Yes, the escapes do need to be put in.)
            """
        ),
    )

    def preprocess(self, nb, resources, km=None):
        """
        Preprocess notebook executing each code cell.
        The input argument `nb` is modified in-place.
        Parameters
        ----------
        nb : NotebookNode
            Notebook being executed.
        resources : dictionary
            Additional resources used in the conversion process. For example,
            passing ``{'metadata': {'path': run_path}}`` sets the
            execution path to ``run_path``.
        km: KernelManager (optional)
            Optional kernel manager. If none is provided, a kernel manager will
            be created.
        Returns
        -------
        nb : NotebookNode
            The executed notebook.
        resources : dictionary
            Additional resources used in the conversion process.
        """
        self.log.info(self.__dict__)
        self.log.info(nb.cells[0])
        for script in self.preamble_scripts:
            self.log.info(f"Injecting preamble script {script}")
            nb.cells.insert(
                0,
                nbformat.from_dict(
                    {
                        "cell_type": "code",
                        "execution_count": 0,
                        "metadata": {"collapsed": True},
                        "outputs": [],
                        "source": f"%run {script}",
                    }
                ),
            )
        nb, resources = super().preprocess(nb, resources)
        self.log.info(f"Removing first {len(self.preamble_scripts)} cells")
        nb.cells = nb.cells[len(self.preamble_scripts) :]
        return nb, resources


class ExecuteWithIPythonArgs(ExecutePreprocessor):
    extra_arguments = List(Unicode).tag(
        config=True,
        help=dedent(
            """
            A list of arguments to be passed to the IPython kernel, e.g. 
            [\\"--profile-dir=/custom/ipython/profile/default\\"]
            """
        ),
    )


from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
