
## API Reference

#### Get all items

```http
  GET /api/v1/blog
```


#### Post item

```http
  POST /api/v1/blog
```

| Fields | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `VARCHAR` | **Required**. Title |
| `slug` | `CHAR` | **Optional**. your slug (default is generate slug + id generator) |
| `description` | `TEXT` | **Required**. content of your post |


