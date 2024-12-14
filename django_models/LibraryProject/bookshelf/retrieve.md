# Retrieve a Book Instance

In this operation, we retrieve the book instance that was previously created. We will use the title "1984" to fetch the record.

```python
# Retrieve the book instance by title
book = Book.objects.get(title="1984")
