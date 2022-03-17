# Implementation

This project uses Python3 (in particular Flask), and Docker for containerization. Specific Python3 package requirements can be found <a href="https://github.com/akhilsadam/positional-iss/blob/master/requirements.txt">here</a>. R and the npm package `@appnest/readme` by Andreas Mehlsen are used for documentation, but are not part of the API and will not be documented.

The source is available <a href="https://github.com/akhilsadam/positional-iss/">here</a>, and a list of important files can be found below.
## Files

 - `app/`:&nbsp;&nbsp;&nbsp;The application folder.
 - `doc/`:&nbsp;&nbsp;&nbsp;A documentation folder.
 - `Dockerfile`:&nbsp;&nbsp;A dockerfile for containerization.
 - `Makefile`:&nbsp;&nbsp;A makefile for ease of compilation.
 - `requirements.txt`:&nbsp;The list of Python3 requirements.
 - `wsgi.py`:&nbsp;&nbsp;&nbsp;The main Python file.

### The App/ Directory

- `api/`:&nbsp;&nbsp;&nbsp;Contains API route definitions in Python.
- `static/`:&nbsp;&nbsp;&nbsp;Contains static files for browser use.
- `templates/`:&nbsp;&nbsp;Contains Jinja2 templates for browser use.
- `test`:&nbsp;&nbsp;&nbsp;Contains testfiles in Python.
- `assets.py`:&nbsp;&nbsp;Collects static files for browser use.
- `routes.py`:&nbsp;&nbsp;Collects the API route definitions.
- `log.py`:&nbsp;&nbsp;&nbsp;Defines Python logger.
- `options.py`:&nbsp;&nbsp;Defines global options, like the application url.



