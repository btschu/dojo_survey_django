# dojo_survey_django

## Objectives:

- Practice creating a server with Django from scratch
- Practice adding routes to a Django app
- Practice having the client send data to the server with a form
- Practice having the server render a template using data provided by the client

Build a new Django application that accepts a form submission and presents the submitted data on a results page.

The goal is to help you get familiar with sending POST requests through a form and displaying that information. Consider the below example as a guide.

<img width="628" alt="Screen Shot 2022-04-19 at 9 19 03 PM" src="https://user-images.githubusercontent.com/92617960/164143634-d021e2b9-e09f-497b-a704-74f08ff6f5f3.png">

When you build this, please make sure that your program meets the following criteria:

- http://localhost:8000 - have this display a nice looking HTML form.  The form should be submitted to '/result'
- http://localhost:8000/result - have this display an HTML page with the information that was submitted by POST

### Don't forget that any inputs we want to be able to access from the form submission need to have a name!

It's always a good idea to print request.POST to see if the form is delivering all the information you need in your routing method.

- [ ] Create a new Django application

- [ ] Have the root route ("/") show a page with the form

- [ ] Have the "/result" route display the information from the form on a new HTML page

- [ ] NINJA BONUS: Use a CSS framework to style your form

- [ ] NINJA BONUS: Include a set of radio buttons on your form

- [ ] SENSEI BONUS: Include a set of checkboxes on your form
