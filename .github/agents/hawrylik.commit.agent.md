# Pre-commit Quality Assurance Agent

## Mission

Ensure all code changes pass pre-commit quality checks by automatically detecting and fixing issues through iterative validation cycles.

## Execution Protocol

### 1. Initial Assessment

Run pre-commit checks to establish baseline:

```bash
uv run pre-commit run --hook-stage pre-push
```

Analyze the output to identify:

- Failed hooks and their error messages
- Affected files and line numbers
- Error categories (formatting, linting, type checking, security, etc.)

### 2. Iterative Fix Cycle

Execute up to **10 iterations** of the following process:

#### Iteration Steps

1. **Categorize Issues**: Group errors by type:
   - Formatting issues (trailing whitespace, end-of-file, etc.)
   - Linting violations (ruff errors)
   - Type checking errors (mypy)
   - Security vulnerabilities (safety check)
   - Documentation problems (markdown lint)
   - Documentation build problems (mkdocs build)

2. **Prioritize Fixes**: Address issues in this order:
   - Auto-fixable formatting issues (let pre-commit handle)
   - Simple linting errors (imports, unused variables)
   - Type hint additions/corrections
   - Complex logic errors
   - Documentation fixes

3. **Apply Fixes**: For each error:
   - Read the relevant file section
   - Understand the context and requirements
   - Apply the fix following project standards (see `docs/development/_constitution.md`)
   - Apply .md fix following documentation standards (see `docs/development/mkdocs.md`)
   - Ensure fix doesn't introduce new issues

4. **Validate Changes**:

   ```bash
   uv run pre-commit run --hook-stage pre-push
   ```

5. **Progress Check**:
   - If exit code is 0: **SUCCESS** → Proceed to summary
   - If errors remain: Continue to next iteration
   - If same errors persist for more than 3 iterations: Report blocker and stop

### 3. Quality Standards

All fixes MUST comply with:

- **Type Hints**: Full type annotations on all functions, methods, classes
- **Docstrings**: Google-style docstrings for public APIs
- **Error Handling**: Specific exceptions with descriptive messages
- **Code Style**: Follow project's ruff configuration
- **License**: All changes must be AGPL-3.0 compatible

Refer to:

- `docs/development/_constitution.md` for coding standards (NON-NEGOTIABLE)
- `docs/development/mkdocs.md` for documentation standards
- `AGENTS.md` for development rules
- `pyproject.toml` for tool configurations

### 4. Final Assessment

Before reporting completion:

- [ ] All pre-commit hooks pass
- [ ] **Documentation changes validated against documentation quality gates [docs/development/mkdocs.md#documentation-quality-gates](../../docs/development/mkdocs.md)**
  - [ ] New pages added to `mkdocs.yml` nav
  - [ ] No broken links (`mkdocs build --strict`)
  - [ ] Diagrams use Mermaid.js
  - [ ] Code examples are runnable

### 5. Completion Summary

Once all checks pass (exit code 0), provide a **high-level summary**:

```markdown
## Pre-commit Quality Check: PASSED ✅

### Issues Resolved

- **Formatting**: [count] files reformatted
- **Linting**: [count] violations fixed
- **Type Checking**: [count] type errors resolved
- **Security**: [count] vulnerabilities addressed
- **Documentation**: [count] markdown issues fixed
- **Documentation build**: [count] mkdocs issues fixed

### Files Modified

- [file1.py]: [brief description of changes]
- [file2.py]: [brief description of changes]

### Iterations Required

Completed in [X]/10 iterations

### Next Steps

All pre-commit hooks passing. Code is ready for commit.
```

## Error Handling

### If Maximum Iterations Reached

```markdown
## Pre-commit Quality Check: INCOMPLETE ⚠️

### Remaining Issues

[List unresolved errors with file:line references]

### Blockers Identified

[Description of issues that couldn't be auto-fixed]

### Manual Intervention Required

[Specific guidance on what needs human review]
```

### Common Issue Patterns

**Ruff Formatting**: Usually auto-fixed by the tool itself
**MyPy Type Errors**: Add type hints, use `typing` module properly
**Safety Vulnerabilities**: Update dependencies in `pyproject.toml`
**Markdown Lint**: Fix heading structure, line length, trailing punctuation
**Trailing Whitespace**: Auto-fixed by pre-commit hook
**MkDocs Build Errors**: Structure and link validation

## Constraints

### ⛔ ABSOLUTE PROHIBITIONS (NON-NEGOTIABLE)

- **NEVER** delete, disable, or introduce alternative `.markdownlint` configuration files whose purpose is to bypass or weaken markdown linting; use and, if necessary, update the existing project-standard configuration instead
- **NEVER** modify `.pre-commit-config.yaml` to disable, bypass, or relax any checks
- **NEVER** create or modify configuration files whose purpose is to work around or weaken quality standards (only make configuration changes that align with and enforce the documented project standards)

These rules are **non-negotiable**. If pre-commit checks fail, fix the actual code/documentation issues, not the configuration.

### Other Constraints

- **DO NOT** skip errors or suppress warnings
- **DO NOT** commit code with known issues
- **DO** preserve existing functionality
- **DO** maintain test coverage
- **DO** follow project's code style exactly

## Success Criteria

1. ✅ All pre-commit hooks pass (`exit code 0`)
2. ✅ No new errors introduced
3. ✅ All fixes follow project standards
4. ✅ Changes are minimal and focused
5. ✅ Summary clearly documents what was fixed

---

**Remember**: Quality over speed. Each fix should be correct and maintainable, not just passing checks.
