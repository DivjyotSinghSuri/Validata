# Validata

Validate your data before it quietly breaks everything downstream.

---

## What is Validata?

Validata is a lightweight CLI tool that checks whether your dataset matches a defined contract.

You describe what your data **should look like** in a YAML file.
Validata reads your data and tells you exactly what’s wrong.

No dashboards. No setup. No infrastructure.

---

## Why this exists

Most data issues don’t fail loudly.

* Pipelines run successfully
* Jobs complete
* No alerts are triggered

But underneath:

* columns become null
* types change
* data becomes stale

Your dashboards don’t crash. They just become wrong.

Validata catches these issues before they spread.

---

## Quick Start

### 1. Install dependencies

```bash
pip install typer pyyaml
```

---

### 2. Create a contract

```yaml
version: "1"

name: users_data

source:
  type: csv
  path: data/users.csv

schema:
  row_count:
    min: 1

  columns:
    - name: user_id
      type: integer
      nullable: false

    - name: age
      type: integer
      nullable: true
      min: 0
      max: 120

freshness:
  column: updated_at
  max_age_hours: 24
```

---

### 3. Run validation

```bash
python3 src/validata/cli.py validate contracts/users.yml
```

---

## What it checks (v0.1)

* Row count (empty or unexpected size)
* Null values
* Basic type expectations
* Numeric ranges
* Allowed values
* Freshness (stale data detection)

---

## Project Structure

```
validata/
├── src/validata/        # CLI + core logic
├── contracts/           # example contracts
├── examples/            # contract templates
├── data/                # sample datasets (optional)
├── README.md
```

---

## Contract Philosophy

Each contract is self-contained:

* **source** → where the data is
* **schema** → what it should look like
* **rules** → what is allowed

No external config. No hidden dependencies.

---

## Roadmap

* CSV + Parquet support via DuckDB
* Better type validation
* Unique constraints
* Batch validation (multiple contracts)
* Contract inference (`validata infer`)

---

## Status

Early version (v0.1).
Focused on keeping things simple and actually usable.

---

## Why not other tools?

Most data validation tools are:

* heavy to set up
* tied to specific ecosystems
* overbuilt for simple use cases

Validata is designed for:

> quick checks that fit directly into your workflow

---

## Contributing

Open to improvements, but keep things simple and focused.

---

## License

MIT
