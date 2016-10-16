# bmframework
How to use this framework: to use networkhelper, make sure to install psycopg2. Otherwise, simply import the parser, call networkhelper to login to your remote console port. Call parse with your socket, and your list. Your list is a list of functions with method signature: dictionary, socket, **kwargs. 
Let parse do the rest. To stop parsing, keyboard break, and it will automatically deallocate socket.
