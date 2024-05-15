## Dependency Injection in Python

A basic python application that showcases how DI (Dependency Injection) can make code much cleaner.

DI is especially useful when classes depend on a single shared instance of a class.
While this may be accomplished using global variables, having classes depend on global state
makes it easy to introduce unexpected behavior.

Moreover, by using a dependency injection container, it is clear what modules a class depends on by looking
at the constructor of the class.

In this demo, we will be using Python's `kink` library.

## Install dependencies

```
pip install -r requirements.txt
```

## Run the demo auth server
```
python server/server.py
```

## Run the tkinter application
```
python index.py
```