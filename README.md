# About Portfolio APP
 This is a portfolio app which can be integrated to multiple user for any system. Rightnow it is for single superuser where in a profile class:
* name
* profile picture
* hobby
* address
* company
* school name and year
* highschool name and year
* university name and year
* 6 skills can be added

 And in about me class, about user is added.

## BACKEND Development
>Here, class based views are used so that with less code and efficiency, it can be developed.

>To pass multiple context, extra_context attribute is used. For example, to show a card containing image, name, hobby, address, company in every page, I used extra_context to pass all objects of Profile model in homeview, projectview, aboutmeview, editview of Profile and Abooutme models.


## FRONTEND Development

Here, css, js, bootstrap are used in html with proper breakpoint as screen size decreases.

To show the projects, I used github api to fetch the repos and github. For example:

>  fetch('https://api.github.com/users/DibashBikramThapa/repos')<p>
   .then(response => response.json())<p>
   .then(function gitclick(data){<p>
    _here, js query to show the project title and link url_ <p>
        })

#### For database, default sqlite3 is used locally and deployed in heroku.
