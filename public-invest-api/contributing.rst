Contributing
============
Contributions are more than welcome! For some tips on how to contribute, please see below:

1. Fork the repository
2. Create a new branch (e.g. `git checkout -b my-new-feature`)
3. Make your changes
4. Commit your changes (e.g. `git commit -am "Add new feature"`)
5. Push to the branch (e.g. `git push origin my-new-feature`)
6. Create a new Pull Request

Note: `docstrings` are written using Google"s style guide. Please follow this style when adding new functions or classes.

Updating the Documentation
------------------------
Documentation is stored in a different repository. To update the documentation, follow the steps above, except base your changes off of: https://github.com/NelsonDane/docs
Then, create a pull request to the `main` branch of the `docs` repository. The documentation is built using Sphinx and hosted on GitHub pages.
If you want to test the documentation locally, you can do so by running the following command in the after cloning the `docs` repository:

.. code-block:: bash

    make html

This will build the documentation and store it in the `_build/html` directory. You can then open the `index.html` file in your browser to view the documentation.
You can also use the `make clean` command to remove the build files and start fresh.
