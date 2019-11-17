# python3-logger-vs-logging
understanding python logger hierarchy

$ python src/main.py 
```
INFO:root: * main.py * 
INFO:root: * app.client imported * 
INFO:[app.client]: * app.client imported * 
INFO:root: * main.py: Client().greet() 
INFO:[Client.greet]: * logger from Client.greet() * 
INFO:root: * logging from Client.greet() * 
```
