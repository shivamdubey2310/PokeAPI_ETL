Certainly! Here's a comprehensive tutorial on two powerful Python tools for exploring and documenting JSON data: **`json-explorer`** and **`json-schema-for-humans`**.

---

# 📘 JSON Exploration and Documentation Tools Tutorial

This tutorial covers:
1. **Exploring JSON Data with `json-explorer`**
2. **Generating Human-Readable JSON Schema Documentation with `json-schema-for-humans`**

---

## 🔍 1. Exploring JSON Data with `json-explorer`

### 🧠 Purpose:
`json-explorer` is a command-line tool that helps you interactively explore the structure and contents of JSON data, especially useful when dealing with large or complex JSON files.

### ✅ Use Case:
Quickly understand the properties, data types, and unique values within JSON objects, making it easier to analyze API responses or data dumps.

### 💻 Installation:

```bash
pip install json-explorer
```

*Note: `json-explorer` is a lightweight tool with no dependencies and supports Python 3.7 and above.*

### 🚀 Usage:

1. **Prepare Your JSON Data:**
   - Save your JSON objects, one per line, in a file (e.g., `data.jsonl`).

2. **Run `json-explorer`:**

   ```bash
   json-explorer data.jsonl
   ```

   This command launches a web-based interface displaying the structure and statistics of your JSON data.

3. **Explore the Data:**
   - Navigate through the web interface to inspect properties, data types, and unique values.
   - Use this insight to construct queries with tools like `jq` or `jmespath` for further data manipulation.

### 📂 Example:

Suppose you have a JSON Lines file named `data.jsonl` with the following content:

```json
{"id": 1, "name": "Alice", "roles": ["admin", "user"]}
{"id": 2, "name": "Bob", "roles": ["user"]}
```

To explore this data:

```bash
json-explorer data.jsonl
```

This will open a web interface where you can interactively examine the structure and contents of your JSON data.

*For more details, refer to the [json-explorer PyPI page](https://pypi.org/project/json-explorer/).*

---

## 📝 2. Generating Human-Readable JSON Schema Documentation with `json-schema-for-humans`

### 🧠 Purpose:
`json-schema-for-humans` is a Python package that generates beautiful, static HTML or Markdown documentation from a JSON Schema, making it easier to understand and communicate the schema's structure and constraints.

### ✅ Use Case:
Create user-friendly documentation for JSON Schemas to facilitate better understanding among developers and stakeholders.

### 💻 Installation:

```bash
pip install json-schema-for-humans
```

### 🚀 Usage:

1. **Generate Documentation:**

   ```bash
   generate-schema-doc path/to/your_schema.json
   ```

   By default, this command creates an HTML documentation file named `schema_doc.html` in the current directory.

2. **Customize Output:**
   - **Specify Output File:**

     ```bash
     generate-schema-doc path/to/your_schema.json path/to/output.html
     ```

   - **Generate Markdown Documentation:**

     ```bash
     generate-schema-doc --config template_name=md path/to/your_schema.json
     ```

   - **Minify HTML Output:**

     ```bash
     generate-schema-doc --minify path/to/your_schema.json
     ```

     *Minification is enabled by default.*

3. **View Documentation:**
   - Open the generated `schema_doc.html` or `schema_doc.md` file in your browser or Markdown viewer to explore the human-readable documentation.

### 📂 Example:

Given a JSON Schema file `schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "User",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "The unique identifier for a user."
    },
    "name": {
      "type": "string",
      "description": "The name of the user."
    },
    "email": {
      "type": "string",
      "format": "email",
      "description": "The email address of the user."
    }
  },
  "required": ["id", "name", "email"]
}
```

To generate documentation:

```bash
generate-schema-doc schema.json user_schema_doc.html
```

Open `user_schema_doc.html` in your browser to view the rendered documentation.

*For more information, visit the [json-schema-for-humans GitHub repository](https://github.com/coveooss/json-schema-for-humans).*

---

## 🛠️ Summary

| Tool                      | Purpose                                         | Installation Command             | Usage Example                                               |
|---------------------------|-------------------------------------------------|----------------------------------|-------------------------------------------------------------|
| `json-explorer`           | Interactive exploration of JSON data structures | `pip install json-explorer`     | `json-explorer data.jsonl`                                  |
| `json-schema-for-humans`  | Generate human-readable documentation from JSON Schemas | `pip install json-schema-for-humans` | `generate-schema-doc schema.json output.html`               |

---

By integrating these tools into your workflow, you can efficiently explore complex JSON data and create comprehensive, user-friendly documentation for your JSON Schemas.

--- 