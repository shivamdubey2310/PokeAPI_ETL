# Tutorials for this are saved in json_explorer_tutorials.md 

def json_describe_to_md(json_data, output_file="output.md"):
    import os

    count = 0
    headers = [
        "Index", "Column", "Main Type", "Sub Type", "Sub Key",
        "Sub Sub Type", "Sub Sub Key", "Sub Sub Sub Type", "Sub Sub Sub Key"
    ]

    md_lines = ["| " + " | ".join(headers) + " |"]
    md_lines.append("|" + " --- |" * len(headers))

    for key, value in json_data.items():
        index = str(count)
        column_name = key

        main_type = str(type(value))
        sub_type = sub_key = ""
        sub_sub_type = sub_sub_key = ""
        sub_sub_sub_type = sub_sub_sub_key = ""

        if isinstance(value, (list, tuple)):
            if value:
                level_1 = value[0]
                sub_type = str(type(level_1))

                if isinstance(level_1, dict) and level_1:
                    sub_key_val = list(level_1.keys())[0]
                    sub_key = str(sub_key_val)
                    level_2 = level_1[sub_key_val]
                    sub_sub_type = str(type(level_2))

                    if isinstance(level_2, dict) and level_2:
                        sub_sub_key_val = list(level_2.keys())[0]
                        sub_sub_key = str(sub_sub_key_val)
                        level_3 = level_2[sub_sub_key_val]
                        sub_sub_sub_type = str(type(level_3))
                        sub_sub_sub_key = list(level_3.keys())[0] if isinstance(level_3, dict) else "N/A"
                    elif isinstance(level_2, (list, tuple)) and level_2:
                        sub_sub_sub_type = str(type(level_2[0]))
                        sub_sub_sub_key = "ListItem"
                    else:
                        sub_sub_sub_type = sub_sub_sub_key = "N/A"
                elif isinstance(level_1, (list, tuple)) and level_1:
                    level_2 = level_1[0]
                    sub_sub_type = str(type(level_2))
                    sub_key = "ListItem"

                    if isinstance(level_2, dict) and level_2:
                        sub_sub_key_val = list(level_2.keys())[0]
                        sub_sub_key = str(sub_sub_key_val)
                        level_3 = level_2[sub_sub_key_val]
                        sub_sub_sub_type = str(type(level_3))
                        sub_sub_sub_key = list(level_3.keys())[0] if isinstance(level_3, dict) else "N/A"
                    elif isinstance(level_2, (list, tuple)) and level_2:
                        sub_sub_sub_type = str(type(level_2[0]))
                        sub_sub_key = sub_sub_sub_key = "ListItem"
                    else:
                        sub_sub_sub_type = sub_sub_key = sub_sub_sub_key = "N/A"
                else:
                    sub_type = str(type(level_1))
                    sub_key = sub_sub_type = sub_sub_key = sub_sub_sub_type = sub_sub_sub_key = "N/A"
            else:
                sub_type = "Empty List/Tuple"
                sub_key = sub_sub_type = sub_sub_key = sub_sub_sub_type = sub_sub_sub_key = "N/A"

        row = f"| {index} | {column_name} | {main_type} | {sub_type} | {sub_key} | {sub_sub_type} | {sub_sub_key} | {sub_sub_sub_type} | {sub_sub_sub_key} |"
        md_lines.append(row)
        count += 1

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"✅ Markdown saved as: {output_file}")


# to generate json-schema 
def generate_json_schema(json_data):
    def infer_type(value):
        if isinstance(value, bool):
            return "boolean"
        elif isinstance(value, int):
            return "integer"
        elif isinstance(value, float):
            return "number"
        elif isinstance(value, str):
            return "string"
        elif isinstance(value, list):
            if value:
                return {"type": "array", "items": infer_type(value[0])}
            else:
                return {"type": "array"}
        elif isinstance(value, dict):
            return generate_json_schema(value)
        else:
            return "null"

    if isinstance(json_data, dict):
        schema = {"type": "object", "properties": {}}
        for key, value in json_data.items():
            schema["properties"][key] = infer_type(value)
        return schema
    else:
        return infer_type(json_data)


# Tree using rich.tree
from rich.tree import Tree
from rich.console import Console

def build_tree(obj, tree):
    if isinstance(obj, dict):
        for key, val in obj.items():
            branch = tree.add(f"[bold]{key}[/bold]")
            build_tree(val, branch)
    elif isinstance(obj, list):
        for i, item in enumerate(obj[:5]):  # limit to first 5 items
            branch = tree.add(f"[cyan]Item {i}[/cyan]")
            build_tree(item, branch)
        if len(obj) > 5:
            tree.add(f"... ({len(obj) - 5} more items)")
    else:
        tree.add(f"[green]{repr(obj)}[/green]")

def visualize_json_tree(json_data, output_file="json_tree.md"):
    tree = Tree("[bold magenta]JSON Structure[/bold magenta]")
    build_tree(json_data, tree)

    console = Console(record=True)
    console.print(tree)

    # Export to text/markdown file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(console.export_text())  # write plain text representation

    print(f"✅ JSON tree saved to {output_file}")