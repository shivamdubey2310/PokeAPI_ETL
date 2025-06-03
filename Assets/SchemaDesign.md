Here is a **normalized relational database schema** based on the endpoints and columns you've provided from the PokeAPI. This schema is designed to extract data from the specified endpoints and load it into a **MySQL** database while maintaining normalization (3NF).

---

## ⚙️ Tables & Schema Design

---

### **1. `pokemon`**
**Description:** Basic information about a Pokémon.

| Column Name         | Data Type     | Description                     |
|---------------------|---------------|---------------------------------|
| `id`                | INT (PK)      | Unique Pokémon ID               |
| `name`              | VARCHAR       | Name of the Pokémon             |
| `base_experience`   | INT           | Experience gained when defeated |
| `height`            | INT           | Height                          |
| `weight`            | INT           | Weight                          |
| `is_default`        | BOOLEAN       | Whether this is the default form |
| `order`             | INT           | Sort order                      |
| `species_id`        | INT (FK)      | References `pokemon_species(id)` |

---

### **2. `pokemon_species`**
**Description:** Species-level information.

| Column Name            | Data Type     | Description                          |
|------------------------|---------------|--------------------------------------|
| `id`                   | INT (PK)      | Unique species ID                    |
| `name`                 | VARCHAR       | Species name                         |
| `base_happiness`       | INT           | Base happiness                       |
| `capture_rate`         | INT           | Capture rate                         |
| `gender_rate`          | INT           | Gender rate                          |
| `hatch_counter`        | INT           | Hatch counter                        |
| `is_baby`              | BOOLEAN       | Whether it is a baby Pokémon         |
| `is_legendary`         | BOOLEAN       | Whether it is legendary              |
| `is_mythical`          | BOOLEAN       | Whether it is mythical               |
| `evolves_from_species` | INT (FK)      | References self (`pokemon_species.id`) |
| `growth_rate`          | VARCHAR       | Growth rate                          |
| `habitat`              | VARCHAR       | Habitat                              |
| `generation`           | VARCHAR       | Generation name                      |
| `shape`                | VARCHAR       | Pokémon shape                        |
| `color`                | VARCHAR       | Pokémon color                        |

---

### **3. `pokemon_ability`**
**Description:** Many-to-many relationship between Pokémon and abilities.

| Column Name     | Data Type     | Description                         |
|------------------|---------------|-------------------------------------|
| `pokemon_id`     | INT (FK)      | References `pokemon(id)`            |
| `ability_id`     | INT (FK)      | References `ability(id)`            |
| `is_hidden`      | BOOLEAN       | Whether it's a hidden ability       |
| `slot`           | INT           | Ability slot                        |
| **PK**: (`pokemon_id`, `ability_id`) |

---

### **4. `ability`**
**Description:** Details of each ability.

| Column Name     | Data Type     | Description          |
|------------------|---------------|----------------------|
| `id`             | INT (PK)      | Ability ID           |
| `name`           | VARCHAR       | Ability name         |
| `generation`     | VARCHAR       | Generation name      |
| `is_main_series` | BOOLEAN       | Is part of main series |

---

### **5. `pokemon_form`**
**Description:** Forms of Pokémon.

| Column Name     | Data Type     | Description                     |
|------------------|---------------|---------------------------------|
| `id`             | INT (PK)      | Form ID                         |
| `pokemon_id`     | INT (FK)      | References `pokemon(id)`        |
| `name`           | VARCHAR       | Form name                       |
| `form_name`      | VARCHAR       | Name of the form (in-game)      |
| `form_order`     | INT           | Form order                      |
| `is_default`     | BOOLEAN       | Whether this is the default form |
| `is_mega`        | BOOLEAN       | Whether this is a Mega Evolution |
| `is_battle_only` | BOOLEAN       | Used only in battle             |
| `version_group`  | VARCHAR       | Version group                   |

---

### **6. `type`**
**Description:** Pokémon types.

| Column Name | Data Type | Description  |
|-------------|-----------|--------------|
| `id`        | INT (PK)  | Type ID      |
| `name`      | VARCHAR   | Type name    |
| `generation`| VARCHAR   | Generation   |

---

### **7. `pokemon_type`**
**Description:** Many-to-many relationship between Pokémon and types.

| Column Name     | Data Type     | Description                 |
|------------------|---------------|-----------------------------|
| `pokemon_id`     | INT (FK)      | References `pokemon(id)`    |
| `type_id`        | INT (FK)      | References `type(id)`       |
| `slot`           | INT           | Type slot (1 = primary)     |
| **PK**: (`pokemon_id`, `type_id`) |

---

## 🔑 Primary & Foreign Key Summary

- **Primary Keys:** `pokemon.id`, `pokemon_species.id`, `ability.id`, `type.id`, `pokemon_form.id`
- **Foreign Keys:**
  - `pokemon.species_id` → `pokemon_species.id`
  - `pokemon_ability.pokemon_id` → `pokemon.id`
  - `pokemon_ability.ability_id` → `ability.id`
  - `pokemon_form.pokemon_id` → `pokemon.id`
  - `pokemon_type.pokemon_id` → `pokemon.id`
  - `pokemon_type.type_id` → `type.id`
  - `type_damage_relation.type_id` → `type.id`
  - `type_damage_relation.related_type_id` → `type.id`
  - `pokemon_species.evolves_from_species` → `pokemon_species.id`

---

Let me know if you want this schema visualized as an ER diagram or if you want a SQL `CREATE TABLE` script based on this!