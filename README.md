# Happy Project 😊

### A project to *empower* needy-students.

Happy Project is a non-profit initiation founded by IT people from Jaffna, Sri Lanka. This is to help students in need
and couldn't get hold of it. This project is originally targetted towards Sri Lankan Students, but people from other
region also, with few alteration to the source code.

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Refer deplyment section for deployment process.
**It is recommended to create an isolated environment as Happy Project uses latet, pre-release versions to stay
future proof**

### Prerequisites

All the backend and neccessary prerequisites are mentioned in `requirements.txt`. They are mostly...
```
django **4.0**
django-storages
whitenoise
gunicorn
django-heroku
psycpg
```

### Installing as a dev
1. Create a dev env

```
python3.10 -m venv env
pip3.10 install -r requirements.txt
```

2. Populate the environment variables

Edit the .env file accordingly and **especially the SECRET_KEY**

3. Migrate

```
# not neccessary to indicate python3.10 as the env is already created with python3.10
# it is assumed that the current working dir is the root dir

python manage.py migrate
```

## Running the tests

Please if someone can, write tests and create a pull request


## Deployment

Originally, Happy Project is deployed as webapp in [Heroku](https://www.heroku.com). Hence, you will
see `Procfile; runtime.txt;` etc. But the source itself can be hosted anywhere that can run django apps.

***In future, it is anticipated that a desktop(offline) version can be supported via APIs***

## Versioning

Happy Project uses [SemVer](http://semver.org/) for versioning. 

## Authors

* **Shanthosh** - *Initial work* - [Happy-Project](https://github.com/Happy-Project)
* **Birnadin E.** - *Code Authoring* - [Birnadin Erick](https://github.com/BirnadinErick)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

**Hope this will help you one way or the other**

### </> with 💖 from Jaffna, Sri Lanka
