<p align="center">
  <img src="assets/logos/codex-agents-logo-name.svg" alt="codex-agents logo" width="400" />
</p>

<p align="center">
  <strong>Drop-in <code>AGENTS.md</code> workflow packages and <code>SKILL.md</code> exports for Codex.</strong>
</p>

<p align="center">
  <a href="https://github.com/simonesiega/codex-agents/stargazers"><img src="https://img.shields.io/github/stars/simonesiega/codex-agents?style=social" alt="GitHub stars" /></a>
  <a href="https://github.com/simonesiega/codex-agents/issues"><img src="https://img.shields.io/github/issues/simonesiega/codex-agents" alt="Open issues" /></a>
  <a href="https://github.com/simonesiega/codex-agents/pulls"><img src="https://img.shields.io/github/issues-pr/simonesiega/codex-agents" alt="Open pull requests" /></a>
  <a href="https://github.com/simonesiega/codex-agents/commits/main"><img src="https://img.shields.io/github/last-commit/simonesiega/codex-agents" alt="Last commit" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/simonesiega/codex-agents" alt="License" /></a>
</p>

<p align="center">
  <img src="assets/how-it-works.png" alt="How codex-agents works" width="800" />
</p>


## Overview

`codex-agents` provides reusable `AGENTS.md` workflow packages and portable `SKILL.md` workflows for Codex.

The repository is built around a simple idea: Codex works better when instructions are focused, scoped, and easy to route. Instead of putting every rule into one large always-loaded file, each workflow gives Codex a clear entry point and a set of task-specific instruction files.

Use `agents/` when you want copy-ready `AGENTS.md` packages that can be dropped into a real repository. Use `skills/` when you want portable Codex skill versions of selected workflows.

The goal is to make Codex workflows easier to reuse, easier to maintain, and more predictable across real software projects.

## Why use this repo

Most Codex setups start with one simple `AGENTS.md` file. Over time, that file can become a long mix of review rules, commit rules, audit instructions, documentation preferences, safety constraints, project conventions, and one-off notes.

That makes the workflow harder to control: Codex receives more context than it needs, task boundaries become less precise, and small edits can affect unrelated behavior.

`codex-agents` gives you a cleaner starting point for building structured Codex workflows.

It helps you use Codex with:

- **fewer tokens** spent on unrelated instructions
- **copy-ready workflow packages** for real repositories
- **portable skill workflows** for reusable task-specific behavior
- clearer separation between review, audit, commit, and documentation tasks
- more predictable outputs for each engineering workflow
- safer defaults for validation, Git operations, and scope boundaries
- easier maintenance through small, focused instruction files

## Available packages

### Agent workflow packages

Copy-ready `AGENTS.md` packages that can be dropped into real repositories.

| Package | Use it when you need | Templates | Start here |
|---|---|---|---|
| [`codebase-review-commit`](agents/codebase-review-commit/) | Code review, deep audits, commit messages, and commit splitting | `full`, `review`, `commit` | [`README`](agents/codebase-review-commit/README.md) · [`Usage`](agents/codebase-review-commit/docs/usage.md) |

### Codex skills

Reusable `SKILL.md` workflows for task-specific Codex behavior.

| Skill | Use it when you need | References | Start here |
|---|---|---|---|
| [`codebase-review-commit`](skills/codebase-review-commit/) | Review, audit, and commit guidance as a Codex skill | `REVIEW.md`, `REVIEW_DEEP.md`, `COMMIT.md` | [`SKILL.md`](skills/codebase-review-commit/SKILL.md) |

## Quick start

Choose the format that fits your workflow.

### Use an agent package

Copy an `AGENTS.md` template pack into your target repository:

```bash
cp agents/<package-name>/templates/<template-name>/* /path/to/project/
```

Then open Codex inside the target repository and ask for the workflow you need.

Each package defines its own templates, supported prompts, and focused instruction files. For package-specific details, read the package `README.md` and usage guide.

### Use a Codex skill

Copy the skill folder into the skills directory used by your Codex setup:

```bash
cp -r skills/<skill-name> /path/to/codex/skills/
```

Then use Codex with a request that matches the skill, such as a review, audit, or commit workflow.

## Usage example

To use the `codebase-review-commit` agent package, copy the full template into your project:

```bash
cp agents/codebase-review-commit/templates/full/* /path/to/project/
```

Then ask Codex for the workflow you need:

```txt
review --changed
suggest commit
split these changes into commits
deep audit before commit
```

Codex will start from the copied `AGENTS.md` router and load the focused workflow files only when they are relevant.

If you prefer the skill version, copy the skill package into the skills directory used by your Codex setup:

```bash
cp -r skills/codebase-review-commit /path/to/codex/skills/
```

The skill keeps the same review, audit, and commit logic in a compact `SKILL.md` package backed by focused references.

For Windows PowerShell and package-specific commands, see the codebase-review-commit [usage guide](agents/codebase-review-commit/docs/usage.md).

## Repository structure

The repository is organized around reusable agent packages, Codex skills, shared documentation, and visual assets.

```txt
.
├── agents/               # copy-ready AGENTS.md workflow packages
├── skills/               # SKILL.md versions of selected workflows
├── assets/               # README images and logos
└── docs/                 # shared package-authoring documentation
```

## Package structure

Agent packages are self-contained and include documentation, examples, and copy-ready templates.

```txt
package-name/
├── README.md             # package overview
├── docs/                 # package-specific usage docs
├── examples/             # example prompts and expected behavior
└── templates/            # copy-ready instruction packs
```

Templates contain the files that can be copied into a target repository:

```txt
AGENTS.md                 # small router and package entry point
REVIEW.md                 # standard review behavior
REVIEW_DEEP.md            # deeper audit behavior
COMMIT.md                 # commit message and commit-splitting behavior
```

Skill packages keep the runtime entry point and focused reference files, while examples and extended documentation stay in the related agent package.

```txt
skill-name/
├── SKILL.md              # skill entry point
└── references/           # focused supporting instruction files
```

This structure keeps agent packages easy to copy and understand, while keeping skills compact and focused for reusable Codex workflows.

## Shared documentation

The `docs` directory contains repository-wide guidance for creating, maintaining, and extending workflow packages and their related skill exports.

| Document | Purpose |
|---|---|
| [`agent-workflow-packages`](docs/agent-workflow-packages.md) | Defines the structure, files, templates, and maintenance rules for `agents/` workflow packages |
| [`authoring-guidelines`](docs/authoring-guidelines.md) | Explains how to write focused Codex instruction files |
| [`template-maintenance`](docs/template-maintenance.md) | Explains how to keep canonical files and copy-ready templates aligned |
| [`safety-principles`](docs/safety-principles.md) | Defines the safety baseline used across all packages |
| [`examples-guidelines`](docs/examples-guidelines.md) | Explains how to write realistic and useful package examples |

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE).
