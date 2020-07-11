# Changelog

All notable changes to this project will be documented in this file.

The format is based on [changelog.md](https://changelog.md/) and this project adheres to [semantic versioning](https://semver.org/).

Changes for the upcoming release can be found in the `changelog.d` directory in this repository.

Do **NOT** add changelog entries here! This changelog is managed by [towncrier](https://towncrier.readthedocs.io/en/actual-freaking-docs/index.html) and is compiled at release time.

.. towncrier release notes start

Cookbook 0.5.0 (2020-07-11)
===========================

Features
--------

- Added storing recipes to Postgres database instead of disk.

  Added database migrations.

  Added environment variables.

  Added configuration file.

  Added database creation to README. (#003)


Cookbook 0.4.0 (2020-06-27)
===========================

Features
--------

- Changed download_recipe to save.

  Changed list_recipes to browse.

  Added view command for opening downloaded recipes in firefox.

  Tests delete downloaded pages. (#002)


Cookbook 0.3.3 (2020-06-27)
===========================

Features
--------

- Add a [changelog.md](https://changelog.md/) and [towncrier](https://towncrier.readthedocs.io/en/actual-freaking-docs/index.html) so developers can log future changes to the project. (#001)
