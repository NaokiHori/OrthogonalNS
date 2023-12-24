import os
import sys

sys.path.append(os.path.abspath("./conf_params"))

project = "Orthogonal NS"
author = "Naoki Hori"
copyright = f"2023, {author}"

from alabaster_params import html_theme, html_theme_options
from mathjax_params import mathjax_path, mathjax3_config

html_static_path = ["_static"]
