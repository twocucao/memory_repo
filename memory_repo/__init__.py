"""Query API similar to Django for Python objects or dictionaries"""

__version__ = "0.1"
__author__ = "Said Ali <said.ali@msn.com>"
try:
    from memory_repo.query import QuerySet
except:
    from query import QuerySet
