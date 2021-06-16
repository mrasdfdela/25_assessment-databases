### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
**PostgreSQL is a relational database for managing interrelated tables and records that can be queried, updated, and deleted**

- What is the difference between SQL and PostgreSQL?
**PostgreSQL is a 'flavor' of SQL--a specific implementation of that shares much of the same syntax and functionality**

- In `psql`, how do you connect to a database?
**In the command line, type \c \<databasename\>**

- What is the difference between `HAVING` and `WHERE`?
**Having is used in conjunction with the GROUP BY operator; WHERE is used for filtering on a table**
- What is the difference between an `INNER` and `OUTER` join?
**INNER will join tables where record references match; OUTER will show all records whether or not the references match**
- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
**LEFT OUTER will join by showing all records on the statements' left-most table; RIGHT OUTER will join by showing all records on the right-most table**
- What is an ORM? What do they do?
**Object relational modeling is a way to map records in a database to objects in a language that can be manipulated**
- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
**AJAX requests are done asynchronously from the client and the server will return data without the page refreshing. For the `requests` library, the server can make requests and serve a full webpage**
- What is CSRF? What is the purpose of the CSRF token?
**It is a security token sent to a client from the server so that it can be returned and verify that requests are being made by that server**
- What is the purpose of `form.hidden_tag()`?
**In Jinja, this hides the Flask form of CSRF tokens in the UI** 