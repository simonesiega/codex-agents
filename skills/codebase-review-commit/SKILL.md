---
name: codebase-review-commit
description: Use when asked to review code, diffs, branches, PRs, staged changes, uncommitted changes, run deep audits, suggest or split Conventional Commits, or create commits only after an explicit user request.
---

# Codebase Review and Commit Skill

Use this skill to route Codex through a focused code review, deep audit, commit recommendation, commit split, or review-before-commit workflow.

This file is the lightweight router. Load only the supporting reference files needed for the user's request, then follow those files as the source of truth for workflow, safety, and output format.

## When Not to Use

- Do not use for unrelated coding tasks, generic project planning, or broad documentation writing.
- Do not use when the user asks to implement fixes without also asking for review, audit, or commit help.
- Do not use for repository exploration unless it directly supports a review or commit workflow.

## References

The supporting files live in `references/`:

| Reference | Use for |
| --- | --- |
| `references/REVIEW.md` | Standard code review behavior, evidence rules, and review output format. |
| `references/REVIEW_DEEP.md` | Extension for high-risk, security, architecture, performance, testing, or full-depth audits. |
| `references/COMMIT.md` | Commit recommendations, commit splitting, Conventional Commit messages, and explicit commit execution. |

If a required reference file is missing or unreadable, stop and report exactly which file is unavailable instead of approximating its behavior.

## Routing

Use the smallest useful reference set:

- Normal review, file review, folder review, diff review, branch review, PR review, or changed-files review: load `references/REVIEW.md`.
- Deep review, audit, security review, architecture review, performance review, testing review, `--full`, or high-risk changes: load `references/REVIEW.md` and `references/REVIEW_DEEP.md`.
- Commit title, commit body, Conventional Commit recommendation, commit split, or commit execution: load `references/COMMIT.md`.
- Review before commit: load `references/REVIEW.md` first, then `references/COMMIT.md` only after the review result is clear.
- Deep audit before commit: load `references/REVIEW.md` and `references/REVIEW_DEEP.md` first, then `references/COMMIT.md` only after the audit result is clear.

If the user asks only for commit help, inspect only enough context to describe the changes accurately. Do not perform a full code review unless the user asks for one or obvious risk requires calling it out.

## Scope Defaults

- If the user gives a path, review or inspect that path and the minimal related context needed to understand it.
- If the user asks for changed, staged, uncommitted, branch, commit, or PR work, use the relevant diff as the source of truth.
- If no scope is given for a review, treat the repository root as the scope at standard depth.
- If no scope is given for commit help, inspect staged changes first; if nothing is staged, inspect unstaged changes only as a recommendation source unless the user asks to commit them.
- Do not silently broaden the task. State any material scope limits in the final answer.

## Safety Rules

- Do not edit files unless the user explicitly asks for fixes.
- Do not stage, commit, amend, reset, rebase, push, tag, delete, rename, or run destructive commands unless the user explicitly asks.
- Do not invent test results, command output, changed files, validation, or commit rationale.
- Use concrete evidence from the diff, repository files, tests, configuration, documentation, command output, or user-provided context.
- If scope or evidence is insufficient, say exactly what is missing instead of guessing.
- Preserve unrelated user changes in the working tree.
- When commit execution is requested, follow `references/COMMIT.md` and the repository's git safety rules.

## Output Behavior

Follow the output format from the loaded reference file. Do not dump internal checklists.

- Use the review format from `references/REVIEW.md` for review tasks.
- Use the deep-review heuristics from `references/REVIEW_DEEP.md` only as an extension, not as a separate output template.
- Use the commit recommendation format from `references/COMMIT.md` for commit tasks.
- When both review and commit workflows apply, report review findings first, then provide the commit recommendation only after the review result is clear.
- If no strong review findings exist, say so plainly and include residual risks or checks not run.
- If only a commit title was requested and one commit is enough, return only the title unless the user asked for rationale.

## Good Invocations

```text
review .
review --changed
review src/auth --focus security
review main..feature --depth deep
review this PR
suggest a commit
split these changes into commits
review staged changes and suggest a commit
review changes and then commit
perform a deep audit before committing
```
