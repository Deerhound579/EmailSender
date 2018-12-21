# Notes on BeautifulSoup4

#### `.contents` and `.children`

A tag's children are available in a list called `.contents`

```python
head_tag = soup.head
head_tag
# <head><title>The Dormouse's story</title></head>

head_tag.contents # Head has one child: <title>
#[<title>The Dormouse's story</title>]

# Access all children using index
title_tag = head_tag.contents[0] 
title_tag
# <title>The Dormouse's story</title>
title_tag.contents
# [u'The Dormouse's story']
```

#### Name&Attributes&Strings

Every tag has a name, accessible as `.name`

Access a tag's attributes by treating the tag like a dictionary

A string corresponds to a bit of text within a tag

```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
tag.name #'b'
# You can change a tag's name:
tag.name = "blockquote"
# Access attributes
tag['class'] # 'boldest'
tag.string # 'Extremely bold'
# Deleting an attribute
del tag['class']
# Replace a string
tag.string.replace_with("No longer bold")
```

