# Agent Workflow Packages

## Purpose

Agent workflow packages are reusable instruction bundles for Codex. They define structured, copy-ready workflows that can be copied into real software repositories.

An agent package covers one coherent workflow family, such as code review, commit preparation, documentation, release support, testing, backend work, frontend work, or orchestration.

## Core idea

An agent package avoids one large always-loaded instruction file. Instead, it uses a small `AGENTS.md` router and a set of focused task files. The router selects the files relevant to the user's request. Each task file owns the detailed behavior for one workflow.

This keeps Codex behavior easier to route, easier to maintain, and more predictable across repositories.

## Standard package structure

Agent packages use this standard structure:

```txt
agents/<package>/
├── README.md       # package overview, value, quick start, and template choices
├── AGENTS.md       # small router that selects the right task files
├── TASK_FILE.md    # focused workflow instructions
├── docs/           # package-specific usage documentation
├── examples/       # realistic examples and sample files
└── templates/      # copy-ready packs for target repositories
```

Packages can include multiple task files when the workflow needs them:

```txt
REVIEW.md           # standard review workflow
REVIEW_DEEP.md      # deep-review extension
COMMIT.md           # commit recommendation and execution workflow
RELEASE.md          # release preparation workflow
DOCS.md             # documentation workflow
```

Each task file owns one job. Related workflows can live in the same package, but unrelated behavior stays in separate files or separate packages.

Packages can omit `templates/`, `examples/`, or package-local `docs/` only when the package is intentionally small and does not need them.

## Package qualities

Agent packages are:

- **copy-ready**: templates can be copied into a target repository without hidden context
- **scoped**: the workflow family and boundaries are clear
- **routable**: `AGENTS.md` makes the correct task file easy to select
- **safe**: destructive actions require explicit user intent
- **maintainable**: canonical files, templates, examples, and docs stay aligned
- **concrete**: instructions describe observable behavior instead of vague preferences

## Router files

`AGENTS.md` is the package entry point. It routes requests to the smallest useful instruction set.

A router defines:

- available task files
- when each task file applies
- when multiple task files apply together
- when optional extensions stay unloaded
- typical request-to-file mappings

A router does not duplicate the full workflow from task files.

Good routing examples:

```txt
review --changed                 -> REVIEW.md
review src/auth --depth deep     -> REVIEW.md + REVIEW_DEEP.md
suggest commit                   -> COMMIT.md
review changes and then commit   -> REVIEW.md + COMMIT.md
```

Weak routing example:

```txt
Use the best review strategy and make a good commit.
```

## Task files

Task files contain the detailed behavior for one workflow.

A task file defines:

- purpose
- supported requests
- scope rules
- workflow steps
- safety rules
- validation expectations
- output format
- fix or execution mode, when relevant

Task files use concrete operational instructions.

Prefer:

```txt
Report findings with location, issue, impact, suggested fix, and confidence.
```

Avoid:

```txt
Give high-quality feedback.
```

## Package README

Each package `README.md` explains one package.

It covers:

- what the package is for
- who the package is for
- which files are included
- which templates are available
- how to choose a template
- how to copy the package into a target repository
- where package-specific docs and examples live

The root README explains the repository. Package READMEs explain individual packages.

## Package-specific docs

Use `agents/<package>/docs/` for documentation that belongs to one package.

Good package-specific docs include:

- package-specific copy commands
- template selection guidance
- supported request examples
- package-specific routing behavior
- package-specific troubleshooting notes

Shared authoring rules, safety principles, template-maintenance rules, and example standards belong in the root `docs/` folder.

## Examples

Use `examples/` to show package behavior in practice.

Examples include realistic inputs, representative or recorded outputs, and any sample files needed to understand the workflow.

Each example identifies:

- the template or workflow demonstrated
- the user request
- the files the router loads
- the expected output shape
- why the output matches the package rules

Examples stay specific to the package they demonstrate.

## Templates

Use `templates/` for instruction packs users can copy directly into target repositories.

A template includes only the files required for its purpose.

Common template types include:

- `full`: complete workflow package
- `review`: review-only package
- `commit`: commit-only package
- task-specific packs for narrow workflows

Template routers can differ from the canonical package router when the template exposes fewer workflows.

A specialized router should:

- mentions only files included in the template
- avoids routing to missing files
- states when a requested workflow is not included
- keeps differences from the canonical router small and intentional

## Naming conventions

Package names identify the workflow family.

Good names:

```txt
codebase-review-commit
docs-maintenance
release-prep
frontend-review
backend-api-review
```

Weak names:

```txt
helper
agent
workflow
misc
general
```

Package names are lowercase and hyphen-separated.

## Maintenance checklist

Before finishing package changes, check:

- package-root canonical files describe the intended behavior
- `AGENTS.md` routes only to files that exist
- task files stay focused on their own workflow
- template copies are aligned where intended
- specialized templates omit unsupported workflows intentionally
- package-local docs contain package-specific guidance
- examples match the documented workflow
- links point to existing files
- safety rules are not weakened or duplicated inconsistently

## Review checklist for new packages

Before adding a new package, verify that:

- the package has a clear workflow family
- the package name is specific and readable
- the router is small and operational
- task files define concrete behavior and output formats
- templates can be copied without hidden dependencies
- examples demonstrate realistic usage
- package docs do not duplicate root docs
- safety boundaries are explicit
- the package adds meaningful value beyond generic instructions
