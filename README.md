# 🚀 Airflow DAGs Repository

Welcome to the **Airflow DAGs repository**! This repository contains all your **data workflows** orchestrated using **Apache Airflow**. It is designed to be **clean, scalable, and easy to maintain**.

Whether you’re ingesting **stocks, cryptocurrencies**, or any other data pipelines, this repo is your single source of truth for Airflow orchestration.

---

## 📦 Features

* One DAG per file 📝
* Modular and reusable utilities 🧩
* Organized by **projects** for scalability 📂
* Ready for local development and deployment to Airflow environments 🌐

---

## ⚙️ Requirements

* Python 3.13+ 🐍
* [Apache Airflow](https://airflow.apache.org/) 3.0+
* [`uv`](https://uv.io/) as a package manager ⚡

> This project uses **`pyproject.toml`** for dependencies.

---

## 🛠️ Setup (Local Development)

Follow these steps to get started quickly:

### 1. Clone the repository

```bash
git clone git@github.com:<your-org>/airflow-dags.git
cd airflow-dags
```

### 2. Install dependencies using `uv`

```bash
uv install
```

> This will read the `pyproject.toml` and install all required packages into a **virtual environment** managed by `uv`.

### 3. Activate the environment

```bash
uv shell
```

Now you’re inside the **project environment**, ready to run or test DAGs.

### 4. Optional: Run tests

```bash
pytest tests/
```

---

## 📂 Repository Structure

```text
airflow-dags/
├── dags/                 # All DAG files organized by domain/project
├── plugins/              # Custom operators, sensors, hooks
├── tests/                # Unit tests for DAGs and utils
├── config/               # Connections, variables, environment configs
├── scripts/              # Utility scripts for backfill, validation, etc.
├── pyproject.toml        # Project dependencies
├── README.md             # This file
└── .gitignore            # Ignore generated files, venv, logs, etc.
```

---

## 📝 DAG Guidelines

* One DAG per file ✅
* DAG IDs: `<project>__<purpose>`
* Use **tags** for categorization (`finance`, `crypto`, `monitoring`)
* Keep business logic **outside** DAG files, in `utils/` or `plugins/`

---

## 🔐 Security Notes

* **Do not commit secrets**. Use Airflow Variables or Connections for sensitive info.
* `.env` files are ignored by Git — keep a `.env.example` for reference.

---

## 💡 Tips

* Use `uv shell` whenever you work on DAGs to ensure the environment is consistent.
* Run `pytest` before pushing new DAGs to catch import errors early.
* Document new DAGs clearly, with a description at the top of the file.

---

## ❤️ Contributing

1. Fork the repo
2. Create a new branch for your feature or DAG
3. Run tests locally (`pytest tests/`)
4. Submit a pull request

---

## 📞 Contact / Support

For questions, issues, or help with Airflow DAGs:

* Reach out to the **data engineering team**
* Or create an **issue in this repository**

---

> Happy orchestrating! ☁️📊⚡