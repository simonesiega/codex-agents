# Usage

## Quick Start

Choose one template pack and copy it into the root of the target repository:

| Need | Copy |
|---|---|
| Full review + commit workflow | `templates/full/` |
| Review only | `templates/review/` |
| Commit only | `templates/commit/` |

The router is designed so the agent can start from `AGENTS.md` and follow only the workflow files needed for the current request.

This package stays modular on purpose: use the full set only when the target repository needs both review and commit workflows.

## Copy Commands

From inside `agents/codebase-review-commit/`, copy the chosen pack into the target repository root.

### Full package
macOS or Linux:

```bash
cp templates/full/* /path/to/project/
```

Windows PowerShell:

```powershell
Copy-Item templates/full/* C:\path\to\project\
```

### Review-only package 
macOS or Linux:

```bash
cp templates/review/* /path/to/project/
```

Windows PowerShell:

```powershell
Copy-Item templates/review/* C:\path\to\project\
```

### Commit-only package
macOS or Linux:

```bash
cp templates/commit/* /path/to/project/
```

Windows PowerShell:

```powershell
Copy-Item templates/commit/* C:\path\to\project\
```

Copy only one pack unless you are intentionally composing custom instructions. The copied `AGENTS.md` should be the target repository's entry point for this workflow.

## Full package usage

Use `templates/full/` when the target repository wants both review and commit workflows.

Included files:

```txt
AGENTS.md
REVIEW.md
REVIEW_DEEP.md
COMMIT.md
```

Typical requests:

| Request | Files loaded |
|---|---|
| `review .` | `AGENTS.md` to `REVIEW.md` |
| `review --changed` | `AGENTS.md` to `REVIEW.md` |
| `review src/auth --depth deep` | `AGENTS.md` to `REVIEW.md` and `REVIEW_DEEP.md` |
| `suggest commit` | `AGENTS.md` to `COMMIT.md` |
| `review changes and then suggest commit` | `AGENTS.md` to `REVIEW.md`, then `COMMIT.md` |
| `deep audit before commit` | `AGENTS.md` to `REVIEW.md` and `REVIEW_DEEP.md`, then `COMMIT.md` |

Recorded example: [`examples/full/EXAMPLE.md`](../examples/full/EXAMPLE.md).

## Review-only template usage

Use `templates/review/` when the target repository wants only code review workflows.

Included files:

```txt
AGENTS.md
REVIEW.md
REVIEW_DEEP.md
```

Typical requests:

| Request | Files loaded |
|---|---|
| `review src/auth` | `AGENTS.md` to `REVIEW.md` |
| `review --changed` | `AGENTS.md` to `REVIEW.md` |
| `review src/payments --full` | `AGENTS.md` to `REVIEW.md` and `REVIEW_DEEP.md` |
| `audit src/auth` | `AGENTS.md` to `REVIEW.md` and `REVIEW_DEEP.md` |

If the user asks for commit messages or commit execution, the template router should say that commit instructions are not included unless they exist elsewhere in the target repository.

Recorded example: [`examples/review/EXAMPLE.md`](../examples/review/EXAMPLE.md).

## Commit-only template usage

Use `templates/commit/` when the target repository wants only commit workflows.

Included files:

```txt
AGENTS.md
COMMIT.md
```

Typical requests:

| Request | Files loaded |
|---|---|
| `suggest commit` | `AGENTS.md` to `COMMIT.md` |
| `commit --staged` | `AGENTS.md` to `COMMIT.md` |
| `split these changes into commits` | `AGENTS.md` to `COMMIT.md` |

If the user asks for review, the template router should say that review instructions are not included unless they exist elsewhere in the target repository.

Recorded example: [`examples/commit/EXAMPLE.md`](../examples/commit/EXAMPLE.md).

## Example user requests

| Request | Files loaded | Notes |
|---|---|---|
| `review src/` | `REVIEW.md` | Standard scoped review |
| `review --commit abc123` | `REVIEW.md` | Single-commit review |
| `review src/auth --depth deep` | `REVIEW.md` + `REVIEW_DEEP.md` | High-risk or audit-style review |
| `review src/payments --focus security` | `REVIEW.md` + `REVIEW_DEEP.md` | Security-sensitive area |
| `suggest commit` | `COMMIT.md` | One commit recommendation |
| `commit --staged` | `COMMIT.md` | Message based on staged changes |
| `split these changes into commits` | `COMMIT.md` | Multi-commit grouping |
| `review changes and then commit` | `REVIEW.md` then `COMMIT.md` | Review before naming or creating a commit |

## Recommended workflows

### Normal review

- Load `REVIEW.md`.
- Inspect only the requested scope and the smallest useful related context.

### Deep review

- Load `REVIEW.md` and `REVIEW_DEEP.md`.
- Use the deep file only when the request is audit-like, high-risk, or explicitly deep.

### Commit suggestion

- Load `COMMIT.md`.
- Inspect only enough to describe the change accurately.

### Commit split

- Load `COMMIT.md`.
- Group by intent, reviewability, and rollback safety rather than by file count.

### Review before commit

- Load `REVIEW.md` first.
- If the review is deep or high-risk, also load `REVIEW_DEEP.md`.
- Load `COMMIT.md` only after the review step.

## Keeping token usage low

- Keep `AGENTS.md` short and route from there.
- Do not load `REVIEW_DEEP.md` for normal reviews.
- Do not load `COMMIT.md` during review-only work.
- Do not expand review scope into unrelated code just because it exists.
- Prefer template packs when a project needs only one workflow family.

## Notes on not loading unnecessary files

- `REVIEW.md` is the default review file.
- `REVIEW_DEEP.md` is an extension, not a default.
- `COMMIT.md` is for commit help, not general review.
- Template routers should mention missing workflows briefly instead of improvising them.
- If a request is ambiguous, choose the smallest safe file set and state the routing assumption.

## Common Mistakes

- Do not copy multiple template packs into the same repository unless you are deliberately merging them.
- Do not load `REVIEW_DEEP.md` for every review; it is an extension for deep, audit-like, or high-risk work.
- Do not use `COMMIT.md` as a substitute for code review.
- Do not claim tests, builds, or checks were run unless a command actually ran.
- Do not expand review scope into unrelated code just because the repository is available.
