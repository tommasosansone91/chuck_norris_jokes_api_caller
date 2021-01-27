# Oneflow - Backend developer Assignment

Create an API using flask as presented below.

## General

All of your commits must be here, we want to see how you work.

**Register everything** including your tests/spikes, ideas if you had more time (explain how would you solve things), decisions you've made (and why), the architecture you chose. Add a `COMMENTS.md` or a `HISTORY.md` to show us your thoughts and ideas.

## The assignment
![](https://api.chucknorris.io/img/chucknorris_logo_coloured_small.png)

The applicant should design and implement a minimalistic flask API application that would let the user search, create, delete and update jokes from [Chuck Norris jokes](https://api.chucknorris.io/), that works through for example Postman.

We expect the applicant to at least implement these endpoints (but feel free to add more):

- GET /api/jokes/
- POST /api/jokes/
- GET /api/jokes/id
- PUT /api/jokes/id
- DELETE /api/jokes/id

## Technical assumptions

- You should use [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- You should consider how you would scale the API for other types of jokes and more functionality per category

## Extras

Focus on the basics and on solving the main problem, but you can also:

- Add documentation
- Add unit tests
- Add extra options/attributes to endpoints to make them more powerful

## What are we evaluating?

1. The described features and requirements.
2. Any extras you've added to your final solution.
3. Any other creative thing or feature you added by yourself.
4. In general: simplicity, clarity of your solution, architecture, documentation, code style, interface design, and the code.

## Tips

- We want you to show us how you work, break down bigger problems and prioritize them.
- It's an option to not implement everything, mock anything you think it's gonna save you time.
- It's better if you show us something small that works and is well factored rather than something complete but "buggy"
- It's better if you use open-source libraries and explain why you chose them.
- If you have any questions, please ask us :)
