# API

## 1. What are APIs? How are they used and why are they so popular?
Application Programming Interfaces are a set of rules, tools and protocols that allow different applications to communicate with each other. they do this by defining methods and the data formats that applications can request and exchange data. APIs are used for development, integration and to access services. This makes APIs popular as they increase efficiency by reusing existing functionalities, enabling scalability and offloading tasks to specialised services. This allows developers to combine services in new and creative ways.     
## 2. Create a diagram to showcase the data transfer process in API communication

## 3. What is a REST API? 
Representational State Transfer is a web API that follows the REST architecture.  
### What makes an API RESTful?
  
The Key Features:
- **Statelessness**: Requests contain all necessary information; server doesn't store client state between requests.
- **Client-Server Architecture**: Client and server are separate, enhancing scalability and simplifying the architecture.
- **Uniform Interface**: Standard operations used HTTP methods and resource URIs.
- **Resource-based**: Resources are manipulated by using well-defined operations.
- **Layered System**: Allows for intermediaries like proxies and gateways to be inserted between clients and servers.      


### What are the REST API guidelines?
REST APIs follow guidelines consistency and usability.

**Guidelines:**
     
- Use nouns for resources (/users). 
- HTTP methods for operations.
- Utilise HTTP status codes (404 Not Found).
- Meaningful error messages.
## 4. What is HTTP? 
   - HTTP is a protocol that is used for communication on the internet. HTTP stands for Hyper Text Transfer Protocol.  HTTPS is an extension of HTTP that adds a layer of security. This is done by encrypting the data that was transmitted between the client and server.

## 5. Explain HTTP request structure using the diagrams provided, or your own (see attachments)

## 6. Explain HTTP response structure using the diagrams provided, or your own (see attachments)

## 7. What are the 5 HTTP verbs? 
- **GET**: 
    
  Request data from a specified resource, and with the information it collects it doesn't make any changes to the resource.

- **POST**:

  Used to submit data to be processed to a specified resource. Creates a new resource often as a result.

- **PUT**:

  With the data provided, it updates a specified resource. Creates a new resource if it does not exist or replaces the existing one.

- **DELETE**:

  Used to request the removal of a specified resource.

- **PATCH**: 

  Used when only a part of the resource needs updating. This is done by making partial modifications.

## 8. What is "statelessness"? 
Satelessness is the context of HTTP that each request from the client to the server has all the information that the server needs to fulfill the request.
   
## 9. What is caching?
Caching is the process of storing frequently accessed data. This is done by storing the data in a cache which is in a temporary strorage location so future requests are served more quickly.  