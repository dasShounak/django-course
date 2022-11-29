# Django

## 9/ Models-Templates-Views Paradigm

---

Django operates on the Models-Templates-Views paradigm. Also called “MTV”, it encompasses the idea of how these three are connected

Steps:

1. In the `views.py` file we import any models that we will need to use.
2. Use the view to query the model for data that we will need.
3. Pass results from the model to the template.
4. Edit the template so that it is ready to accept and display the data from the model.
5. Map a URL to the view.
