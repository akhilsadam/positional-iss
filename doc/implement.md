# Implementation

This project uses Python3 (in particular Flask), and Docker for containerization. Specific Python3 package requirements can be found <a href="https://github.com/akhilsadam/positional-iss/blob/master/requirements.txt">here</a>. R and the npm package `@appnest/readme` by Andreas Mehlsen are used for documentation, but are not part of the API and will not be documented.

The source is available <a href="https://github.com/akhilsadam/positional-iss/">here</a>, and a list of important files can be found below.
## Files

 - `app/`:              The application folder.
 - `doc/`:              A documentation folder.
 - `Dockerfile`:        A dockerfile for containerization.
 - `Makefile`:          A makefile for ease of compilation.
 - `requirements.txt`   The list of Python3 requirements.
 - `wsgi.py`:           The main Python file.

### The App/ Directory

- `api/`:               Contains API route definitions in Python.
- `static/`:            Contains static files for browser use.
- `templates/`:         Contains Jinja2 templates for browser use.
- `test`:               Contains testfiles in Python.
- `assets.py`:          Collects static files for browser use.
- `routes.py`:          Collects the API route definitions.
- `log.py`:             Defines Python logger.
- `options.py`:         Defines global options, like the application url.



