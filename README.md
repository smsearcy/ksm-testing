Testing KSM Issue
=================

Minimal Pyramid app to replicate issue using Keeper Secrets Manager in Pyramid web application,
when using Gunicorn worker processes.

```
$ python3.8 -m venv venv
$ source venv/bin/activate
$ pip install -U pip
$ pip install -r requirements.txt
$ KSM_TOKEN="<token>" ./test.sh [-w ##]
```
