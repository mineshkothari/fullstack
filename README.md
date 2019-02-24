# [Fullstack](https://mk-fullstack.herokuapp.com/) | developed by Minesh Kothari

<br />
<br />

## Overview

### About Fullstack

Fullstack is an online hub bringing together web developers of all skillset and backgrounds whether they're a newbie, a hobbyist or a veteran.

The website allows you to share knowledge through the Forum, learn how to code with our extensive Courses and becoming inspired reading through the Blogs.

### What is it for?

This project has been developed as part of my Stream 3 project for [Code Institute](https://codeinstitute.net/)'s Full Stack Web Development course. Upon completion of the course, I will gain a diploma in Software Development.

### Who is it targeted at?

This project is targeted at anyone who wants to be kept up-to-date with Web Development. Whether you're a newbie finding your feet with the very first 'Hello, World' application using nothing but HTML, or a 10 year veteran who has what it takes to build the next 'big thing', Fullstack aims to bring the community closer. 

With Fullstack boasting various apps such as:
- Forum - a platform aimed to ask questions, stay connected and much more
- Blog - a platform aimed to inspire others and keeping everyone up-to-date with tech
- Courses - a platform aimed to develop everyone's skillset in web development

Is there really anywhere else you need to be?

<br />
<br />

## User Experience

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

Forum App
1. Delete a Thread post **See Report > Known Bugs/Issues > Deleting thread posts**

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

I used **SASS** as my chosen CSS preprocessor. This is a great way to import custom styles and override the original Bootstrap library. I also have the added benefit of using SASS variables along with other cool tricks. 

- [Git](#)

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

I ensured the website was thoroughly tested by people at regular intervals during development process and recieved some useful feedback on where to improve.

**Personal Details**

I used the email address to distinguish the users within the forum app as I knew this would be unique for every user and a quite simple to implement.

I was asked *"What if I don't want other people knowing my email address?"* by one of the testers, and quite rightly so. This was something that was completely overlooked by me initially and to be in-keeping with good data protection practices, especially in light of GDPR, I knew I had a problem which I needed to resolve.

To encourage users from registering to the website and giving them a good user experience during this process, I wanted the registration form to be as short as possible. This implicated matters further as I did not want to include another field for the 'Username' on the regstation form. 

As a result, I included a separate form located on the 'My Profile' page where users are able to update their details and create their Username (with the default being 'Anonnymous') as a way to identify them protecting their privacy.

**Contrast**

In order to achieve a good user experience, clear contrast is needed to ensure the users are able to read all the text on the webpage. Even if this meant a sacrifice to a 'cool' desgin.

Initially, I set transparent backgrounds for all the course items along with a light shade font colour and reduced font weight for the course details and description. Although this effect looked striking on a high-end 4K resolution panel (development machine), the results were less than favourable on a lower end display panel when testing.

After this was pointed out, I ensured that the contrast across the website was improved remarkably such as [here](https://mk-fullstack.herokuapp.com/courses/language/13/).

**Chrome Autofill on forms**

Personally, I was never a fan of Google Chrome's yellow Autofill so I initally set a custom shadow on the input field to hide the default yellow when Chrome autofills the form fields.

However, after some user testing, I recieved valuable feedback where users found it extremely hard to see the mouse cursor on a dark background. This prompted me to revert back to the yellow background as this not only gives users a sense of familiarity, but improved user experience.

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
Google Chrome
Firefox
Microsoft Edge
Internet Explorer 11
```

**Mobile Browsers Tested:**
```
Samsung Internet (Samsung S8)
Chrome (Samsung S8, iPhone 6S)
Safari (iPhone 6S)
```

Being able to cater the website for all users is important, this includes the operating system they're using to the browser. Browsers have their own unique way of rendering certain HTML elements and CSS styles **_(User Agent Stylesheets)_** and it's important for the developer to ensure the website remains consistant across all platforms.

For this reason, thorough testing was done at regular intervals during the development of Fullstack to focus on ensuring the website behaved similar on the main browsers listed above.

### Error Handling

Comprehensive testing was undertaken to ensure users recieved clear error messaging in the event something 'went wrong'.

So I tasked individual testers/users to try and force some errors and give me feedback on thier experience.

This included tasks such as:
1. Enter an invalid email address during registration (e.g: email.com)
2. Enter an incorrect password during login
3. Visit checkout without adding items to the cart
4. Visit a language in the Courses app which didn't have any courses/modules ([Python](https://mk-fullstack.herokuapp.com/courses/language/16/))
5. Visit a forum with no threads ([Python](https://mk-fullstack.herokuapp.com/forum/threads/8/))
6. Enter incorrect details during checkout

Whilst I anticipated these errors, it was important for me to understand the user's experience when something 'goes wrong' and whether they feel there's a clear message explaning the problem and how to either:

a. **Resolve the issue** 
	- Entering a valid email address during registration
	- Entering the correct password when logging in
	- Creating a new Thread in the forum

b. **Move past the problem**
	- Find another course from one of the available languages

The feedback was remarkable and the error messaging was well recieved. However, there was one notable issue:

**Registering with the same email**

When registering a new account with an email address that already exists in the database presented a **_UNIQUE constraint failed_** error message. In other words, a Server 500 error on the live site (which is never a good thing).

After searching to find a fix, I came across a Stack Overflow [thread](https://stackoverflow.com/questions/39600784/django-1-9-check-if-email-already-exists) which seemed to describe the same problem I faced. In *tredzko*'s solution, I found a fix to use ```cleaned_data``` to check if the username is taken.

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

The cloud-based AWS is used to serve static files for Fullstack. In order to achieve this, I created and configured an Amazon S3 bucket to to ensure static images and project files were uploaded to it correctly.

One of the main benefits of using a cloud-based tool such as AWS S3 is that it frees up space on your servers, thus freeing up load times.

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

With a fresh new database, you'll need to run migrations to populate all the tables. In order to to this, you'll need to follow the command below (ensuring you're in the same folder as 'manage.py' file):

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



### Known Bugs/Issues

**Deleting thread posts**

Deleting the last post from a forum thread raised the following exception:

```
AttributeError at /forum/thread/<post_id> 'NoneType' object has no attribute 'user'
```

In light of this known bug - I have had to 'disable' this feature for the time being to ensure the website has no unhandled exceptions. However, this is something I will be looking into outside the scope of this project.

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



### Media

Many of the images from this site have been sourced from Unsplash. I created a [collection](https://unsplash.com/collections) which I called using their API https://source.unsplash.com/collection/{COLLECTION ID} during testing. This worked particularly well as it's quick and lightweight. An example of how it was used can be seen below.

```css
section.intro {
    background: linear-gradient(rgba(245,245,245,1),rgba(204,204,204,0.6)), url("https://source.unsplash.com/collection/3320800/") no-repeat center center / cover;
}
```

### Acknowledgements
