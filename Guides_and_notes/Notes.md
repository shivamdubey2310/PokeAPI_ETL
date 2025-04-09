## Notes
### 1. To get the key names from the response from an api 
```python
# To get the names of key in the response
    key_names = json_response.keys()
    print(key_names)
```
--------

### Creating schema file for json response
```python
file_name = "pokemon_json_schema.md"
helper.json_describe_to_md(pokemon_json_response, file_name)
```
---

### Detailed schema of a json file
```bash
json-explorer json_file_name.json
```

----

