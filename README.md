# NOTEPILE

Notepile is a set of personal notes on various software and web
development technologies.

The site is intended to provide me with a quick reference from any location without the need to log into Github or any other account.

#1 = 1 1 (1)

#2 = 1 1 (1)

---

Feb 15, 2023 - Set project aside to finish other things.

## To Do

-   enter the Notes from the downloaded Mongo database file.
-   create a means of uploading the file with the application
-   ...or just copy paste the file locally...
-   convert JSON to Python > Add Python dictionary items to the Sqlite database
-   setup Postgres database for production
-   launch app on Fly.io
-   decide whether to include:
    -   User accounts and authentication
-   add `target="_blank"` attribute to `<a>` tags.
-   review and streamline `base.css` style page. Remove unecessary rules.
-   add functionality for a single note to have multiple topics
    -   add a new field ?

## To Study with Django

-   creating User accounts and auth
-   manipulating forms
-   signals

## New Notes

-   making API call with requests
-   Python try except blocks
-   change port for Django app (just add port after runserver)
    -   or make a script ...

```bash
#!/bin/bash

# create a bash script with the following:
exec ./manage.py runserver 0.0.0.0:5000

# save it as runserver in the same dir as manage.py
chmod +x runserver

# and run it as...
./runserver
```

## NOTES TO ADD:

-   list of most common status codes with link to wiki page
-   python regex
-   python \*args and \*\*kwargs
-   python unpacking
-   python comprehensions (including complex ones)
-   python filter, map and lambdas
-   python request library
    -   list of response object methods
-   python file handling / json in python
-   python handling env variables in django
-   bash scripting
-   Nginx
-   Linux networking
