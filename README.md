WENDY
=====

# Setup

## Prerequisites

- Python >= 3.8

## Requirements

```bash
$ pip install -r requirements.txt
```

# Commands

```bash
python cmd/wendy -h      
usage: WENDY [-h] [--gen-repo] [--repo-name REPO_NAME] [--migrate]

optional arguments:
  -h, --help            show this help message and exit
  --gen-repo, -r        Auto-gen repository files
  --repo-name REPO_NAME, -n REPO_NAME
                        Repo name
  --migrate, -m         Performing migrations
```

## Migrations

- Using `aerich`:

```bash
$ aerich migrate --name update
```

- Using `wendy`

```bash
$ python cmd/wendy -m
```

## Generate repository files

```bash
$ python cmd/wendy -r -n Building
```
