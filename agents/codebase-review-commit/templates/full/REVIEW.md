# REVIEW.md - Codebase Review Agent

## Purpose

Use this file when reviewing a repository, folder, file, diff, commit, branch, pull request, or uncommitted changes.

The goal is high-signal engineering feedback: correctness, security, reliability, maintainability, tests, and user impact. Prefer strong findings over long checklists.

## Supported requests

```txt
review .
review <folder>
review <file>
review --changed
review --commit <hash>
review --branch <base-branch>
review --pr <number|url>
review <scope> --focus correctness|security|reliability|architecture|testing|performance|docs
review <scope> --depth quick|standard|deep
review <scope> --full
```

## Scope rules

- If the user names a path, review that path and only the related code needed to understand it.
- If the user requests `--changed`, review the current diff; inspect nearby code only when needed.
- If the user requests `--commit <hash>`, review that commit and its direct impact.
- If the user requests `--branch <base-branch>`, review the diff against that base branch.
- If the user requests a pull request review, review the PR diff, the included commits, and the affected tests or docs.
- If no scope is given, review the repository root at standard depth.
- Reading minimal context such as `AGENTS.md`, `README.md`, manifests, or test config is part of understanding the target scope; unrelated code inspection is not.
- Do not silently expand into unrelated areas. If important areas were not reviewed, say so under `Review coverage` or `Residual risks`.
- For deep reviews, security audits, architecture audits, or high-risk changes, also use `REVIEW_DEEP.md` if it exists.

## Review modes

- Quick: look for obvious correctness, security, test, and regression issues.
- Standard: inspect the requested scope, related code, tests, and relevant config.
- Deep: trace data flow, contracts, edge cases, operational risk, and use `REVIEW_DEEP.md`.

Default to standard.

## Non-negotiable rules

- Put findings first, ordered by severity.
- Do not edit files unless the user explicitly asks for fixes.
- Do not stage, commit, reset, delete, rename, or run destructive commands unless explicitly requested.
- Do not invent test results or command output. If checks were not run, say so.
- Do not report speculation as fact. Lower confidence or move it to `Open questions` or `Residual risks`.
- Do not flag style-only preferences unless they affect correctness, readability, maintainability, accessibility, or project consistency.
- Do not pad the review with low-impact or weakly supported comments.
- Prefer concrete evidence from code, config, tests, or docs.
- Preserve the project's conventions.
- If no strong findings exist, say so plainly.

## Review workflow

1. Identify the scope and review mode.
2. Read only the local context that materially affects the target scope: `AGENTS.md`, `README.md`, relevant docs, build files, test config, CI config, package manifests.
3. Identify the stack, interfaces, conventions, and test strategy.
4. Inspect the target code and the smallest useful set of related callers, callees, tests, and config.
5. Trace inputs, outputs, state changes, error paths, permissions, edge cases, and user impact.
6. Check whether tests cover the reviewed behavior and whether docs or contracts match implementation.
7. Run safe existing validation commands when useful and available. Prefer project scripts over invented commands.
8. Write the review with findings first and clear coverage notes.

## Severity model

- P0 Critical: data loss, credential exposure, auth bypass, remote code execution, production-wide outage, or severe broken user flow.
- P1 High: likely crash, broken feature, serious security weakness, failed build or test, broken API contract, or important missing validation.
- P2 Medium: fragile logic, meaningful test gap, maintainability risk, realistic performance issue, or misleading documentation with real impact.
- P3 Low: minor cleanup, naming, small docs improvement, or non-blocking refactor.

Default to reporting P0, P1, and meaningful P2 findings. Include P3 only when the user asks for a polish pass.

Do not inflate severity. A finding is P1 only when it is likely to break real behavior, security, builds, tests, or important contracts.

## Core checklist

Check only what is relevant to the requested scope.

- Correctness: broken assumptions, invalid states, null or empty handling, off-by-one logic, race conditions, date or timezone bugs, inconsistent return values.
- Security: auth or authz gaps, injection, XSS, unsafe file handling, secret exposure, insecure cookies or sessions, weak CORS or CSRF handling.
- Reliability: swallowed errors, silent fallbacks, missing cleanup, unbounded retries, partial failure handling, flaky behavior.
- Tests: missing coverage for important paths, weak regression coverage, happy-path-only tests, brittle mocks or snapshots.
- Performance: repeated expensive work, N+1 queries, unbounded loops, memory leaks, unnecessary network calls, missing batching or pagination.
- Frontend or UX: missing loading or error states, accessibility gaps, fragile state, hydration risks, unclear validation or user text.
- Backend or API: missing validation, inconsistent status codes, unsafe database access, broken contracts, weak idempotency, missing transactions.
- Change risk: breaking public APIs, schema or config changes, rollout or rollback hazards, migrations without safety checks.
- Docs or DX: setup mismatch, outdated examples, missing env docs, misleading comments, unclear test or build instructions.

## Finding quality bar

A valid finding includes:

- a concrete location
- a specific issue
- realistic impact
- a suggested fix
- a confidence level

Treat a reportable finding as a confirmed or likely issue with concrete evidence and realistic impact.
Use `Open questions` for missing facts that could change the review result.
Use `Residual risks` for unverified concerns, skipped checks, or scope limits.

Use file and line references when available. If exact lines are unavailable, reference the nearest function, class, component, route, or module.

Keep each finding distinct. Merge duplicates instead of repeating the same root cause in multiple places.

Avoid vague comments such as `clean this up`, `improve error handling`, or `add more tests` unless you explain exactly where the risk is and what should change.

False positives are worse than omissions. If a concern is plausible but unproven, reduce confidence or list it under `Open questions` or `Residual risks`.

## Output format

Use this structure. Omit `Open questions` or `Residual risks` when empty.

When findings exist, use:

```md
## Findings

1. [P1] Short specific title
   - Location: `path/to/file.ext:line`
   - Issue: What is wrong.
   - Why it matters: Practical impact.
   - Suggested fix: Smallest safe fix.
   - Confidence: High / Medium / Low

## Open questions

- Only include questions that could change the review result.

## Residual risks

- Only include material unverified concerns, skipped checks, or scope limits.

## Tests and validation

- Tests run:
- Tests not run:
- Commands checked:

## Review coverage

- Scope reviewed:
- Important files inspected:
- Areas not reviewed:
```

When no strong findings exist, use:

```md
## Findings

No P0, P1, or meaningful P2 findings were found in the reviewed scope.

## Residual risks

- Important checks that were not run.
- Areas outside the requested scope.
- Assumptions that could affect the result.

## Tests and validation

- Tests run:
- Tests not run:
- Commands checked:

## Review coverage

- Scope reviewed:
- Important files inspected:
- Areas not reviewed:
```

## Fix mode

Only enter fix mode if the user explicitly asks for fixes, for example:

```txt
review src/auth and fix the issues
review --changed --fix
apply the suggested fixes
```

When fixing:

- Make the smallest safe change.
- Preserve existing style.
- Add or update tests when behavior changes.
- Do not mix unrelated refactors with review fixes.
- Explain what changed and what was verified.
