# Modular AGENTS.md Workflows for Review and Commits

A modular instruction package for Codex that separates code review, deep audits, and commit workflows into focused, copy-ready Markdown files.

## What this package is

This package is a small instruction bundle for Codex and compatible coding agents that support `AGENTS.md` files as persistent project guidance.

It provides:

- a small router in [`AGENTS.md`](AGENTS.md)
- a default review workflow in [`REVIEW.md`](REVIEW.md)
- a deeper audit extension in [`REVIEW_DEEP.md`](REVIEW_DEEP.md)
- a separate commit workflow in [`COMMIT.md`](COMMIT.md)

The root files are the canonical source files for maintenance and customization. The `templates/` folders are the three copy-ready packs for real project use.

## Why it exists
Many project instruction files become too broad: review rules, audit checklists, commit conventions, and Git safety all end up in one always-loaded file.

This package separates those concerns so agents can:

- load only the smallest useful instruction set
- keep default context small
- use deep review only when the request is high-risk
- keep commit naming and commit execution separate from code review

## Best for

- Repositories that want reusable Codex review instructions.
- Teams that want review and commit workflows separated.
- Projects that want copy-ready `AGENTS.md` template packs.

## Core files

| File | Role | Use when | Do not use for |
|---|---|---|---|
| `AGENTS.md` | Root router | The project wants one entry point that selects the right workflow | Detailed review or commit behavior by itself |
| `REVIEW.md` | Default review workflow | Reviewing a repo, folder, file, diff, branch, commit, PR, or uncommitted changes | Deep audit logic by itself |
| `REVIEW_DEEP.md` | Deep review extension | Security reviews, architecture reviews, audits, performance/testing audits, or other high-risk changes | Normal review on its own |
| `COMMIT.md` | Commit workflow | Commit messages, Conventional Commits, commit grouping, and safe commit execution | Full code review |

## Quick start

### 1. Choose a pack

- Full pack: `templates/full/`
- Review-only pack: `templates/review/`
- Commit-only pack: `templates/commit/`

### 2. Copy it into the target repository

Copy exactly one pack into the root of the target repository so Codex can read its `AGENTS.md` entry point. Platform-specific commands are in [`docs/usage.md`](docs/usage.md).

### 3. Ask for a workflow

Then ask the agent for the workflow you want, for example:

```txt
review src/auth
review --changed
review src/payments --full
suggest commit
split these changes into commits
review changes and then suggest commit
```

## Usage examples

| User request | Files loaded |
|---|---|
| `review .` | `AGENTS.md` to `REVIEW.md` |
| `review --changed` | `AGENTS.md` to `REVIEW.md` |
| `review src/auth --depth deep` | `AGENTS.md` to `REVIEW.md` and `REVIEW_DEEP.md` |
| `review src/payments --full` | `AGENTS.md` to `REVIEW.md` and `REVIEW_DEEP.md` |
| `suggest commit` | `AGENTS.md` to `COMMIT.md` |
| `commit --staged` | `AGENTS.md` to `COMMIT.md` |
| `split these changes into commits` | `AGENTS.md` to `COMMIT.md` |
| `review changes and then commit` | `AGENTS.md` to `REVIEW.md`, then `COMMIT.md` |
| `deep audit before commit` | `AGENTS.md` to `REVIEW.md` and `REVIEW_DEEP.md`, then `COMMIT.md` |

More detailed workflow examples live in [`docs/usage.md`](docs/usage.md).

## Examples

Recorded examples are available for each template pack:

- [`examples/full/EXAMPLE.md`](examples/full/EXAMPLE.md)
- [`examples/review/EXAMPLE.md`](examples/review/EXAMPLE.md)
- [`examples/commit/EXAMPLE.md`](examples/commit/EXAMPLE.md)

## Template packs

The `templates/` directory exists so users can copy only the workflow they need.

| Template pack | Files | Use when |
|---|---|---|
| `templates/commit/` | `AGENTS.md`, `COMMIT.md` | The project wants only commit naming, commit grouping, and safe commit execution rules |
| `templates/review/` | `AGENTS.md`, `REVIEW.md`, `REVIEW_DEEP.md` | The project wants only review and deep-audit workflows |
| `templates/full/` | `AGENTS.md`, `REVIEW.md`, `REVIEW_DEEP.md`, `COMMIT.md` | The project wants the full copy-ready package |

The template routers are specialized for their own folders. They mention only the workflows included in that pack, plus a short note when a request falls outside the template.

## Recommended copy strategy

- If you want both review and commit workflows, copy `templates/full/`.
- If you want only review workflows, copy `templates/review/`.
- If you want only commit workflows, copy `templates/commit/`.
- Keep one `AGENTS.md` router at the repository root.
- Treat the root files as canonical. Use them to personalize or maintain the package, then keep the matching template files aligned.

## When to use each workflow

| Need | Recommended files |
|---|---|
| Standard code review | `REVIEW.md` |
| Deep audit or high-risk review | `REVIEW.md` + `REVIEW_DEEP.md` |
| Commit message suggestion | `COMMIT.md` |
| Commit split or grouping | `COMMIT.md` |
| Review before commit | `REVIEW.md` then `COMMIT.md` |
| Deep audit before commit | `REVIEW.md` + `REVIEW_DEEP.md` then `COMMIT.md` |

## Shared package guidance

Common guidance for package structure, template maintenance, and safety standards is in [`docs/agent-workflow-packages.md`](../../docs/agent-workflow-packages.md).

## Folder structure

```txt
.
├── AGENTS.md                   # router that selects the right workflow file
├── COMMIT.md                   # commit message, grouping, and safe commit workflow
├── README.md                   # package overview and quick-start guide
├── REVIEW.md                   # default code review workflow
├── REVIEW_DEEP.md              # deep audit extension for high-risk reviews
├── docs/                       # documentation specific to this workflow package
│   └── usage.md                # detailed usage and copy instructions
├── examples/                   # recorded examples for each template pack
│   ├── README.md               # examples index
│   ├── commit/                 # commit-only example
│   │   ├── EXAMPLE.md          # recorded commit workflow output
│   │   └── reporting.py        # sample file used by the example
│   ├── full/                   # review plus commit example
│   │   ├── EXAMPLE.md          # recorded full workflow output
│   │   └── password_reset.py   # sample file used by the example
│   └── review/                 # review-only example
│       ├── EXAMPLE.md          # recorded review workflow output
│       └── user_service.py     # sample file used by the example
└── templates/                  # copy-ready packs for target repositories
    ├── commit/                 # commit-only pack
    │   ├── AGENTS.md           # commit-only router
    │   └── COMMIT.md           # commit workflow file
    ├── full/                   # review plus commit pack
    │   ├── AGENTS.md           # full router
    │   ├── COMMIT.md           # commit workflow file
    │   ├── REVIEW.md           # default review workflow
    │   └── REVIEW_DEEP.md      # deep audit extension
    └── review/                 # review-only pack
        ├── AGENTS.md           # review-only router
        ├── REVIEW.md           # default review workflow
        └── REVIEW_DEEP.md      # deep audit extension
```

## Documentation

- [`docs/usage.md`](docs/usage.md) - how to use the full package and the template packs in real repositories
- [`docs/agent-workflow-packages.md`](../../docs/agent-workflow-packages.md) - shared guidance for package structure, templates, safety, and maintenance
