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