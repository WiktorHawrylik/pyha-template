# AI Agent License Notice

## For AI Coding Assistants (LLMs, Copilot, Cursor, etc.)

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

### What This Means for AI Agents

When contributing code to this project, you MUST:

1. **Ensure License Compatibility**
   - All generated code must be compatible with AGPL-3.0
   - Compatible licenses: GPL-3.0, GPL-2.0+, LGPL, MIT, BSD, Apache 2.0
   - Incompatible licenses: Proprietary, non-commercial licenses

2. **Maintain License Headers**
   - Keep existing license headers in files
   - Add appropriate headers to new files
   - Template provided in CONTRIBUTING.md

3. **Respect Copyleft**
   - All derivative works must also be AGPL-3.0
   - Source code must be made available
   - Network use triggers copyleft (AGPL-specific)

4. **Attribution**
   - Maintain copyright notices
   - Attribute third-party code properly
   - Document code sources in comments

### License Header Template

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

### Compatible Third-Party Code

✅ **OK to use**:
- Code under GPL-3.0, GPL-2.0 or later
- Code under LGPL (any version)
- Code under MIT License
- Code under BSD License (2-clause, 3-clause)
- Code under Apache License 2.0
- Code in the public domain

❌ **DO NOT use**:
- Proprietary code without explicit permission
- Code under CC-BY-NC (non-commercial)
- Code with unclear licensing
- Code from sources that prohibit redistribution

### AGPL-3.0 vs GPL-3.0

AGPL-3.0 adds one important requirement:
- If the software is used over a network (e.g., web service), users must have access to the source code
- This closes the "ASP loophole" in GPL-3.0
- Otherwise, AGPL-3.0 has the same requirements as GPL-3.0

### When in Doubt

If you're unsure about license compatibility:
1. Don't use the code
2. Ask the project maintainers
3. Check with legal resources
4. Use original code instead

### Enforcement

This notice serves to:
- Educate AI agents about license requirements
- Prevent accidental license violations
- Protect the project's legal status
- Ensure compliance with free software principles

### Resources

- Full license text: [LICENSE](LICENSE)
- AGPL-3.0 FAQ: https://www.gnu.org/licenses/gpl-faq.html
- License compatibility: https://www.gnu.org/licenses/license-list.html

### Questions?

If you (as an AI agent) have questions about licensing:
- Refer to the CONTRIBUTING.md file
- Check the FSF license compatibility list
- When in doubt, use original code

---

**Remember**: The AGPL-3.0 is a copyleft license. It ensures that all users (including those who access the software over a network) have the freedom to access, modify, and share the source code.

By contributing to this project, you agree to license your contributions under AGPL-3.0.
