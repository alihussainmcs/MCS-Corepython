"""
20.jinja2 template?

Jinja2 is a full-featured template engine for Python. It has full unicode support, an optional
integrated sandboxed execution environment, widely used and BSD licensed.

Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template
allow writing code similar to Python syntax. Then the template is passed data to render the
final document.

Jinja2 is a Python library that you can use to construct templates for various output formats
from a core template text file. It can be used to create HTML templates for IBM® QRadar® applications.


==>Why do we need Jinja 2?

Sandboxed Execution: It provides a protected framework for automation of testing programs, whose
is unknown and must be investigated.

HTML Escaping: Jinja 2 has a powerful automatic HTML Escaping, which helps preventing Cross-site
Scripting (XSS Attack). There are special characters like >,<,&, etc. which carry special meanings
in the templates. So, if you want to use them as regular text in your documents then, replace
them with entities. Not doing so might lead to XSS-Attack.

Template Inheritance: This is the most important feature, which I will expand on to later in the post.


"""