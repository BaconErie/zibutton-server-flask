Dev Doc
=======

Documentation related to developing zibutton server, not usage.

Contains important notes to keep in mind while coding.

Goals
=====

As a guideline, a goal is defined as a task that can be achieved by a single function. Functions include helper functions or view function. However, this is a guideline, not a rule, and exceptions can be made on what constitutes a goal.

- View all of a user's lists
- View a particular list
- Create/edit lists
- Study particular list
- Create accounts
- Login accounts
- Verify tokens and get id from tokens
- Sign out


View all of a user's lists
--------------------------

Path: /lists, /lists?user=<user_id>
API Path: /api/users, /api/users/<user_id>

If not logged in, then accessing paths with no user_id should be returned with 401 by server and redirect to /login by client

Server returns names and ids of the lists that are visible to the user

Get user from the token using the token verification function


View a particular list
----------------------

Path: /lists?list=<list_id>
API Path: /api/list/<list_id>

If list is private, then return 403 if wrong user or no user

If not auth fail, server should return list name, user name, user id, as well as a list of characters

Client will get the list using the API and render the list and everything



Create/edit lists
------------

