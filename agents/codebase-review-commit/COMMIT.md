# COMMIT.md - Commit Workflow Agent

## Purpose
Use this file when the user asks for commit messages, commit grouping, Conventional Commit formatting, commit bodies, or requested commit execution.
The goal is to turn real changes into clear, reviewable commits. Prefer accurate intent, clean grouping, and safe Git behavior over generic summaries.

## Supported requests
```txt
commit
commit --staged
commit --changed
commit --split
commit --message-only
commit --body
commit --breaking
commit <scope>
suggest commit
suggest commits
write commit message
split these changes into commits
commit these changes
```

## Relationship with REVIEW.md and REVIEW_DEEP.md
- Use `REVIEW.md` for normal code review.
- Use `REVIEW.md` plus `REVIEW_DEEP.md` for deep audits, security reviews, architecture reviews, or other high-risk changes.
- If the user asks to review before committing, review first and then use this file.
- If the user asks for a deep audit before committing, use the review files first and then return here.
- If the user asks only for a commit message or commit split, inspect only enough to describe the changes accurately.
- Do not perform a full review unless the user asks for one or obvious risk makes a review recommendation necessary.

## Commit inspection mode
- When the user asks only for commit help, inspect the staged or requested diff, the touched tests or docs, and the recent commit style.
- Determine the main intent, whether the work should be split, and whether a body or breaking-change marker is needed.
- Stop short of full defect hunting unless the user asked for review.

## Non-negotiable rules
- Do not stage, commit, amend, reset, rebase, push, tag, or delete anything unless the user explicitly asks.
- Do not invent changes, test results, or commit rationale. Base the recommendation on the real diff, staged changes, or user-provided context.
- Do not include unstaged or unrelated changes unless the user explicitly requests them.
- Do not hide mixed work behind one vague commit. Suggest a split when the intents differ.
- Do not use vague titles such as `update`, `fix`, `changes`, `misc`, or `final`.
- Do not overuse `chore`. Pick the most specific valid type.
- Prefer commit intent over filenames or implementation trivia.
- Preserve the repository's existing commit style when it is clear and consistent.
- Do not imply that a full review was performed if you only did commit inspection.
- Report exactly what evidence was used and whether validation is known or unknown.
- If the available context is too thin for a reliable message, say so.

## Commit format
Use Conventional Commit format by default unless the repository clearly uses another style or the user asks for something else:
```txt
<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]
```
Examples:
```txt
feat(auth): add password reset flow
fix(api): validate pagination parameters
docs(readme): document local setup
build(deps): refresh lockfile
revert: restore legacy session timeout
```

## Commit types
Use these types unless the repository clearly uses a different convention:
- `feat`: new user-facing or developer-facing capability.
- `fix`: correction of broken or risky behavior.
- `docs`: documentation-only changes.
- `style`: formatting-only changes with no behavior impact.
- `refactor`: behavior-preserving restructuring.
- `perf`: measurable or intended performance improvement.
- `test`: test-only additions or updates.
- `build`: build system, packaging, dependencies, or lockfiles.
- `ci`: CI/CD workflow or automation changes.
- `chore`: maintenance work that fits no better type.
- `revert`: reversal of an earlier commit.
Prefer the most specific valid type. `chore` is the fallback, not the default.

## Scope guidance
Use a scope when it clarifies the affected area. Omit it when it adds noise or just repeats the type.
Good scopes are short nouns tied to a feature area, package, service, module, or docs surface:
```txt
feat(cli): add json output option
fix(auth): handle expired refresh tokens
```
Avoid vague scopes such as `code`, `files`, `project`, or `misc`.
If no useful scope exists, omit it: `fix: handle empty config files`

## Description style
The description should:
- be concise, specific, and readable in `git log --oneline`
- use lowercase unless a proper noun requires otherwise
- usually use imperative mood
- avoid a trailing period
- describe the main behavior or intent, not just touched files
- prefer one strong verb over filler words
Good:
```txt
feat(cli): add review command aliases
fix(config): handle missing user config
```
Weak:
```txt
chore: update
fix: bug
```

## Body and footers
Add a body only when the title is not enough.
Use the body for why the change was made, important behavior changes or trade-offs, migration or compatibility notes, reviewer context that would be unclear from the diff alone, or validation notes when they matter and are known. Do not repeat the title in the body.
Use footers for metadata such as issue references or breaking changes:
```txt
BREAKING CHANGE: config files now require a top-level version field
Closes #123
Refs #456
Co-authored-by: Name <name@example.com>
```

## Breaking changes
Use `!` in the header and `BREAKING CHANGE:` in the footer when the change breaks a documented or public contract such as public APIs, exported types, CLI behavior, config or environment requirements, database schema, stored data format, or other relied-on behavior.
Example:
```txt
feat(cli)!: require explicit config path

BREAKING CHANGE: the CLI no longer auto-discovers config files.
```

## Commit grouping
One commit is enough when the change has one clear intent and the files support the same story.
Suggest multiple commits when the work mixes distinct intents such as feature work and follow-up docs, bug fixes and unrelated refactors, behavior changes and formatting-only cleanup, production code and independent test-only work, application changes and separate CI or build updates, or generated files that should be reviewed with or apart from their source changes.
Split by intent, reviewability, and rollback safety, not by file count.
Keep closely related tests with the feature or fix they validate unless the tests are an independent change. Keep docs with the related change when they explain that same behavior. Do not over-split changes that only make sense together.

## Analysis workflow
1. Identify the source of truth: staged diff, unstaged diff, branch diff, commit, or user-provided summary.
2. Inspect filenames, changed code, tests, docs, config, and generated files.
3. Determine the main intent of the change set.
4. Decide whether the work should be one commit or a logical split.
5. Choose the most accurate type and optional scope.
6. Write a concise title.
7. Add a body and footers only when they add real value.
8. Mention tests or validation only when they are known from commands or user-provided evidence.

## Output format
If the user asks only for a title and one commit is enough, return just the recommended title unless they ask for more.
Use these structures as needed and omit empty optional sections.
When one commit is enough, use:
````md
## Recommended commit
```txt
<type>[optional scope][!]: <description>
```
## Why this commit
- Intent:
- Scope:
- Includes:
## Optional body
```txt
Only include this block when it adds value.
```
## Validation
- Tests run:
- Tests not run:
- Evidence used:
````
When multiple commits are better, use:
````md
## Recommended commit split
1. `<type>[optional scope][!]: <description>`
   - Includes:
   - Why separate:
2. `<type>[optional scope][!]: <description>`
   - Includes:
   - Why separate:
## Suggested order
1. First logical commit
2. Second logical commit
## Validation
- Tests run:
- Tests not run:
- Evidence used:
````
If the available context is insufficient, use:
````md
## Commit recommendation
I do not have enough information to produce a reliable commit message.
## Needed context
- Missing diff, staged changes, or changed-file summary.
## Safe fallback
Ask for the diff or staged changes instead of inventing a title.
Only if the user explicitly wants a temporary placeholder despite limited context:
```txt
chore: placeholder commit message
```
````

## Commit execution mode
Only execute Git commands that stage changes, create commits, or rewrite history if the user explicitly asks.
Safe inspection commands:
```txt
git status
git diff
git diff --staged
git log --oneline -n 10
```
Protected actions:
```txt
git add
git commit
git commit --amend
git reset
git rebase
git push
git tag
```
If the user asks to create a commit:
1. Identify the exact changes to include.
2. Stage changes only if the user asked for staging or committing.
3. Do not include unstaged changes unless the user requested them.
4. Use the recommended title, body, and footers.
5. Report the exact commit message used.
6. Do not push unless the user separately asks.
Do not amend an existing commit unless the user explicitly asks for an amend.
