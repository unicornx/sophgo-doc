# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SG200X'
copyright = '2023 SOPHGO Co., Ltd'
author = 'Sophgo'
release = '0.0.1'

title = 'Technical Reference Manual'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

latex_maketitle = r'''
\begin{titlepage}
\begin{center}
    \includegraphics[width=0.8\textwidth]{logo.png}
    \vspace*{2cm}

    \Huge \textbf{'''+ project + r'''} \par
    \vspace*{1cm}
    \Huge \textbf{'''+ title + r'''} \par
    \vspace*{6cm}
\end{center}
\noindent \Large Version : ''' + release + r'''\par
\vspace*{2cm}
\noindent \normalsize Copyright © ''' + copyright + r'''. All rights reserved.\\
\noindent \normalsize No part of this document may be reproduced or transmiited in any form or by any means\\
\noindent \normalsize without prior written consent of ''' + copyright + r'''\\
\end{titlepage}
'''

latex_elements = {
	'maketitle': latex_maketitle,

	'preamble':r'''
		\usepackage{tocloft}
		\renewcommand\cftfignumwidth{4em}
		\renewcommand\cfttabnumwidth{4em}
		\renewcommand\cftsecnumwidth{4em}
		\renewcommand\cftsubsecnumwidth{6em}
		\renewcommand\cftparanumwidth{6em}
		\usepackage{fancyhdr}
		\setlength\headheight{14pt}
		\fancypagestyle{normal}{
			\fancyhead[R]{}
			\fancyhead[C]{\leftmark}
			\fancyfoot[C]{''' + copyright + r'''}
			\fancyfoot[R]{\thepage}
			\renewcommand{\headrulewidth}{0.4pt}
			\renewcommand{\footrulewidth}{0pt}
		}''',
}