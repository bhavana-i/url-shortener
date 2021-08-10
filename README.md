[**URL Shortener App**](https://weburlshortener.herokuapp.com/) - An application that reduces the length of URLs  

## Why I worked on this project

As part of my dev growth, I thought I'd build an application that ticked the following boxes:

* functionality: it should serve a specific purpose rather than just be a dummy application
* usefulness: users should derive some meaningful merit from it<
* instructiveness: it should be to me, an opportunity to learn and improve my software engineering skills


I decided on building an application that that shortens the length of URLs making them not only easier to share, but also convenient to monitor. Users would find value in it and I would also improve my backend engineering skills in the process of building it.


## Project Implementation 
This application was designed using Django's Model View Template (MVT) pattern.  

A single model was used to govern fields (e.g. the user's original long URL) and their behaviors (e.g. saving the shortened URL associated with each long URL). It was also used to keep track of the number of times a shortened URL was utilized.

The Views managed the form in which the user inputed their original URL and the display of the shortened URL. It also handled the redirection of shortened links to original web pages if they existed and returned a 404 otherwise. 

The templates which constitute the UI were created using HTML/CSS and Bootstrap elements. 

## How to navigate this project
* The model used to govern fields in the database: See [here](https://github.com/Wolemercy/url-shortener/blob/main/urlreduce/models.py)
* The Utility Function that generates the code for the shortened URL: See [here](https://github.com/Wolemercy/url-shortener/blob/main/urlreduce/urlreduce_utils.py)
* The Form that accepts the user's URL: See [here](https://github.com/Wolemercy/url-shortener/blob/main/urlreduce/forms.py)
* The Views that process the web requests: See [here](https://github.com/Wolemercy/url-shortener/blob/main/urlreduce/views.py)
* The Tests for the application: See example [here](https://github.com/Wolemercy/url-shortener/blob/main/urlreduce/tests/test_forms.py) 

## The Stack
The tech stack involved in this project are:

<ul>
  <li>Programming Language - Python</li>
  <li>Backend  Framework - Django</li>
  <li>Frontend  Framework - Django (with Bootstrap)</li>
  <li>Database - PostgreSQL</li>
  <li>Hosting - Heroku</li>
</ul>

## Opportunities for Improvement
If I have more time, I intend to add a couple of functionalities including (and probably beyond):
- showing users all the links they've created
- allowing users delete their created links
- dockerizing the application
- automating the tests
- making the UI a bit better  
