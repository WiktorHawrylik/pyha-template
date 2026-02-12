# License Compliance Guide

## For AI Coding Assistants and Contributors

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

## What This Means for AI Agents

When contributing code to this project, you MUST:

### 1. Ensure License Compatibility

- All generated code must be compatible with AGPL-3.0
- **Compatible licenses**: GPL-3.0, GPL-2.0+, LGPL, MIT, BSD, Apache 2.0
- **Incompatible licenses**: Proprietary, non-commercial licenses

### 2. Maintain License Headers

- Keep existing license headers in files
- Add appropriate headers to new files
- Template provided in [CONTRIBUTING.md](https://github.com/WiktorHawrylik/your-package-name/blob/main/CONTRIBUTING.md)

### 3. Respect Copyleft

- All derivative works must also be AGPL-3.0
- Source code must be made available
- Network use triggers copyleft (AGPL-specific)

### 4. Attribution

- Maintain copyright notices
- Attribute third-party code properly
- Document code sources in comments

## License Header Template

Add this to new Python files:

```python
"""Module description.

Copyright (C) YYYY Your Name

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
```

## AGPL-3.0 Key Points

### What You Can Do

✅ Use the code commercially
✅ Modify the code
✅ Distribute the code
✅ Use the code privately
✅ Grant patent rights

### What You Must Do

⚠️ Disclose source code
⚠️ License under AGPL-3.0
⚠️ State changes made
⚠️ Include original license
⚠️ Provide source for network use

### What You Cannot Do

❌ Hold liable
❌ Use without attribution
❌ Sublicense under different terms

## Special AGPL-3.0 Feature: Network Use

Unlike GPL, AGPL requires that if you run modified versions of this software as a web service or network service, you must make the source code available to users of that service.

**Example**: If you create a web API using this library and modify it, you must provide the modified source code to users who interact with your API.

## Compatible Licenses

You can incorporate code from these licenses:

- **GPL-3.0** - GNU General Public License v3.0
- **GPL-2.0+** - GNU General Public License v2.0 or later
- **LGPL** - GNU Lesser General Public License
- **MIT** - MIT License
- **BSD** - BSD Licenses (2-clause, 3-clause)
- **Apache-2.0** - Apache License 2.0
- **Public Domain** - CC0, Unlicense

## Incompatible Licenses

Do NOT incorporate code from:

- **Proprietary** - Commercial, closed-source code
- **CC BY-NC** - Creative Commons Non-Commercial
- **GPL-2.0-only** - GPL v2.0 only (without "or later")
- **Custom restrictive licenses**

## Checklist for AI Agents

Before generating or suggesting code:

- [ ] Is the code original or based on compatible open-source?
- [ ] If from external source, what is its license?
- [ ] Have I added proper attribution in comments?
- [ ] Have I included/maintained license headers?
- [ ] Is the resulting code compatible with AGPL-3.0?
- [ ] Have I documented any third-party code sources?

## When Using Third-Party Code

If incorporating code from other sources:

1. **Check the license** - Ensure it's AGPL-compatible
2. **Add attribution** - Comment with source and license
3. **Preserve notices** - Keep original copyright notices
4. **Document** - Note the source in commit messages

Example:

```python
# The following function is based on code from:
# Source: https://github.com/example/project
# License: MIT
# Copyright (c) 2024 Original Author

def borrowed_function():
    """Function borrowed from external source."""
    pass
```

## Questions?

- Read the full [CONTRIBUTING.md](https://github.com/WiktorHawrylik/your-package-name/blob/main/CONTRIBUTING.md) guide
- Check the [LICENSE](https://github.com/WiktorHawrylik/your-package-name/blob/main/LICENSE) file
- Review [AGPL-3.0 FAQ](https://www.gnu.org/licenses/gpl-faq.html)

## Summary

The AGPL-3.0 license ensures:

1. **Freedom** - Anyone can use, modify, and distribute
2. **Transparency** - Source code must be available
3. **Continuity** - Derivatives remain free and open
4. **Network protection** - Cloud/SaaS use requires source disclosure

When in doubt, err on the side of:

- More attribution
- More documentation
- More transparency
- Compatible licensing

---

**Remember**: License compliance is not just legal necessity—it's respect for the open-source community and the collaborative spirit of software development.
