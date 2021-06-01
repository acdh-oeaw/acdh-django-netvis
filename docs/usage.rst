=====
Usage
=====

render netvis in an objects detail view
---------------------------------------

To display a network in a template you'll need to

* import the needed JavaScript libraries (via template tag `{% load_netvis_js %}`
* create and style a div to place the visualiziation
* initialize `showGraph` function by passing an url providing the graph data and the `id` of the element where the visualization should be rendered

.. code-block:: html

    {% load static %}
    {% load netvis_extras %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            ....
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            {% load_netvis_js %}
        </head>
        <body>
            ...
            <div id="visualization" style="position: relative; height: 700px; background: #fafafa;"></div>
            <script type="text/javascript">
            showGraph("{% url 'netvis:graph' app_name='example' model_name='mytext' pk=object.id %}", "visualization")
            </script>
        </body>
    </html>



