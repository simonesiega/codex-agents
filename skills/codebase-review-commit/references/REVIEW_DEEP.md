# REVIEW_DEEP.md - Deep Review Extension

## Purpose
Use this file only as an extension to `REVIEW.md` for deep reviews, security audits, architecture audits, performance audits, testing audits, or other high-risk changes.
`REVIEW.md` remains the source of truth for scope, severity, output format, and fix-mode rules. This file adds deeper review heuristics. It should improve judgment, not output volume.

## When to use this file

Consult this file when the user asks for:

```txt
review . --depth deep
review <scope> --depth deep
review <scope> --focus security
review <scope> --focus architecture
review <scope> --focus performance
review <scope> --focus testing
review <scope> --full
audit <scope>
```

Also consult it when the reviewed change touches:

- authentication, authorization, sessions, or permissions
- payments, billing, financial logic, or regulated data
- database migrations, schema changes, or data retention behavior
- public APIs, SDKs, CLIs, exported packages, or compatibility-sensitive interfaces
- deployment, CI/CD, infrastructure, secrets, or environment configuration
- concurrency, queues, caches, jobs, workers, or distributed workflows
- large refactors or architectural boundaries

## Relationship with REVIEW.md

- Inherit scope discipline, severity, output format, and safety rules from `REVIEW.md`.
- Use this file to inspect more deeply, not more broadly.
- Do not restate this checklist in the final answer.
- Report only concrete findings, material residual risks, or relevant open questions.
- If this file conflicts with `REVIEW.md`, `REVIEW.md` wins.

## Evidence discipline

Classify concerns before reporting them:

- Confirmed issue: directly supported by code, config, tests, or documented behavior.
- Likely issue: strongly supported by code evidence but not fully executed.
- Residual risk: plausible concern that could not be verified within the allowed scope.

Report confirmed and likely issues as findings. Use `Open questions` when missing facts could change the result. Confidence should reflect evidence, not severity.

False positives are expensive. Do not turn a possibility into a finding without evidence and realistic impact.

## Deep review process

1. Map the boundary.
   - What is inside the requested scope?
   - What external systems, users, services, or modules interact with it?
   - Which paths are user-facing, security-sensitive, or production-critical?

2. Trace core flows.
   - Input and validation
   - Permissions and policy checks
   - State changes, persistence, and side effects
   - Output, logging, and externally visible behavior

3. Trace failure and recovery paths.
   - Invalid input
   - Missing data
   - Dependency failures
   - Timeouts, retries, and partial writes
   - Cleanup, rollback, and empty-state behavior

4. Compare implementation against contracts.
   - Public APIs, CLI behavior, UI behavior, type definitions, docs, tests, and established conventions

5. Check release and operational risk.
   - Backward compatibility
   - Required migrations, rollout ordering, or feature flags
   - Rollback safety
   - Production observability

6. Write only the strongest findings.
   - Prefer fewer stronger findings over checklist noise.

## Deep inspection areas

Check only the relevant sections. Skip the rest. The checklist is a risk map, not a required output list.

### Correctness and state

- behavior that does not match tests, docs, contracts, or user expectations
- invalid assumptions about nulls, optional fields, empty collections, or missing config
- incorrect state transitions, ordering, filtering, pagination, or deduplication
- race conditions, stale state, timezone or date bugs, or non-deterministic behavior
- partial failures, cleanup gaps, or hidden coupling

### Security, privacy, and abuse

- missing auth, authz, object-level checks, or privilege boundaries
- injection, XSS, SSRF, unsafe deserialization, path traversal, or unsafe file handling
- weak sessions, cookies, CSRF, CORS, replay, or idempotency protections
- secrets, PII, or sensitive internals exposed in logs, telemetry, bundles, URLs, fixtures, or generated files
- debug or admin behavior exposed in production, or missing abuse controls on sensitive flows

### Architecture and maintainability

- unclear boundaries, wrong-layer business logic, tight coupling, or circular dependencies
- duplicated domain logic or abstractions that hide critical behavior
- public interfaces leaking internals
- large refactors mixed with behavior changes
- complex code without proportional tests or documentation

### APIs, data, and background work

- missing validation or inconsistent response and error contracts
- missing transactions, integrity checks, idempotency, or message versioning
- unsafe queries, N+1 patterns, stale reads, cache bugs, or unsafe retries
- queues, jobs, or migrations that can leave inconsistent state
- breaking API or data changes without compatibility notes, versioning, or docs

### Frontend and user experience

- missing loading, empty, success, or error states
- broken validation, unclear user-facing text, or accessibility gaps
- hydration mismatches or fragile client-server boundaries
- stale state, double submission, destructive actions without confirmation, or optimistic updates without rollback
- sensitive data exposed to the browser unnecessarily

### Testing and validation

- critical flows without tests
- edge, regression, permission, or failure paths missing coverage
- brittle snapshots or mocks that hide real behavior
- tests coupled to implementation details instead of outcomes
- missing build, typecheck, integration, performance, or CI validation where the path is important

### Reliability, performance, and operations

- swallowed errors, silent fallbacks, or misleading error messages
- missing timeouts, backoff, cleanup, rollback, or resource release
- hot-path expensive work, unbounded loops, memory growth, or leaked handles
- missing logs, metrics, tracing, or failure visibility on critical paths
- unsafe or undocumented runtime config, deployment assumptions, generated artifacts, or CI/CD paths that can bypass validation

### Change, release, and dependencies

- breaking public contracts, defaults, or config in ways that alter production behavior
- rollout, migration, feature-flag, or rollback paths that appear incomplete or unsafe
- hidden impact on external consumers outside the reviewed scope
- unnecessary or risky dependencies, scripts, or third-party actions
- lockfile drift, version mismatches, or dependency churn mixed with unrelated changes

### Prompt and instruction files

When reviewing `AGENTS.md`, `REVIEW.md`, `REVIEW_DEEP.md`, `COMMIT.md`, prompts, or agent instructions, check for:

- unclear scope or invocation patterns
- conflicting rules or weak routing
- always-loaded files that are too long for their value
- vague advice without concrete behavior
- missing output format, severity, safety rules, or examples
- duplicated guidance or instructions that encourage repo-wide or speculative review

## Final review calibration

Before finalizing a deep review, check:

- Are the findings ordered by severity?
- Is each finding concrete, actionable, and tied to realistic impact?
- Are confirmed issues, open questions, and residual risks clearly separated?
- Are tests and validation reported honestly?
- Is the reviewed scope explicit, with unreviewed areas called out?
- Did the review use only the deep sections that were actually relevant?
- Did the review stay concise enough to be useful?
- Did the review avoid style-only noise and checklist dumping?
