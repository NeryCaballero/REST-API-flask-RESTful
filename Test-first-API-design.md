# Test-first API design

The **Test first design** approch helps us design our APIs better and makes software development more efficient.

Simply put, it is writing a full description of the API functionalities before writing any code.

Thinking about this forces you to identify:

- What are the operations that we want our API to handle ?
- What are the necessary endpoints we have to make available ?
- Does the user needs to provide any information in order to respond to each request ? 
  - If yes, in which format? Which information is required, optional and/or unique?
- How do we want the response look like?
- What errors need to be handled?


###Implementation: 
Think about each and every request that the API is going to expect.

For each request:
1. Write down the endpoint through which is going to be accesible.
2. Write a short description for what this endpoint will do.
    - What it would return ?
        - In which format ? 
    - Does the request needs to provide any data?
        - In which format ? *This is a good way to identify which parameters need to be unique, required and optional.*
    - Which errors might it encounter?
    

### Functionalities of My API :

1. Get all items available: ```GET /items```
2. Get one item: ```GET /item/<name>```
    - by unique name, passed on the url.
    - If the item does not exist, it will display not found.
3. Create a new item: ```POST /item/<name>```
    - by unique name, passed on the url, 
    - required: price, passed on the Body, format JSON.
    - if the item already exists, it will fail.
4. Modify an existing item: ```PUT /item/<name>```
    - by unique name, passed on the url.
    - required: price, passed on the Body, format JSON.
    - if the item does not exists, it will create the item.
5. Delete an item: ```DEL /item/<name>```
    - by unique name, passed on the url.

* All functionalities require authentication token.

It is pretty clear  to see, that 4 out of the 5 functionalities can share the same endpoint using different HTTP request methods.