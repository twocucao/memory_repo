# Memory Repo

```
Memory Repo is my own favor of https://github.com/said-ali/iterable_orm
```

If you have a small amount of data need to filter multiple times and database access is not cheap(e.g: prefetch too much
django models), you may need a
django way of filter to make you code much clearer

memory_repo allows you to filter, exclude and sort data using similar API provided by Django ORM. The data needs to be a
list of objects.

memory_repo gives you the following API

- filter - Returns a new list of objects or dictionaries that match the given lookup parameters
- exclude - Returns a new list of objects or dictionaries that do not match the given lookup parameters
- get - Returns a single object or dictionary if there's two matches returns an exception
- order_by - Returns a list ordered objects or dictionaries
- first - Returns the first object or dictionary of filtered or exlcude data
- last - Returns the first object or dictionary of filtered or exlcude data
- count - Returns a lenth of filtered or exlcude or dictionaries

> Please note that memory_repo does not support Q like objects offered by Django ORM, but offers a way around by passing
> anonymous function to filter or exclude function e.g repo.filter(age=lambda x: x >= 20 and x <= 30)

## Basic Usage

```python
from memory_repo import MemoryRepo

Accounts = ["A list of account objects that have attribute such as name, email, age, gender ect"]
repo = MemoryRepo(Accounts)

## Filtering and Excluding
# Filter accounts with age greater than 25 and exclude if gender is male
data = repo.filter(age__gt=20).exclude(gender='male')
# Filter using lamda  
data = repo.filter(age=lambda x: x >= 20 and x <= 30).exclude(gender='male')
# Filter accounts with the name starting with letter 's' and gender is female
data = repo.filter(name__istartswith='s').exclude(gender='female')
# Filter accounts who have registred from 2014 till 2016 of current date and who are a female
data = repo.filter(
    registered__date_range=(datetime.today().replace(year=2014), datetime.today().replace(year=2016))).exclude(
    gender='female'
)
# Filter accounts who have registred from 01-01-2015 till 2016 and who are a female if date is string object
data = repo.filter(registered__date_range=('01-01-2015', '01-01-2016')).exclude(gender='female')
```

```python
from memory_repo import MemoryRepo

Accounts = ["A list of account objects that have attribute such as name, email, age, gender ect"]
repo = MemoryRepo(Accounts)
# Filter accounts with age greater that 25 
data = repo.filter(age__gt=20)
# Filter accounts with age less that 25 and who are a male
data = repo.filter(age__lt=20, gender='male')
# Get number of accounts with age 20 and who are a female
data = repo.filter(age__gt=20, gender='female').count()
# Filter accounts with name starting with letter 's'
data = repo.filter(name__istartswith='s')
# Filter accounts who have registred from 01-01-2015 till 2016
data = repo.filter(registered__date_range=('01-01-2015', '01-01-2016'))
# Filter accounts who have friends who are a male
data = repo.filter(friends__gender='male')
# Filter accounts with date range
data = repo.filter(registered__value_range=('2015-11-15', '2015-11-16'))
# chain filter e.g
data = repo.filter(name__istartswith='s').filter(gender='male')
```

## Excluding

You can Exclude data by value or lookups such as gt, gte ect.
Below are code examples of exlcude function:

```python
from memory_repo import MemoryRepo

Accounts = ["A list of account objects that have attribute such as name, email, age, gender ect"]
repo = MemoryRepo(Accounts)

# Exclude accounts with age greater that 25
data = repo.exclude(age__gt=20)

# Exclude accounts with age less then 25 and who are a male
data = repo.exclude(age__lt=20, gender='male')

# Exclude accounts with name starting with letter 's'
data = repo.filter(name__istartswith='s')

# Exclude accounts who have registred from 01-01-2015 till 2016
data = repo.exclude(registered__date_range=('01-01-2015', '01-01-2016'))

# Exclude accounts who have friends who are a male
data = repo.filter(friends__gender='male')

# Chain exclude e.g.
data = repo.exclude(name__istartswith='s').exclude(gender='male')
```

## Ordering

You can order data by any value of object or dictionary :

```python
from memory_repo import MemoryRepo

Accounts = ["A list of account objects that have attribute such as name, email, age, gender ect"]

repo = MemoryRepo(Accounts)
# Order by name 
data = repo.order_by('name')
# Order name by descending
data = repo.order_by('-name')
# Ordering by related lookup of friends name
data = repo.order_by('friends__name')
# Ordering by related lookup of friends name descending
data = repo.order_by('-friends__name')
```





