
An application that reduces the length of URLS  
**Link to App:** https://weburlshortener.herokuapp.com/

**Goal**  
The goal of this project was to build an application that that shortens the length of URLs making them not only easier to share, but also convenient to monitor.

**Implementation**  
This application was designed using Django's Model View Template (MVT) pattern. A single model was used to govern fields (e.g. the user's original long URL) and their behaviors (e.g. saving the shortened URL associated with each long URL).  
The Views contained the form in which the user inputed their original URL and returned the shortened link. It also handled the redirection of shortened links to original web pages if they existed and returned a 404 otherwise.  
The templates were created using HTML/CSS and Bootstrap elements. 

**Stack**  
The tech stack involved in this project are:

<ul>
  <li>Programming Language - Python</li>
  <li>Backend  Framework - Django</li>
  <li>Frontend  Framework - Django (with Bootstrap)</li>
  <li>Server - Apache</li>
  <li>Database - PostgreSQL</li>
</ul>

**Development**  
The development was done in a Windows environment using Git Bash and Windows Terminal

**Deployment**  
The deployment was handled using Heroku's free-tier cloud resources




