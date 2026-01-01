# 🐍 Additional Python Best Practices

## Project Structure & Code Organization

### Follow a Standard Project Structure
- Organize code into logical packages/modules.
- Separate source files into `src/` (or similar) and tests into `tests/`.
- Place configuration files (e.g., `.env`, `.env.sample`, `pyproject.toml`) at the repository root.
- **Never** hard-code secrets or credentials in source code files.

### Use Configuration Management
- Load credentials and configurations from environment variables or configuration files; never hard-code sensitive data.
- For sensitive values, use secure vaults or other secrets management solutions when possible.

### Document Public APIs
- Write docstrings for all public modules, classes, and functions using [Google](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods), [NumPy](https://numpydoc.readthedocs.io/en/latest/format.html), or [Sphinx](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain) style, as appropriate.
- Use type annotations for all function signatures.

---

## Testing & Quality Assurance

### Write Tests for All New Code
- Achieve and maintain high code coverage, but prioritize meaningful, high-value tests over coverage percentage alone.
- Use parameterized tests for variations.
- Test both the success and failure/error cases.
- For mocking, prefer Python’s built-in `unittest.mock` unless otherwise specified.

### Adopt Code Formatting and Linting Tools
- Use a formatter (`black`, `ruff`, or `autopep8`) to enforce a consistent code style.
- Run static type checkers (`mypy`, `pyright`) and linters (`pylint`, `flake8`, or `ruff`) as part of CI/CD.
- Include configuration for these tools in the repo, and document their use in `CONTRIBUTING.md`.

---

## Dependency Management & Packaging

### Pin and Audit Dependencies
- Specify exact versions in `pyproject.toml` and/or `requirements.txt`. **Never** use loose or unbounded requirements in production.
- Periodically run security and dependency update tools (`pip-audit`, Dependabot, `safety`).
- Remove unused dependencies and keep requirements files up to date.

---

## Performance & Security

### Avoid Premature Optimization
- Write clear and correct code first; optimize only after profiling and identifying real bottlenecks.
- When optimizing, provide comments or documentation explaining the optimization trade-offs.

### Handle External Inputs Safely
- Always validate and sanitize external inputs (from APIs, user input, etc.).
- Use context-managed resources (`with` statements) for files, network connections, etc., to ensure proper cleanup.

---

## Collaboration & Documentation

### Version Control Best Practices
- Write descriptive commit messages, referencing ticket/issue numbers when possible.
- Prefer feature/topic branches; submit changes through PRs with clear descriptions and proof of passing tests.

### Comprehensive README & Examples
- Ensure the project’s `README.md` explains how to set up, test, use, and contribute to the codebase.
- Provide usage examples for major functions/classes (in the README, as docstrings, or in a `/examples/` directory).

---

## Miscellaneous

### Use Logging, Not Print
- For production/logworthy messages, use Python’s `logging` module and set up loggers at the module level.
- Use appropriate logging levels: `debug`, `info`, `warning`, `error`, `critical`.

### Avoid Anti-Patterns
- **Do not** use wildcard imports (`from module import *`).
- **Never** check in secrets or private credentials. Use `.gitignore` for secret or local files.

---

## Prompt Addendum (Pre-Commit/PR Checklist)

**Before submitting code or PRs, confirm:**
- Linting passes with no new errors/warnings.
- All tests pass locally and in CI.
- You have added or updated relevant docstrings and documentation.
- No secrets or credentials are present in your changes.
- All external libraries used are reflected in the dependencies manifest and reviewed for security.

---
