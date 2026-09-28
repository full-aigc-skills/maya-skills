## ADDED Requirements

### Requirement: Official Maya uploader setup is guided

The skill SHALL guide use of the official OS-specific installer, Maya Plug-in Manager, plugin loading, auto-loading, and uploader UI discovery.

#### Scenario: Maya plugin is not loaded

- **WHEN** the user requests Maya-to-Jimeng export but the uploader is not loaded
- **THEN** the skill checks installer completion, plugin path, loaded state, and current Maya compatibility before export

### Requirement: Both official video routes are supported

The skill SHALL support camera rendering from the Maya scene and selection of an already-rendered local video through the official uploader.

#### Scenario: Existing video is selected

- **WHEN** the user provides an already-rendered white-model video
- **THEN** the skill uses local upload without requiring another Maya scene render

### Requirement: Web reference handoff is independently verified

The skill SHALL report local media, uploader link, web navigation, and reference-video loading separately and SHALL NOT infer paid generation from a successful handoff.

#### Scenario: Link opens without visible reference

- **WHEN** the Jimeng page opens but its reference input does not show the intended video
- **THEN** the skill reports reference loading as failed or unverified rather than completed
