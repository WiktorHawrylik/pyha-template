---
# Bug report template to standardize reports.
name: Bug report
description: Report a reproducible bug
labels: ["bug"]
body:
  - type: textarea
    attributes:
      label: What happened?
      description: Provide steps to reproduce.
    validations:
      required: true
  - type: textarea
    attributes:
      label: Expected behavior
      description: What did you expect to happen?
    validations:
      required: true
  - type: textarea
    attributes:
      label: Logs and screenshots
      description: Paste logs or screenshots if relevant.
