# Commit-Only Template Example

## Template Pack

```txt
templates/commit/
```

This example uses the commit-only template. The router can load `COMMIT.md`, but it does not include review instructions. Use this pack when you want commit naming, grouping, and safe commit execution guidance without a full review workflow.

## Example Code

```txt
examples/commit/reporting.py
```

The Python code represents a small staged change:

- It adds CSV-like sales report output.
- It calculates a total from row amounts.
- It contains a possible CSV escaping issue, but the user did not ask for a review.

## User Command

```txt
suggest commit
```

## Expected Routing

```txt
AGENTS.md -> COMMIT.md
```

The request asks for commit help only. The agent should inspect enough context to name the change accurately, but it should not present a full code review.

## Output

This output was recorded from an agent pass using `templates/commit/` against `reporting.py`.

````md
## Recommended commit

```txt
feat(reporting): add sales report builder
```

## Why this commit

- Intent: add a helper for generating sales report output with totals
- Scope: `reporting`
- Includes: new `agents/codebase-review-commit/examples/commit/reporting.py` file with `build_sales_report`

## Validation

- Tests not run: unknown
- Evidence used: staged addition of `agents/codebase-review-commit/examples/commit/reporting.py`
````

## Output Explanation

The commit template should recommend a clear Conventional Commit title and explain the evidence used. It should not turn the unescaped CSV-like output into a review finding because the user did not ask for a review.

If the user instead asked `review reporting.py`, this template should explain that review instructions are not included unless they exist elsewhere in the target repository.
