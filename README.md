django-project-templates
========================

Some Django project/app templates for various things.

### Templates

These are the templates `django-project-templates` includes:

#### Projects

* **default**: A barebones project that includes `local_settings.py` support,
directories for static and media files, `SITE_URL` and `SITE_NAME` variables,
logging, initial email variables, `south`, `django-extensions`, etc.

#### Apps

* **custom_user_nousername**: An app that includes models with UUIDs (provided
by [shortuuid](https://github.com/stochastic-technologies/shortuuid)) instead
of integer ids, a custom `User` model that uses the email as the primary field,
and corresponding admin interface machinery to make this work.

### Usage

Before starting a project with Django 1.6+, do the following:

```bash
git clone git@github.com:skorokithakis/django-project-templates.git
```

Pick the template you want and prepare for awesomeness:

```bash
django-admin.py startproject --template=/cloned/dir/django-project-templates/projects/your-pick/ yourproject
```

or

```bash
./manage.py startapp --template=/cloned/dir/django-project-templates/apps/your-pick/ yourapp
```

Start coding your amazing project and sell it for a cool billion.

### License

The provided templates are licensed, under, hmm, let's say the New BSD license. That should do it.
