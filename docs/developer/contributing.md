# Contributing

## Contribution Status

FoodRPG is currently maintained as a solo development project.

External contributions are not being accepted at this time.

This document describes the project's intended contribution process and development conventions for future use.

## Development Priorities

The current priority is completing the prototype.

Development should prioritize:

- Working functionality.
- Accessibility.
- Keyboard usability.
- Clear component responsibilities.
- Reusable controls and services.
- Understandable dependencies.

Large-scale refactoring should not unnecessarily interrupt feature development.

## Accessibility

Accessibility is required for player-facing functionality.

New functionality should:

- Work with keyboard navigation.
- Use the shared keybinding system.
- Provide appropriate screen-reader announcements.
- Maintain predictable focus behavior.
- Avoid requiring mouse interaction.
- Make important information available through accessible interaction.

## Screens

New screens should use the existing screen infrastructure.

Screen-specific presentation belongs in the screen.

Screen-specific actions should be coordinated by the appropriate controller.

Navigation should use `ScreenManager` rather than introducing another navigation system.

## Controllers

Controllers should coordinate actions between screens, state, and services.

Controllers should not unnecessarily contain presentation logic or duplicate service functionality.

Dependencies should remain directional and circular imports should be avoided.

## Controls and Keybindings

Reusable interaction behavior should be added to the appropriate control rather than duplicated across screens.

Application-wide keyboard behavior should be added to the keybinding system.

Control-specific editing and interaction behavior should remain within the relevant control.

## Persistence

Changes to persistent models should consider save compatibility and the existing save-version mechanism.

Save and load functionality should be tested through the actual flows that use it.

Screens should not directly implement save-file formats.

## Settings

Application configuration should use the Settings system.

Individual screens should not directly manipulate configuration files.

## Documentation

Authoritative documentation belongs in:

- `docs/player/`
- `docs/developer/`

Unfinished ideas, experimental documentation, and future plans that are not ready to be published should remain in:

- `docs/drafts/`

Drafts are not considered authoritative documentation.

## Branches

The project uses a simple branch structure suitable for solo development:

- `main` contains released versions.
- `development` contains current development work.
- Feature or fix branches may be created from `development` when useful.

Releases are tagged from `main`.

## Commits

Use concise Conventional Commit-style messages where practical.

Examples:

- `feat: add gameplay session interface`
- `feat: add save slot management`
- `fix: restore gameplay after loading session`
- `refactor: simplify settings navigation`
- `docs: add project architecture`

## Pull Requests

When contributions are eventually enabled, pull requests should target `development`.

A pull request should explain:

- What changed.
- Why the change was made.
- Important fixes or behavioral changes.
- Known limitations.
- Architectural decisions that affect future development.

## Future Contribution Process

When external contributions are enabled, the expected process will be:

1. Create a branch from `development`.
2. Make the change.
3. Test the change.
4. Update relevant authoritative documentation when necessary.
5. Keep experimental or unfinished material in `docs/drafts/`.
6. Open a pull request against `development`.
7. Review the implementation and accessibility behavior.
8. Merge approved changes into `development`.

The contribution process may be revised when external contributions are actually introduced.
