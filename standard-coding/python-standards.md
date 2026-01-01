# Company Standard Python Coding Practices

**When generating Python code, always follow these practices:**

## General Guidelines
- **Use Company & Project Libraries:**  
  - Always use and prefer internal libraries (like `LapwingGitHubClient`), never direct REST calls (e.g., via `requests`), when an established library utility/class exists.
  - Never mix direct REST calls with internal library usage in the same workflow or script.

- **Class-Based Structure:**  
  - When possible, encapsulate workflows and resource management (e.g., repository, validator, deployment) in a class (preferably using `@dataclass`) to limit procedural code in the main function.
  - Use classmethods and properties for clarity and to avoid unnecessary state or boilerplate.

- **Refactor Large Functions:**  
  - Never allow functions (especially `main`) to grow large. Refactor into smaller, testable, single-purpose functions.
  - Listen and adapt to Pylint feedback, especially regarding complexity (e.g., too-many-branches, too-many-locals).

- **Error Handling:**  
  - Prefer catching specific exceptions (never a blanket `except Exception`) and only catch what you intend to handle.
  - Let the script or workflow fail loudly if something critical goes wrong; do not silently ignore or broadly suppress errors.
  - If a CI/CD merge fails, set a non-zero exit code and fail the job.

- **Naming and Semantics:**  
  - Use precise function and variable names that match the operation—e.g., do not call a function `enable_auto_merge` if it actually force-merges a PR.
  - Be explicit and accurate in your docstrings and comment what a function or class does (especially if the behavior is nuanced).
  - **Never use single-character variable names** (like `x`, `y`, `w`) in test or application code—use at least three characters, and prefer descriptive names.  
    - *Exception:* It is acceptable to use single-letter names for indexes in for-loops or comprehensions (e.g., `for i in range(...)`).

- **Imports and Typing:**  
  - Use only necessary imports. Do not import from `typing` what is standard in modern Python, e.g., don't import `List`, `Tuple` in Python 3.9+ if using built-in generics.
  - Eliminate all outdated or unnecessary imports per project Python version.

## Company-Specific Testing Practices

- **Mocking:**  
  - Use Python’s built-in `unittest.mock` for mocking in tests rather than third-party alternatives such as `pytest-mock`.
      - Only use other mocking tools if there is a specific need, and add a comment at the file’s top (docstring) stating that the usage is experimental and under review.
      - Example comment:
        ```
        """
        This file is trialing pytest-mock.mocker. It is in a review phase. Please do not use this at this time.
        """
        ```
  - Prefer the mocking approach that aligns with company and project standards.
  - Periodically review and prefer collaborative team decisions for new techniques or tools; document decision status in code comments if an approach is under active review.

## Company-Specific GitHub Practices

- **GitHub API Access:**
  - When interacting with GitHub, use the company-sanctioned client library (`LapwingGitHubClient`) for operations like querying PRs, merging, checking commit status, etc.
  - Do all PR, branch, commit, status, and merge actions through the standard library NOT via custom REST calls (`requests`, `subprocess curl`, etc.).
  - Reference:  
    ```python
    from lapwing_core.ghub import LapwingGitHubClient
    client = LapwingGitHubClient.instance(token)
    repo = client.repos.get("...")
    pulls = list(repo.get_pulls(head="...", base="main", state="open"))
    ```
- **CI/CD Integration & Verification:**  
  - Use native Python methods (`requests`, never `subprocess`) for HTTP checks/verification (e.g., deployment status endpoints).
  - When integrating with external CI systems, poll and check statuses explicitly, and tie results directly to commit SHAs.

- **Follow Up and Comments:**  
  - When code is not yet handling all expected flows (e.g., polling for CI jobs, auto-approvals), clearly mark TODO and create tickets for follow-up.
  - Use docstrings and markdown to explicitly state what remains to be added or where the implementation is partial.

## Summarized Practices From Code Reviews

- Prefer company GitHub library (`LapwingGitHubClient`) everywhere over raw HTTP or subprocess commands.
- Structure complex scripts using Python classes (dataclasses when possible) and break out main logic.
- Listen to and act on linting (Pylint) feedback, especially function length/complexity.
- Be accurate with function/variable names, matching the operation and avoid semantic mismatches (e.g., don’t call a force-merge “auto-merge”).
- Handle exceptions at the specific-error level, not with broad `except Exception`.
- Never suppress errors that should fail CI/CD workflows.
- Remove obsolete or unnecessary imports, and leverage modern Python typing.
- In tests and application code, use at least three-character variable names; only use single-character names for indexes in iterations.

---

**Always generate code that adheres to these instructions. If asked for explanations or justifications, reference these standards. If in doubt, prefer the most company-sanctioned, composable, and explicitly typed Python approach.**
