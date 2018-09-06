# nbconvert_utils

Provides two nbconvert preprocessors: `ExecuteWithPreamble`, and `ExecuteWithIPythonArgs`.

`ExecuteWithPreamble` injects additional python scripts to be run _before_ any other code in the notebook to be exported, and then removes the corresponding cells.

`ExecuteWithIPythonArgs` enables passing arguments to the kernel used to run the notebook using the `--Executor.extra_arguments` parameter.

## Usage

`jupyter nbconvert --to markdown --Exporter.preprocessors=[\"nb_utils.ExecuteWithPreamble\"] --ExecuteWithPreamble.preamble_scripts=[\"../../some_script.py\"] *.ipynb`

`jupyter nbconvert --to markdown --Exporter.preprocessors=[\"nb_utils.ExecuteWithPreamble\"] --ExecuteWithIPython.extra_arguments=[\"--profile-dir=/custom/ipython/profile/default\"] *.ipynb`