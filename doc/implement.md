# Implementation

This project uses Python3 (in particular Flask), and Docker for containerization. Specific Python3 package requirements can be found <a href="https://github.com/akhilsadam/positional-iss/blob/master/requirements.txt">here</a>. R and the npm package `@appnest/readme` by Andreas Mehlsen are used for documentation, but are not part of the API and will not be documented.

The source is available <a href="https://github.com/akhilsadam/positional-iss/">here</a>, and a list of important files can be found below.
## Files

 - `app/`:&emsp;&emsp;&emsp;The application folder.
 - `doc/`:&emsp;&emsp;&emsp;A documentation folder.
 - `Dockerfile`:&emsp;&emsp;A dockerfile for containerization.
 - `Makefile`:&emsp;&emsp;A makefile for ease of compilation.
 - `requirements.txt`:&emsp;The list of Python3 requirements.
 - `wsgi.py`:&emsp;&emsp;&emsp;The main Python file.

### The App/ Directory

- `api/`:&emsp;&emsp;&emsp;Contains API route definitions in Python.
- `static/`:&emsp;&emsp;&emsp;Contains static files for browser use.
- `templates/`:&emsp;&emsp;Contains Jinja2 templates for browser use.
- `test`:&emsp;&emsp;&emsp;Contains testfiles in Python.
- `assets.py`:&emsp;&emsp;Collects static files for browser use.
- `routes.py`:&emsp;&emsp;Collects the API route definitions.
- `log.py`:&emsp;&emsp;&emsp;Defines Python logger.
- `options.py`:&emsp;&emsp;Defines global options, like the application url.



