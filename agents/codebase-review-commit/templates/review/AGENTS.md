# AGENTS.md - Review Instruction Router

## Purpose

This template provides only the review workflow.
Use `REVIEW.md` for normal reviews.
Use `REVIEW.md` plus `REVIEW_DEEP.md` for:

- deep reviews
- audits
- security reviews
- architecture reviews
- performance audits
- testing audits
- high-risk changes

## Routing rules

- Use `REVIEW.md` for standard repository, folder, file, diff, commit, branch, PR, or uncommitted-change reviews.
- Use `REVIEW.md` and `REVIEW_DEEP.md` together for deep, audit-style, or high-risk reviews.
- Do not use `REVIEW_DEEP.md` alone.
- If the user asks for commit messages or commit execution, explain that this template only includes review workflows unless commit instructions exist elsewhere in the project.

## Default behavior

- Prefer the smallest useful instruction set.
- Do not stage, commit, amend, reset, rebase, push, tag, or delete anything unless explicitly requested.
- If the request is ambiguous, choose the smallest safe review file set and state the routing assumption briefly.

## Typical mappings

```txt
review .                         -> REVIEW.md
review src/auth                  -> REVIEW.md
review --changed                 -> REVIEW.md
review --commit abc123           -> REVIEW.md
review --pr 123                  -> REVIEW.md
review src/auth --depth deep     -> REVIEW.md + REVIEW_DEEP.md
review src/payments --full       -> REVIEW.md + REVIEW_DEEP.md
audit src/auth                   -> REVIEW.md + REVIEW_DEEP.md
```
