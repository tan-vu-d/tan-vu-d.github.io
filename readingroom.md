---
layout: page
title: archive
permalink: /archive/
---
<head>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <meta charset='utf-8'>
    <title>
        {% if page.title %} {{ page.title }} {% else %} {{ site.name }} &mdash; {{ site.description }} {% endif %}
    </title>
    <link rel="icon" type="image/png" href="/favicon.png" />
</head>

{%- if site.posts.size > 0 -%}
  <ul>
    {%- for post in site.posts -%}
    <li>
      {%- assign date_format = "%Y-%m-%d" -%}
      [ {{ post.date | date: date_format }} ] <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
    </li>
    {%- endfor -%}
  </ul>
{%- endif -%}

