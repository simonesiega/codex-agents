# AGENTS.md - Commit Instruction Router

## Purpose

This template provides only the commit workflow.
Use `COMMIT.md` for:

- commit message suggestions
- Conventional Commit formatting
- commit grouping or splitting
- commit bodies
- breaking-change footers
- requested commit execution

## Routing rules

- For commit messages, commit grouping, Conventional Commit formatting, or requested commit execution, use `COMMIT.md`.
- Do not perform a full code review from this template alone.
- If the user asks for review, explain that this template only includes the commit workflow unless review instructions exist elsewhere in the project.

## Default behavior

- Prefer the smallest useful instruction set.
- Do not stage, commit, amend, reset, rebase, push, tag, or delete anything unless explicitly requested.
- If the request is ambiguous, choose `COMMIT.md` only when the user is clearly asking for commit help.

## Typical mappings

```txt
suggest commit                   -> COMMIT.md
commit --staged                  -> COMMIT.md
commit --changed                 -> COMMIT.md
commit --body                    -> COMMIT.md
commit --breaking                -> COMMIT.md
write commit message             -> COMMIT.md
split these changes into commits -> COMMIT.md
commit these changes             -> COMMIT.md
```
