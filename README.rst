=============
SimpleChinese
=============


.. image:: https://img.shields.io/pypi/v/simplechinese.svg
        :target: https://pypi.python.org/pypi/simplechinese

.. image:: https://img.shields.io/travis/chenmingxiang110/simplechinese.svg
        :target: https://travis-ci.com/chenmingxiang110/simplechinese

.. image:: https://readthedocs.org/projects/simplechinese/badge/?version=latest
        :target: https://simplechinese.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/chenmingxiang110/simplechinese/shield.svg
     :target: https://pyup.io/repos/github/chenmingxiang110/simplechinese/
     :alt: Updates



Chinese text processing, representation, and visualization.


* Free software: MIT license
* Documentation: https://simplechinese.readthedocs.io.


Features
--------

0. Read the data from a csv file.

.. code-block:: python

        df = pd.read_csv("test.csv")

.. image:: https://github.com/chenmingxiang110/SimpleChinese/raw/master/pics/raw.png
        :height: 400

1. Clean the data.

.. code-block:: python

        sc.clean(df)

.. image:: https://github.com/chenmingxiang110/SimpleChinese/raw/master/pics/clean.png
        :height: 400

The clean function does the following:

fillna(): Fill the N/As in a pandas.DataFrame with an empty string.

toLower(): Transform alphabets to their lowercases.

remove_punctuations(): Remove all the punctuations in a string or a pandas.DataFrame.

remove_space(): Remove all the spaces in a string or a pandas.DataFrame.

2. Extract words from the data

.. code-block:: python

        sc.extract_words(sc.clean(df))

.. image:: https://github.com/chenmingxiang110/SimpleChinese/raw/master/pics/extract_words.png
        :height: 400

3. Vectorization

.. code-block:: python

        sc.pca(sc.tfidf(sc.clean(df).iloc[:,0]))

.. image:: https://github.com/chenmingxiang110/SimpleChinese/raw/master/pics/vectorization.png
        :height: 400

4. Word cloud

.. code-block:: python

        sc.wordcloud(sc.clean(df).iloc[:,0], font_path="yahei.ttc")

.. image:: https://github.com/chenmingxiang110/SimpleChinese/raw/master/pics/wordcloud.png
        :height: 400

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
