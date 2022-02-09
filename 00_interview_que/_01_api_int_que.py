"""
API interview questions with sample answers

What is an API?
  “An API (Application Programming Interface) is a software that allows two applications to communicate with
   each other.”


What are some styles for creating a Web API?
 “Common Web API architectural styles are XML/JSON as a formatting language, stateless communication, basic URI as
 the address for the services and HTTP for communication between the client and server. Personally, I prefer XML
 over JSON.”

What is API testing?
“API testing is a type of software testing that determines if the developed APIs are functional, reliable and secure.
Some of the common API testing types are validation, security, UI, functional, load, penetration, runtime/error
detection, fuzz and interoperability and WS Compliance.”

What are the advantages of API Testing?
API testing gives access to the application without needing a user interface. This allows you to detect the minor
issues before they become big problems during GUI testing.

Also, API testing is typically less time consuming than GUI testing because it uses less code. As a result, it
offers a more effective and efficient test coverage.

Another benefit is that the data is transferred using XML or JSON. These modes of exchange are language-independent,
allowing users to select any coding language when choosing automation testing services. Additionally, API testing is
easily integrated with GUI testing.”


What is the procedure for performing API testing?
When performing API testing, you’ll first choose the suite where you’d like to add the API case that you wish to test,
then you choose the test development mode. After that, you create test cases for the desired API methods, configure
the control parameters and test conditions of the application as well as the method of validation. Then you can perform
the API test. Once the test is complete, you check the test reports, filter and sequence all of the API test cases.”

Top Interview Questions
What are the primary challenges of API testing?
I find selecting and combining parameters and sequencing calls to be the most challenging parts of API testing.”


What are some tools used for API testing?
A few popular tools are Katalon Studio, Postman, SoapUi Pro, Tricentis Tosca and Apigee. Personally, I prefer
SoapUi’s interface. It’s quick and really easy to use.”

What kinds of bugs does API testing find most commonly?
I have often used API testing to find several different issues, such as missing or duplicate functionality, failure
to handle errors effectively and seamlessly as well as any performance, stress, multi-threading, reliability or
security issues. However, unimplemented and improper errors, unused flags and inconsistent error handling are some of
the other errors that can be found through API testing.”

What is the difference between API and Web services?
Web services must be exposed over the web and have three styles of communication: SOAP, REST and XML-RPC. They always
need a network to operate. However, APIs have multiple methods of communication. A network is unnecessary for their
operation, and they don’t have to be exposed over the Web.”


What is SOAP?
"SOAP, also known as Simple Object Access Protocol, is an XML-based messaging protocol. It aids in the exchanging of
information between computers. You utilize SOAP API to make, find, delete or update records. In instances where there
are more than 20 different calls, SOAP API can be utilized to do searches and manage passwords by adapting the protocol
to whatever language supports web services.”

What is REST API?
REST, or Representational State Transfer, is a set of functions that help developers perform requests and receive
responses. Interaction is performed through HTTP Protocol. REST is stateless, so the server has no status or session
data. With an effectively-applied REST API, you can restart the server in between two calls. Web services typically
use the POST method to perform operations. REST, however, uses GET to access resources.”

What is the difference between SOAP and REST?
There are several differences between SOAP and REST. First, SOAP is a protocol through which two computers can
communicate by sharing XML, while REST is a service designed for network-based software architecture. Additionally,
SOAP supports only XML format, and REST supports a lot of different data formats. SOAP is unable to support caching,
and REST can.

SOAP is also less quick than REST and is similar to a desktop application, where it is closely connected to the server.
REST acts like a browser and uses standard methods. An application has to fit inside it. Lastly, SOAP runs on HTTP but
envelopes the message, while REST uses the HTTP headers to hold meta information.”

What factors help inform your decision on which style of Web services—SOAP or REST—to use?
REST is usually preferred because of its simplicity, performance, scalability and support across many data formats.
However, SOAP is a viable choice when service requires an advanced level of security and reliability.”

What tests can be performed on APIs?
Tests can and should be performed on APIs for several reasons, including testing the return values or inputting
 conditions.”

What kind of testing environment is needed for API?
Setting up the API testing environment can be difficult because you have to configure both the server and the database
 without the use of GUI.”

What’s the difference between UI and API testing?
UI, or user interface, testing is focused on examining the graphical interface of an application, such as how the user
can interact with its elements. API testing, on the other hand, sets up a mode of communication between two software
systems, allowing them to share sub-routines and functions.”

What is input injection?
Input injection refers to the simulation of user input.”

What are some ways that you can simulate user input?
You can accomplish input injection by utilizing a robot, a device driver or low-level input, just to name a few.”

What is Run scope?
Run scope is a Web application used to test APIs by supplying an accessible interface and backend services.”

Explain API documentation
Good API documentation is vital to the process. It supplies a quick reference while working within a program. It
provides the plan, delivery layout, sources the content and details every function within the system.”

What is Unit testing?
Unit testing, unlike API, is completed before adding code. It’s a type of white box testing that draws the source code
into the form and tests the basic functionalities of a system separately.”

Describe TestAPI
TestAPI is a sort of library that provides the building blocks for creating automated test suites and tools for
testing.”

What is the protocol for REST Web services?
HTTP is the protocol used in REST Web services. It facilitates communication between the server and the client.”

What is URI?
URI, or Uniform Resource Identifier, is a way to facilitate unambiguous identification of resources on a Web service’s
hosting server through a string of characters.”

What is caching?
Through caching, you’re able to temporarily store and retrieve data from your system’s memory. Caching mechanisms are
extremely effective and efficient because of their ability to improve the speed of delivery.”

"""