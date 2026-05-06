# Review-Only Template Example

## Template Pack

```txt
templates/review/
```

This example uses the review-only template. The router can load `REVIEW.md` and `REVIEW_DEEP.md`, but it has no commit workflow. Use this pack when you want code review behavior without commit-message guidance.

## Example Code

```txt
examples/review/user_service.py
```

The Python code intentionally includes several reviewable problems:

- SQL is built with an f-string.
- The database connection is never closed.
- `is_admin` is returned as the raw SQLite value instead of a boolean.

## User Command

```txt
review user_service.py
```

## Expected Routing

```txt
AGENTS.md -> REVIEW.md
```

This is a standard scoped review. The user does not request a deep audit, security focus, or commit help, so the router should load only the default review workflow.

## Output

This output was recorded from an agent pass using `templates/review/` against `user_service.py`.

```md
## Findings

1. [P1] Parameterize the user lookup query
   - Location: `agents/codebase-review-commit/examples/review/user_service.py:8`
   - Issue: `user_id` is interpolated directly into the SQL query with an f-string.
   - Why it matters: If `user_id` comes from a request path, CLI argument, or other untrusted input, a caller can alter the query and read unintended rows.
   - Suggested fix: Use a parameterized query, for example `cursor.execute("SELECT id, email, is_admin FROM users WHERE id = ?", (user_id,))`.
   - Confidence: High

2. [P2] Close the database connection after reading the profile
   - Location: `agents/codebase-review-commit/examples/review/user_service.py:5`
   - Issue: The SQLite connection is opened but never closed.
   - Why it matters: Repeated calls can leak file handles and keep database resources open longer than needed.
   - Suggested fix: Close the connection in a `finally` block or use a context that explicitly closes the connection after use.
   - Confidence: High

## Residual risks

- Only `user_service.py` was reviewed.
- Callers and tests were not inspected, so the source and type of `user_id` were inferred from the function boundary.

## Tests and validation

- Tests run: None.
- Tests not run: Unit tests for `get_user_profile`.
- Commands checked: None.

## Review coverage

- Scope reviewed: `agents/codebase-review-commit/examples/review/user_service.py`.
- Important files inspected: `agents/codebase-review-commit/examples/review/user_service.py`.
- Areas not reviewed: Database schema, caller input validation, authentication or authorization checks.
```

## Output Explanation

The review template should put findings first and should not suggest a commit message. This output focuses on concrete code issues, reports validation honestly, and avoids expanding into unrelated files.
