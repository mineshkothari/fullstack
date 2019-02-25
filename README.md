# [Fullstack](https://mk-fullstack.herokuapp.com/) | developed by Minesh Kothari

<br />
<br />

## Overview

### About Fullstack

Fullstack is an online hub bringing together web developers of all skillset and backgrounds whether they're a newbie, a hobbyist or even a veteran.

The website allows you to share knowledge through the Forum, learn how to code with our extensive Courses and becoming inspired reading through the Blogs.

### Who is it targeted at?

This project is targeted at anyone who wants to be kept up-to-date with Web Development. Whether you're a newbie finding your feet with the very first 'Hello, World' application using nothing but HTML, or a 10-year veteran who has what it takes to build the next 'big thing', Fullstack aims to bring the community closer. 

With Fullstack boasting various apps such as:
- Forum - a platform aimed to ask questions, stay connected and much more
- Blog - a platform aimed to inspire others and keeping everyone up-to-date with tech
- Courses - a platform aimed to develop everyone's skillset in web development

Is there really anywhere else you need to be?

### Why is there a Github repo for this project?

This project has been developed as part of my Stream 3 project for [Code Institute](https://codeinstitute.net/)'s Full Stack Web Development course. Upon completion of the course, I will gain a diploma in Software Development.

The 'Courses app' for this project uses e-commerce functionality using the Stripe API. The shop is in sandbox mode which means you're more than welcome to test the shop using the default sandbox card details and you wouldn't be charged. ;)

If you'd like to try this out, then you can add some items into the cart and enter the following details when prompted at checkout:

- Credit card number: **4242424242424242**
- CVV: **Any three digits (e.g 111)**
- Expiry Month & Year: **Any date in the future**

<br />
<br />

## User Experience

Fullstack is designed to give the end user a **_satisfied_** experience with its simplicity. 

Certain design practices inspired the design process of this project, to name a few:

1. Whitespace
2. Visual Hierarchy
3. Material Design 

Utilise key aspects of some of these 'good' practises helped me build a front end which offers the end user a luxurious visit. A great website starts with a good user interface, and Fullstack is no different.

Fullstack consists of 4 main areas:

1. **Courses** - If a user would like to learn about web design / web development, they can come here to browse through available courses and purchase them at checkout. This will give them access to the course which they can then use to improve their skills and knowledge.

2. **Blog** - If a user would like to keep up-to-date with the latest news, tech, trends and many more in the world of design and development, then the Fullstack Blog will have everyone covered. The user can browse through the list of blogs, read them and leave comments (via the Disqus API).

3. **Forum** - If a user is stuck on a particular problem, they can start a new thread, leave posts or reply to others to find the perfect solution, where someone from the community will be happy to help. Similarly, if you're an individual who thrives on helping others, you may wish to spend some time browsing through the threads replying to others and sharing your wisdom.

4. **Account** - Certain areas of this website requires you to log in. These can include scenarios such as purchasing courses and joining the discussions in the forum. If you'd like to be a part of the future at Fullstack, you can register an account with us through the registration page, login with valid credentials, update you personal details, view purchased courses and also requesting a 'forgot password' email.

<br />
<br />

## Features

### Features Implemented

Homepage
1. Act as a launchpad to the:
	- About page
	- Courses App
	- Blog App
	- Forum App
2. Personalised message if user logged in & link to 'My Profile'
3. Three featured Languages to choose from the homepage
4. Latest Blog Post on homepage

Courses App
1. View available languages and courses
2. Add a course to the Cart
3. View course (requires purchase)
4. Allow Admin to add a new Language
5. Allow Admin to add a new Module (Course) 

Cart App
1. Proceed to checkout with cart item(s)
2. Continue shopping
3. Remove item(s) from cart
4. Informative message if cart empty

Checkout App
1. Purchase item(s) in cart session
2. Informative message if cart empty

Blog App
1. View all posts
2. View 'Top' posts
3. Comment on blog with Disqus API
4. Allow Admin to add a new blog post
5. Allow Admin to edit existing blog post

Forum App
1. View forum subjects
2. View threads in each subject
3. Start a new Thread
4. View existing threads
5. Comment/reply on thread
6. Prompt user to register/login in order to contribute on thread
7. Edit post
8. Cast vote for polls
9. View Poll results
10. Allowing Admin to add a poll to a new Thread.

Account App (& Admin)
1. Registration - Allowing users to register
2. Login - Allowing users to login using their registered details
3. Password Reset - Allowing users to reset their forgotten password
4. Profile:
	- Allowing users to manage their profile
	- Allowing users to view their purchased courses
	- Allowing Admin to add a new Language
	- Allowing Admin to add a new Module (Course)

### Features yet to be implemented

Generic
1. Implement Page Not Found 404 (instead of redirect to home)

Courses App
1. Add a search option to search for courses
2. Add a filter to filter courses

Forum App
1. Delete a Thread post. **See Report > Known Bugs/Issues > Deleting thread posts**

Account App
1. Re-write the 'Forgot Password' email content.

<br />
<br />

## Technologies Implemented

### Languages Used

- HTML

As with every website or web based app, the use of Hypertext Markup Language is paramount. HTML5 has been used as the markup for this project as this would enable use of many of the new semantics to keep the structure of this project clear and in keeping with the latest industry standards.

- CSS

As with markup, Cascading Style Sheets are essential when controlling the layout of the website. Custom CSS was used in this project in conjunction with Bootstrap 4 to style the website, enhancing user interaction and delivering exceptional user experience.

- JavaScript

Custom JavaScript was used on this project as well as other JavaScript libraries such as jQuery for the mobile toggle menu button and responsive design choices.

- [Python](https://www.python.org/)

Python is the Back-end programming language used for this project, working in conjunction with the Django framework and its open library of essential packages. 

### Frameworks & Libraries

- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction)

The Bootstrap framework was used for this project to utilise various components such as Bootstrap's Navbar, Grid, Variables and many other utilities.

- [Django](https://www.djangoproject.com/)

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Django was utilised in the development of Fullstack to build various flexible and reusable apps across the site.

### Tools

- [NPM](https://www.npmjs.com/)

Node Package Manager was used to install Bootstrap 4 on this project. This approach is ideal as it allows greater flexibility when overriding Bootstrap's original Sass files.

- [SASS](https://sass-lang.com)

I used **SASS** as my chosen CSS pre-processor. This is a great way to import custom styles and override the original Bootstrap library. I also have the added benefit of using SASS variables along with other cool tricks. 

- [Git](https://git-scm.com/)

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. Git is easy to learn and has a tiny footprint with lightning fast performance.

### Database

- [SQLite](https://www.sqlite.org/index.html)

SQLite, included in Python, is a great lightweight database to get you up and running fast during the initial development stages and whilst running the project during the testing stages. Fullstack uses SQLite during the development stages.

- [PostgreSQL](https://www.postgresql.org/)

PostgreSQL, a powerful, open source object-relational database system is used as the database for the live website hosted on Heroku.

<br />
<br />

## Testing

Fullstack has undergone rigorous testing with each new implementation to ensure every aspect of this site works robustly.

*All tests were done on a Windows 10 64-bit PC unless otherwise stated*

### UX/UI Testing

Manual tests were carried out at every stage to ensure the user experience standards remained at consistently high levels with each new implementation, no matter how big or small. This proved an excellent way of identifying and thwarting any issues, reducing the time spent on bug fixes at the end of the project to a small fraction.

I ensured the website was thoroughly tested by people at regular intervals during development process and received some useful feedback on where to improve.

**Personal Details**

I used the email address to distinguish the users within the forum app as I knew this would be unique for every user and a quite simple to implement.

I was asked *"What if I don't want other people knowing my email address?"* by one of the testers, and quite rightly so. This was completely overlooked by me initially and to be in-keeping with good data protection practices, especially in light of GDPR, I knew I had a problem which I needed to resolve.

To encourage users from registering to the website and giving them a good user experience during this process, I wanted the registration form to be as short as possible. This implicated matters further as I did not want to include another field for the 'Display name' on the registration form. 

As a result, I included a separate form located on the 'My Profile' page where users are able to update their details and create their Username (with the default being 'Anonymous') as a way to identify them protecting their privacy.

**Contrast**

In order to achieve a good user experience, clear contrast is needed to ensure the users are able to read all the text on the webpage. Even if this meant a sacrifice to a 'cool' design.

Initially, I set transparent backgrounds for all the course items along with a light shade font colour and reduced font weight for the course details and description. Although this effect looked striking on a high-end 4K resolution panel (development machine), the results were less than favourable on a lower end display panel when testing.

After this was pointed out, I ensured that the contrast across the website was improved remarkably such as [here](https://mk-fullstack.herokuapp.com/courses/language/13/).

**Chrome Autofill on forms**

Personally, I was never a fan of Google Chrome's yellow Autofill so I initially set a custom shadow on the input field to hide the default yellow on the Autofill field.

However, after some user testing, I received valuable feedback where users found it extremely hard to see the mouse cursor on a dark background. This prompted me to revert back to the yellow background as this not only gives users a sense of familiarity, but improved user experience.

**Large Buttons**

One user in particular pointed out that some of the buttons were "Way too large" on mobile screen sizes. This is something I knew during the development process and it was particularly interesting to hear that other people thought the same. I then knew this would need to be looked into with importance and reduced the font-size and padding for buttons on smaller screen sizes.

### Responsive Design

Responsive design is key for any web development project. I ensured with every new implementation made to the Fullstack project, testing was carried out to validate or fix any responsive issues.

Some of the use cases includes:
1. Ensure the navbar is behaving as I envisioned it
2. Ensure forms are rendered correctly
3. Ensure all blog posts have sufficient padding

See the **Report > Responsive Design** section for more details. 

### Cross-Browser Testing

**Desktop Browsers Tested:**
```
Google Chrome 72
Mozilla Firefox 62.0.2
Microsoft Edge 42
Internet Explorer 11
```

**Mobile Browsers Tested:**
```
Samsung Internet (Samsung S8)
Chrome (Samsung S8, iPhone 6S)
Safari (iPhone 6S)
```

Being able to cater the website for all users is important, this includes the operating system they're using to the browser. Browsers have their own unique way of rendering certain HTML elements and CSS styles **_(User Agent Stylesheets)_** and it's important for the developer to ensure the website remains consistent across all platforms.

For this reason, thorough testing was done at regular intervals during the development of Fullstack to focus on ensuring the website behaved similar on the main browsers listed above.

When testing the website in Microsoft Edge v.41, I noticed major issues caused in the way the browser was rendering Flexbox. However, this was then tested again on Microsoft Edge v42 which has since resolved the way the browser renders Flexbox.

### Error Handling

Comprehensive testing was undertaken to ensure users received clear error messaging in the event something 'went wrong'.

So I tasked individual testers/users to try and force some errors and give me feedback on their experience.

This included tasks such as:
1. Enter an invalid email address during registration (e.g: email.com)
2. Enter an incorrect password during login
3. Visit checkout without adding items to the cart
4. Visit a language in the Courses app which didn't have any courses/modules ([Python](https://mk-fullstack.herokuapp.com/courses/language/16/))
5. Visit a forum with no threads ([Python](https://mk-fullstack.herokuapp.com/forum/threads/8/))
6. Enter incorrect details during checkout
7. Enter an invalid URL in the address bar

Whilst I anticipated these errors, it was important for me to understand the user's experience when something 'goes wrong' and whether they feel there's a clear message explaining the problem and how to either:

a. **Resolve the issue** 
	- Entering a valid email address during registration
	- Entering the correct password when logging in
	- Creating a new Thread in the forum

b. **Move past the problem**
	- Find another course from one of the available languages

The feedback was remarkable and the error messaging was well received. However, there was one notable issue:

**Registering with the same email**

When registering a new account with an email address that already exists in the database presented a **_UNIQUE constraint failed_** error message. In other words, a Server 500 error on the live site (which is never a good thing).

After searching to find a fix, I came across a Stack Overflow [thread](https://stackoverflow.com/questions/39600784/django-1-9-check-if-email-already-exists) which seemed to describe the same problem I faced. In *tredzko*'s solution, I found a fix to use ```cleaned_data``` to check if the username is taken.

**Invalid URLs**

Fullstack is set up in a way which redirects users to the homepage if an invalid URL has been entered in the address bar.

This was not only quick and easy, but only required a few lines of code as seen below:

```python
def my_custom_page_not_found_view(request):
    """
    In case page is not found, redirect user back to homepage
    """
    return redirect('index')

```

This ensures there are no unhandled exceptions when a user visits a webpage which doesn't exist.

I will be looking to use a dedicated page to view any "page not found 404 error" in future iterations of this project so users have an even clearer understanding about what has happened.

<br />
<br />

## Deployment

Fullstack is deployed to Heroku along with using AWS S3 to host static and media files.

### Heroku

Creating an app on Heroku is relatively easy and can be done in a couple of ways. Either from the terminal or via the online dashboard.

If you'd like to create a new Heroku app from the terminal, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), once installed on your computer, you can create your new app from within the terminal in just a few commands.

For more information on the Heroku CLI, read the CLI documentation [here](https://devcenter.heroku.com/articles/heroku-cli#getting-started).

Alternatively, you can also create a new Heroku app online from the dashboard by clicking on 'New' then 'Create new app'

Once your new Heroku app has been created, be sure to add the config vars to ensure the app works properly.

### Gunicorn & Procfile

**Gunicorn**

Gunicorn is used to run the application on Heroku. 

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.

In other words, this is exactly what we need as Heroku uses Ubuntu Server.

Gunicorn was installed on the virtualenv using ```pip install gunicorn```.

**Procfile**

[*Heroku apps include a Procfile that specifies the commands that are executed by the app on startup*](https://devcenter.heroku.com/articles/procfile).

The Procfile is essentially a file that’s named 'Procfile' (without any file extensions) and consists of information which is used by Heroku to tell it where to run the application.

Procfile:

```web: cd fullstack && gunicorn fullstack.wsgi:application```

*Please note: Due to the folder structure within the Github repository, there is an extra command to change directory into the project's root folder in order to locate the 'wsgi.py' file.*

In order to run the project locally, I needed to create another file named *Procfile.local*:

```web: cd fullstack && python manage.py runserver```

*Please note: I am using the Windows Operating System. For Mac OS/Linux, it would look something like this 'web: gunicorn fullstack.wsgi:application'*

### PostgreSQL Database

Unlike the SQLite database used for testing, the deployed version of Fullstack uses a more powerful database, PostgreSQL.

In order to use PostgreSQL, I installed an add-on called 'Heroku Postgres' from Heroku's dashboard, adding a new config variable for 'DATABASE_URL' to the app settings on Heroku. 

I then used the new config var within the Django app's settings to ensure we are pointing to the correct database when the project is live, ensuring the SQLite database is still being used during development/testing.

To ensure I connected to the new database correctly, two new packages were required:

**dj-database-url**

```console
$ pip install dj-database-url
```

A package to allow you to connect to a database URL (such as the one given to us when installing Heroku Postgres).

**psycopg2**

```console
$ pip install psycopg2
```

A package allowing you to connect to Postgres databases.

### AWS S3

The cloud-based AWS is used to serve static files for Fullstack. In order to achieve this, I created and configured an Amazon S3 bucket to ensure static images and project files were uploaded to it correctly.

One of the main benefits of using a cloud-based tool such as AWS S3 is that it frees up space on your servers, thus freeing up load times.

### Running Locally

Fullstack uses different environments depending on whether the project is live or in testing. If you're testing the project locally and would like to use the development environment, then you'll need to run the following command:

```console
$ set DJANGO_SETTINGS_MODULE=settings.dev
$ heroku local -f Procfile.local
```

Next, you should open your desired browser and go to your [localhost](http://127.0.0.1:8000/) ensuring you're on port 8000.

Similarly, if you'd like to view test the site using the live/staging settings then ensure you run the following command:

```console
$ set DJANGO_SETTINGS_MODULE=settings.staging
$ heroku local -f Procfile.local
```

For more information and the differences between each of the environments look at **Report > Hosting & Deployment** at the bottom of this README.

<br />
<br />

## Contributing

Fullstack is a personal project created as part of my Full Stack Web Development course. With that being said, it would be amazing to see the community getting involved by making or suggesting, improvements, bug fixes or some really interesting changes to this project.

**Things to consider:**

Fullstack relies on certain languages, tools and packages to be installed in order for it to run properly. A large proportion of these have been configured in such a way that you would not be required to make any additional changes to the files for these to work. However, there are some aspects you will need to be take into consideration when choosing to make changes to this project.

**Prerequisites:**
```
Python 2.7.14
SQLite
PostgreSQL
```

### Forking The Repo

1. In order to make changes, you will need to fork the repository. Click on the **Fork** button in the top-right corner of this page.
2. You will now need a copy of these files on your computer to make changes. To do this, you will need to clone or download the repo you forked in the previous step onto your local computer:
    - Click on the green **Clone or download** button
    - Under **Clone with HTTPS**, copy the clone URL for the repository
    - Open your Git terminal
    - Type ```git clone``` followed by the URL copied in the second step. This should look something like the following:
```console
$ git clone https://github.com/YOUR-USERNAME/fullstack.git
```
3. Once you have the file path all written down, go and hit Enter on your keyboard to request the clone.

And we’re done! Well almost.

### Making Changes

Amongst many of the tech, Fullstack uses Python 2.7 to power the website. You will need to ensure you have this version of Python installed on your PC for optimal usability. This project also uses several Python packages and it is strongly recommended having these installed on your local machine using a virtual environment for the project to function and run properly.

**virtualenv:**

You can create your own virtual environment using **_pip_** by running the following command from the project's root folder in your terminal: (please note - you will need to have *pip* installed as a Python package for this to work)

```console
$ pip install virtualenv
$ virtualenv env
```

*Please note: For Mac or Linux, you’ll need to use sudo: sudo pip install virtualenv*

This creates a new folder called *env* with our virtual environment in it. Once created you can go ahead and activate this by running the following command (ensure you are still in the project root folder):

```console
$ env\Scripts\activate
```

If the virtual environment is activated correctly, you will see *'(env)'* in front of the project location in the terminal as seen below:

```console
(env) C:\<ProjectFilePath>\fullstack>
```

Once activated, you can install the dependencies to the virtual environment using another **_pip_** command from the project's root folder in your terminal:

```console
$ pip install -r requirements.txt
```

*Please note: This walkthrough assumes you're installing the requirements which satisfy the final production site, you will need to install requirements in 'requirements/dev.txt' file for local testing*

**Migrating to the database:**

With a fresh new database, you'll need to run migrations to populate all the tables. Follow the command below (ensuring you're in the same folder as 'manage.py' file):

```console
$ python manage.py migrate
```

*Please note: You will not need to run the makemigrations command as we haven't yet changed our Models*

In order to work on the project locally, you will need an **_env.py_** file in the project's root folder with your config variables. See below for an example:

```python
import os

# SECRET KEY
os.environ.setdefault('SECRET_KEY', '<SECRET_KEY_GOES_HERE>')

# STRIPE KEYS
os.environ.setdefault('STRIPE_PUBLISHABLE', '<STRIPE_PUBLISHABLE_GOES_HERE>')
os.environ.setdefault('STRIPE_SECRET', '<STRIPE_SECRET_GOES_HERE>')

# DATABASE
os.environ.setdefault('DATABASE_URL', '<DATABASE_URL_GOES_HERE>')

# AWS KEYS
os.environ.setdefault('AWS_ACCESS_KEY_ID', '<AWS_ACCESS_KEY_ID_GOES_HERE>')
os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '<AWS_SECRET_ACCESS_KEY_GOES_HERE>')

# GMAIL CREDENTIALS
os.environ.setdefault('EMAIL_ADDRESS', '<EMAIL_ADDRESS_GOES_HERE>')
os.environ.setdefault('EMAIL_PASSWORD', '<EMAIL_PASSWORD_GOES_HERE>')

# DISQUS SETTINGS
os.environ.setdefault('DISQUS_WEBSITE_SHORTNAME', '<DISQUS_WEBSITE_SHORTNAME_GOES_HERE>')
os.environ.setdefault('DISQUS_API_KEY', '<DISQUS_API_KEY_GOES_HERE>')

```

Similarly, if you're looking to deploy the project on Heroku, you'll need to set the config variables under Heroku settings on the dashboard.

And there you have it. Now you're all set to make changes. You can open the project on you preferred text editor or IDE and begin making changes.

### Submitting Pull Requests

Now that you've made changes to the portfolio, you can submit a pull request to the master branch to await approval. To do this:
1. Navigate to the [original repository](https://github.com/mineshkothari/fullstack "https://github.com/mineshkothari/fullstack")
2. Click on **New pull request** on the right of the Branch menu
3. On the compare page, click **compare across forks**
4. Confirm that the *base fork* is the repository you'd like to merge into
5. Use the *head fork* drop-down menu to select your fork, then use the compare branch drop-down menu to select the branch you made your changes in
6. Type a little description for your pull request
7. If you do not want to allow anyone with push access to the upstream repository to make changes to your PR, unselect **Allow edits from maintainers**
8. Click **Create pull request**

For further information about forking a repository, please click [here](https://help.github.com/articles/fork-a-repo/).

For further information about creating pull requests, please click [here](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).

<br />
<br />

## Report

Want to learn about some of the known issues/bugs/limitations with this project? Continue reading to find out more. Perhaps, you will find a solution, or a better solution and if so - feel free to create a pull request with your changes.

### Responsive Design

Using the Bootstrap framework for this project put me in a good place to ensure the website is as responsive as it can be.

However, there were a few decisions I needed to make for improve the user experience for certain screen sizes.

**My Courses on the [Profile](https://mk-fullstack.herokuapp.com/account/profile/) page**

One of my main challenge was to use an intuitive way of presenting the purchased courses on the Profile page for larger displays as it required a bit of trial and error to ensure the breakpoints were sufficient along with the animation effects.

### Preventing Unauthorised Access

It is important to ensure users are only given access to content they're suppose to see.

**Courses**

Fullstack acts as an e-Commerce platform where users can purchase courses. However, it soon became apparent that by entering the URL for any given course directly onto the browser's address bar, then the users had full access to the course material - Free of charge.

This obviously isn't ideal when running an online shop, so in order to tackle this flaw, I needed to ensure an IF/ELSE statement was used to prevent users from accessing content they don't have access to.

```python
# If the user has purchased the module, display content
if module in request.user.module_set.all():
    return render(request, 'courses/module_item.html', {'module': module})

# If user has attempted to view content without a valid purchase, redirect to courses homepage
else:
    return redirect(reverse('courses'))
```

**New Languages/Modules**

Fullstack has a dedicated Admin interface (only visible to admins) where they're able to create new language categories or modules. 

However, a standard user can still access the ```new_language``` or ```new_module``` view by directly entering the URL into the browser address bar. In order to prevent an unauthorised user from accessing these pages, I needed to ensure that the user is of staff status before proceeding.

**Authenticated Users**

Having a dynamic navbar which changes the link options depending on whether the user is authenticated is particularly useful when improving the user experience. For example, we don't want to give a user an option to register when they are already logged in.

Although very unlikely, users can still access the [registration](https://mk-fullstack.herokuapp.com/account/register/) page when logged in by directly entering the URL into the browser. In order to prevent this, a check is made to identify whether the user is logged in, and if they are, then redirect them to the profile page.

### Closing Loops

A well-made website ensures that every situation or scenario is accounted for, as is the case with Fullstack.

I wanted to make sure that the users were given sufficient information when browsing the site and something 'went wrong'.

Even though Fullstack was not intended to be launched without any blog posts / forum topics / courses etc, it was important for me to develop the site with these things in mind. Asking myself questions such as:

- What happens when the user clicks on the [Blog](https://mk-fullstack.herokuapp.com/blog/) link, but there are no blogs?
- What happens when there are no forum topics?
- What happens when there are no courses?

This encouraged a 'Defensive' approach to the development and ensures that in the event something 'goes wrong' i.e. no courses available etc, then the user will be given sufficient information on what to do next.

**A good example of this can be seen [here](https://mk-fullstack.herokuapp.com/courses/language/16/) where there are no Python courses.** 

### Admin Area

I'm proud to announce that Fullstack comes with a lightweight 'CMS' where admins can create/edit language categories, modules/courses, blogs posts and many more - directly accessible from the front end.

When logged in as an admin, certain pages will have an orange menu with buttons/links allowing you to perform specific tasks as mentioned above. 

If you're an assessor and would like to try this feature, then please use the login credentials below:

Email: **admin@fullstack.com**

Password: **Password1234**

### Re-usable Apps

It was strongly encouraged to produce re-usable apps for this project. This is good practice when developing Django apps so we can use them across other projects and applications with minimum repetition and effort and all you'll need to do is install the app on your current project and you're almost good to go.

Each separate component/app for this project comes bundles with its own:
1. Templates folder - Where you'll find HTML files specific to the app
2. Static files - Where you'll find the SASS/CSS files specific to the app (these static files are linked separately to each app using 'block' tags in the HTML file to reduce the amount of CSS rules being loaded to each app unnecessarily).
3. urls.py - Where you'll find the URL patterns specific to the app

How I load the CSS:

```python

# home/base.html
{% block head_css %}{% endblock %}

# courses/courses.html
{% block head_css %}
    <link rel="stylesheet" href="{% static "css/pages/courses.css" %}">
{% endblock %}
```

And with just a few lines of code to the settings.py file and base urls.py file, you should be able to successfully hook up your existing app to a new project.

*Please note: if the re-usable app consists of database tables having been set previously in the **_models.py_** file, you will need to make migrations and run the migrations to ensure your project's schema has been updated. Type the following command in the terminal from your project's root folder:*

```console
$ python manage.py makemigrations
$ python manage.py migrate
```

### SASS Workflow

SASS is used as a CSS pre-processor for this project. I used SASS to gain a better understanding of how powerful CSS pre-processors are in general. Although I predominantly used SASS for nesting and indentation, I think this is a great place to start.

The SASS files are all kept inside the SASS folder in 'static' (with the exception of the re-usable app files).

Inside the SASS folder, you'll find various subfolders for components such as the navbar, forms, buttons and many more, making it simple to navigate through and find the SASS file to make changes.

There is also one 'stand-alone' SASS file **_style.sass_** within that folder (static/sass) which imports the sass files from all the subfolders acting as a table of contents. The key benefit of setting up the SASS workflow this way is to ensure when the SASS is being compiled to CSS, there will only ever be one CSS file, **_style.css_**, which I need to refer to in my base.html document.

```sass
// style.sass
@import "bootstrap/bootstrap"
@import "abstracts/variables"
@import "abstracts/typography"
@import "navbar/navbar"
@import "footer/footer"
@import "buttons/buttons"
@import "forms/forms"
@import "pages/base"
``` 

### Hosting & Deployment

As mentioned throughout the README documentation, Fullstack:

- Is hosted on Heroku
- Uses a local 'static' folder for testing
- Uses AWS S3 for live production
- Uses SQLite for testing
- Uses PostgreSQL for live production
- Has many other differences for improved productivity and better workflow

To configure the processes above came with a lot of challenges and pitfalls - but was well worth it in the end.

**settings.py**

The main focus was to have a clear separation with in the *settings.py* file for each environment and the best way to do this would be to split the settings.py file into three:

1. **base.py** - This holds all the common settings used with both the test environment and live environment.

2. **dev.py** - This holds any additional settings needed ONLY for the testing/development environment

3. **staging.py** - This holds any additional settings needed ONLY for the live/production environment.

**Development**

The development environment is where I've set ```DEBUG=True``` to ensure clear error messages are presented so I can debug problems quickly. 

This is also where I've connected to the SQLite database using the following:

```python
# dev.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

During the testing phase it also made sense to invoke the email backend through the terminal. This made it quick and to test, debug and configure the 'Forgot Password' functionality by sending the email requests straight through the console. When the project went live, I switched this to use Gmail’s SMTP. You'll find how I set this up under the Live header.

```python
# dev.py
# EMAIL BACKEND
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

**Live**

The live environment is where I've set ```DEBUG=False``` to prevent error messages from being viewed publicly.

I also used the staging environment to connect to the PostgreSQL database using ```dj_database_url``` **AND** configure the AWS S3 settings to host my static files.

```python
# staging.py
...
import dj_database_url
...

# Load PostgresDB
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# AWS S3 CONFIG
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = 'mk-fullstack'
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
```

As you can see, for these config vars, environment variables are used to protect malicious use of sensitive data. These variables are set in **_env.py_** (a file added to the .gitignore and subsequently not uploaded to Github).

The env.py file is imported in the **_base.py_** and designed to be used primarily during testing, regardless of whether we are connected to the development environment or staging.

However, when hosting this project live on Heroku's server, I no longer had access to these environment variables as they weren't uploaded to Github. In order to resolve this, I needed to ensure these config vars were all set under Heroku settings.

I put a *try, except* clause in place to avoid an `ImportError` when Heroku looks for a file which 'doesn't exist' (because env.py is not uploaded to Github):

```python 
try:
    import env
except ImportError:  # RELYING ON ENVIRONMENT VARIABLES
    pass
```

Other differences in the live environment include the Gmail settings used to send a 'Forgot Password' notification as seen below.

```python
# staging.py

# GMAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_ADDRESS')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587
```

As we've set ```DEBUG=False```, it would still be useful to see logs when testing the stating environment, so I added the following lines of code to output the log to the console.

```python
# staging.py

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
```

To help me test a particular environment locally, I run the following set of commands on the terminal:

**Development (dev.py) environment**

```console
$ set DJANGO_SETTINGS_MODULE=settings.dev
$ heroku local -f Procfile.local
```

Then I open [localhost](http://127.0.0.1:8000/) on my browser ensuring it's on port 8000.

**Live (staging.py) environment**

```console
$ set DJANGO_SETTINGS_MODULE=settings.staging
$ heroku local -f Procfile.local
```

Then I open [localhost](http://127.0.0.1:8000/) on my browser ensuring it's on port 8000.

### Known Bugs/Issues

**Deleting thread posts**

Deleting the last post from a forum thread raised the following exception:

```
AttributeError at /forum/thread/<post_id> 'NoneType' object has no attribute 'user'
```

In light of this known bug - I have had to 'disable' this feature for the time being to ensure the website has no unhandled exceptions. However, this is something I will be looking into outside the scope of this project.

**Disqus API**

Google Chrome's console throws a warning message in the console when viewing blog posts. I have been unable to debug the exact cause of this but will be looking into this in the near future.

```console
The resource https://c.disquscdn.com/next/embed/common.bundle.505b628fe4a369d7faa766dd8c23b076.js was preloaded using link preload but not used within a few seconds from the window's load event. Please make sure it has an appropriate `as` value and it is preloaded intentionally.

The resource https://disqus.com/next/config.js was preloaded using link preload but not used within a few seconds from the window's load event. Please make sure it has an appropriate `as` value and it is preloaded intentionally.

The resource https://c.disquscdn.com/next/embed/lounge.bundle.c9237ca4eec89ddb1320c66204dab595.js was preloaded using link preload but not used within a few seconds from the window's load event. Please make sure it has an appropriate `as` value and it is preloaded intentionally.

The resource https://c.disquscdn.com/next/embed/styles/lounge.7881ba4704e5c647ac74c94714fe89c0.css was preloaded using link preload but not used within a few seconds from the window's load event. Please make sure it has an appropriate `as` value and it is preloaded intentionally.
```

**TinyMCE Limitations**

TinyMCE is used across the site to power the forms fields used to create/edit blog posts, courses and forum posts. Although this is a good extension of a standard textfield, I have come across a few limitations.

These limitations include:

- Changing font style
- Changing font colour
- Adding hyperlinks*
- Using emojis

Some of these limitation are less important than others, but one that seems to stand out the most is the inability to add hyperlinks. I have noticed when adding blog posts that you can add hyperlinks, but only when copying and pasting them into the TinyMCE's HTMLFields. This means there are no options to set ```target="_blank"``` to the links either.

This poses a problem as it is good practise to open any hyperlinks to external sites in a new tab.

For the future, I will need to read more into the TinyMCE documentation to see whether I can toggle settings to enable this feature or to find an alternate solution to using TinyMCE altogether.

<br />
<br />

## Credits

### Courses

The guides from [HTML Dog](https://htmldog.com/guides/) were used as courses for this project

HTML Courses:

- HTML for beginners - [Getting Started](https://htmldog.com/guides/html/beginner/gettingstarted), [Tags, Attributes, and Elements](https://htmldog.com/guides/html/beginner/tags)

- HTML Headings - [Headings](https://htmldog.com/guides/html/beginner/headings/)

- HTML Lists - [Lists](https://htmldog.com/guides/html/beginner/lists/)

- HTML page titles - [Page Titles](https://htmldog.com/guides/html/beginner/titles/)

CSS Courses:

- CSS for beginners - [Applying CSS](https://htmldog.com/guides/css/beginner/applyingcss/)

- CSS Selectors - [Selectors, Properties, and Values](https://htmldog.com/guides/css/beginner/selectors/)

JavaScript Courses:

- Variables and Data - [Variables and Data](https://htmldog.com/guides/javascript/beginner/variables/)

### Blog Posts

- Becoming a Professional Web Developer - [freecodecamp.org](https://medium.freecodecamp.org/the-practical-guide-to-becoming-a-professional-web-developer-2f255bc25c90)

- Basic concepts of flexbox - [mozilla.org](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)

- 5 Amazing SASS Resourcess - [designshack.net](https://designshack.net/articles/css/30-amazing-resources-for-sass-lovers/)

- HTML vs Body in CSS - [css-tricks.com](https://css-tricks.com/html-vs-body-in-css/)

### Media

Free stock photos from [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/) were used for this project.

Many of the images from this site have been sourced from Unsplash. I created a [collection](https://unsplash.com/collections) which I called using their API https://source.unsplash.com/collection/ {COLLECTION ID} during testing. This worked particularly well as it's quick and lightweight. An example of how it was used can be seen below.

```css
section.intro {
    background: linear-gradient(rgba(245,245,245,1),rgba(204,204,204,0.6)), url("https://source.unsplash.com/collection/3320800/") no-repeat center center / cover;
}
```

Various Web development logos used in the Courses section were also sourced from [seeklogo.com](https://seeklogo.com/).

### Acknowledgements

- Slack Community - For bug fixes and recommendations

- Solution for **_UNIQUE constraint failed_** error message - [Tredzko's Solution](https://stackoverflow.com/questions/39600784/django-1-9-check-if-email-already-exists)
