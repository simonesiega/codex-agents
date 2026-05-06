# Full Template Example

## Template Pack

```txt
templates/full/
```

This example uses the full template. The router can load review instructions and commit instructions. Use this pack when you want both workflows available in the same target repository.

## Example Code

```txt
examples/full/password_reset.py
```

The Python code intentionally includes security-sensitive problems:

- Reset tokens never expire.
- Password reset logs the new password.
- Password storage is not implemented because this is a tiny example, so the review should focus on the visible behavior instead of inventing missing application context.

## User Command

```txt
review password_reset.py and then suggest commit
```

## Expected Routing

```txt
AGENTS.md -> REVIEW.md -> COMMIT.md
```

The request combines review and commit help. The agent should review first, then provide a commit recommendation based on the same scoped change.

## Output

This output was recorded from an agent pass using `templates/full/` against `password_reset.py`.

````md
## Findings

1. [P0] Raw passwords are exposed in logs
   - Location: `agents/codebase-review-commit/examples/full/password_reset.py:24`
   - Issue: `reset_password` prints the user's new password in plaintext.
   - Why it matters: This exposes credentials to logs/stdout and may leak passwords to operators, log aggregation, CI output, or incident artifacts.
   - Suggested fix: Never log passwords. Pass `new_password` to the real password update path, hash it securely, and log only non-sensitive metadata if needed.
   - Confidence: High

2. [P1] Reset tokens never expire
   - Location: `agents/codebase-review-commit/examples/full/password_reset.py:11`
   - Issue: `created_at` is stored but never checked during reset.
   - Why it matters: Any leaked or old reset token remains valid until replaced or used, increasing account takeover risk.
   - Suggested fix: Enforce a short token TTL in `reset_password` and delete expired tokens.
   - Confidence: High

## Residual risks

- The review was limited to `password_reset.py`; no callers, persistence layer, password hashing utilities, or tests were inspected.

## Tests and validation

- Tests run: None
- Tests not run: No test command was run.
- Commands checked: None

## Review coverage

- Scope reviewed: `agents/codebase-review-commit/examples/full/password_reset.py`
- Important files inspected: `agents/codebase-review-commit/examples/full/password_reset.py`
- Areas not reviewed: Callers, auth storage, email delivery, token generation tests, password hashing implementation

## Recommended commit

```txt
fix(auth): secure password reset token handling
```

## Why this commit

- Intent: Fix unsafe password reset behavior before committing it as production-ready auth code.
- Scope: Password reset token validation and credential handling.
- Includes: Removing plaintext password logging, enforcing token expiry, and ensuring reset behavior uses the secure password update path.

## Validation

- Tests run: None
- Tests not run: Password reset unit or integration tests
- Evidence used: Reviewed `agents/codebase-review-commit/examples/full/password_reset.py` only.
````

## Output Explanation

The full template should combine workflows in order: review first, commit second. The commit recommendation should not hide the review findings.

If this were a real change, the findings should be fixed before committing or called out clearly as unresolved risk.
