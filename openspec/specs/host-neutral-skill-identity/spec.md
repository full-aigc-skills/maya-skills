# host-neutral-skill-identity Specification

## Purpose
TBD - created by archiving change host-neutral-skill-identities. Update Purpose after archive.
## Requirements
### Requirement: Maya skills use host-neutral plugin identities

Installable Maya skills SHALL refer to the current public identities `maya-design` and `dreamina-3d` and SHALL NOT expose a host-prefixed alias as the canonical identity.

#### Scenario: Validate a Maya inspection receipt

- **WHEN** a user follows the `maya-inspect` validation checklist
- **THEN** the expected `plugin_id` is `maya-design`

