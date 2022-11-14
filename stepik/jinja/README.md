{{ name }} - переменная

```html
<p>2+2 = {{ 2 + 2 }}; 0.33 / 2 = {{ '{:.1%}}'.format(0.33 / 2) }}</p>
```
<pre>
2 + 2 = 4; 0.33 / 2 = 16.5%
</pre>


{{ name | filter }}

```html
{{ "<p>Some text!</p>"|striptags|title }}

{{ 1.2345678 | round(2) }}
```

{% conditions %} - операторы ветвления

```html
{% if 'am' in 'lambda' %}
    <p>True</p>
{% endif %}

{% if age > 5 %}
    <p>False</p>
```

```html
{% if year % 400 == 0 or (year % 100 != 0 and year % 4 ==0) %}
    <p>Leap</p>
{% else %}
    <p>Not Leap</p>
{% endif %}
```

циклы

```html
{% for item in ['Pen', 'Pencil', 'Notebook'] %}
    <li>{{ item }}</li>
```
Условие `ELSE` если итерируемая последовательность пуста
```html
<ul>
    {% for user in {} %}
        <li>{{ user }}</li>
    {% else %}
        <li>dict is empty</li>
    {% endfor %}
</ul>
```