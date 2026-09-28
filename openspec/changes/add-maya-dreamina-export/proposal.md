## Why

The Maya package describes Playblast previews and a host-script handoff, but it does not guide installation and use of the official Jimeng Seedance 2.5 Maya uploader described in the supplied manual. Users need a directly installable skill for the graphical plugin workflow.

## What Changes

- Add `maya-dreamina-export` covering the official installer, Maya Plug-in Manager, camera rendering, existing-video upload, and web reference verification.
- Include one example for each route and register the new skill in the package manifest and catalogs.
- Keep `maya-export-preview` for local Playblast receipts and avoid making its host scripts prerequisites for official UI use.
- Route official uploader requests from `maya-use` to the new skill.

## Capabilities

### New Capabilities

- `maya-dreamina-reference-export`: Guide authorized official uploader installation and verify Maya white-model video handoff to Jimeng's web reference input.

## Impact

Skill source and package metadata only. No vendor ZIP or installer is redistributed; no undocumented API or paid generation is included.
