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
