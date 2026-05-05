# AGENTS.md - Review and Commit Instruction Router

## Purpose

This repository provides three task-specific instruction files:

- `REVIEW.md` - default code review workflow
- `REVIEW_DEEP.md` - optional deep-review extension
- `COMMIT.md` - commit naming, grouping, and commit execution rules

Use this file to route the agent to the right file or combination of files.
Keep routing simple. Load only the files needed for the current request.

## Routing rules

- For normal review requests, use `REVIEW.md`.
- For deep reviews, audits, security reviews, architecture reviews, performance audits, testing audits, or other high-risk changes, use `REVIEW.md` and `REVIEW_DEEP.md` together.
- For commit messages, commit grouping, Conventional Commit formatting, or requested commit execution, use `COMMIT.md`.
- If the user asks to review before committing, use `REVIEW.md` first, then `COMMIT.md`.
- If the user asks for a deep audit before committing, use `REVIEW.md` and `REVIEW_DEEP.md` first, then `COMMIT.md`.
- If the user asks only for a commit message or commit split, do not perform a full code review unless the user asks for one.

## File roles

### `REVIEW.md`

Use for repository, folder, file, diff, commit, branch, PR, or uncommitted-change review.
This is the default source of truth for:

- scope discipline
- review workflow
- severity model
- finding format
- review output format
- fix-mode rules

### `REVIEW_DEEP.md`

Use only as an extension to `REVIEW.md`.
Do not use it by itself as a replacement review file.
It adds deeper inspection heuristics for high-risk or audit-style reviews.

### `COMMIT.md`

Use for:

- commit message suggestions
- Conventional Commit formatting
- commit splitting or grouping
- commit bodies and breaking-change footers
- requested commit execution

It is not the default review file.

## Default behavior

- Prefer the smallest useful instruction set.
- Do not load `REVIEW_DEEP.md` unless the request is deep, audit-like, or high-risk.
- Do not treat commit naming as a full review task.
- Do not duplicate output formats across files; follow the format defined in the file you routed to.
- If multiple files apply, use them in this order: review files first, commit file second.
- If the request is ambiguous, choose the smallest safe file set and state the routing assumption briefly.

## Typical mappings

```txt
review .                         -> REVIEW.md
review src/auth                  -> REVIEW.md
review --changed                 -> REVIEW.md
review --commit abc123           -> REVIEW.md
review main..feature --deep      -> REVIEW.md + REVIEW_DEEP.md
review src --full                -> REVIEW.md + REVIEW_DEEP.md
audit src/payments               -> REVIEW.md + REVIEW_DEEP.md
suggest commit                   -> COMMIT.md
commit --staged                  -> COMMIT.md
split these changes into commits -> COMMIT.md
review changes and then commit   -> REVIEW.md + COMMIT.md
deep audit before commit         -> REVIEW.md + REVIEW_DEEP.md + COMMIT.md
```
