# playground

A sandbox repository for small utilities, experiments and automation practice.

## Contents

| Path | What it is |
| --- | --- |
| `src/text_utils.py` | `slugify` and `truncate` string helpers |
| `src/retry.py` | Retry decorator with exponential backoff and jitter |
| `tests/` | pytest suite for the modules above |

## Running the tests

```bash
python -m pip install pytest
python -m pytest
```

## Conventions

- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/).
- Formatting rules live in `.editorconfig`.
- Every change lands through a pull request, even solo ones.
