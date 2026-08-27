# Project Structure

## Overview

FoodRPG is organized from application-level components down to reusable interaction components, data models, and gameplay systems.

The structure is intended to make it clear where a responsibility belongs before new functionality is added.

## Application

The application layer contains the components responsible for starting and running the game.

### `Game`

Owns the application lifecycle and main loop.

### `GameState`

Stores shared application and gameplay state and provides access to shared services.

## Services

Services provide reusable functionality across the application.

Typical services include:

- `ScreenManager` — manages the screen stack.
- Speech service — provides accessible speech output.
- Settings service — manages application configuration.
- Save/load service — manages persistent gameplay data.
- Path service — provides paths for application resources and documentation.

## Screens

Screens provide the player-facing interface.

Current screens include areas such as:

- Main Menu.
- New Game.
- Save Slots.
- Gameplay.
- Resume.
- Settings.
- Documentation.

Screens present controls and information while delegating actions to their controllers.

## Controllers

Controllers coordinate screen actions with application state and services.

A typical interaction follows this flow:

```text
Screen
  ↓
Control
  ↓
Controller
  ↓
State / Service
  ↓
ScreenManager
  ↓
Next Screen
```

For example, saving from gameplay follows the general pattern:

```text
Gameplay / Resume
  ↓
Save Slots
  ↓
Save Slots Controller
  ↓
Save/Load Service
  ↓
Session serialization
  ↓
Save Slot
```

## Controls

Controls provide reusable keyboard-navigable interaction.

Examples include:

- `Button`
- `TextField`
- `ComboBox`
- `LabelField`

Controls manage their own interaction details where appropriate.

## Keybindings

The keybinding system defines shared keyboard interactions.

Screens and controls use the keybinding system instead of duplicating raw keyboard mappings throughout the application.

## Models

Models represent application and gameplay data.

### `Player`

Stores player and business information created during the New Game flow.

### `Session`

Stores the active gameplay session, including the player, game time, location, objective, current task, current activity, and tutorial state.

The session can be serialized for saving and reconstructed when loading.

## Gameplay Systems

Gameplay systems contain the actual rules and mechanics of FoodRPG.

They remain separate from generic UI infrastructure so gameplay functionality can grow without turning screens, controls, or generic services into containers for game rules.

## Documentation

Authoritative documentation is separated from private development drafts.

```text
docs/
├── player/
├── developer/
└── drafts/
```

### `docs/player/`

Contains player-facing documentation such as game documentation and changelogs.

### `docs/developer/`

Contains reliable technical documentation such as:

- Architecture.
- Project structure.
- Contributing guidelines.
- Development notes.
- Release notes.

### `docs/drafts/`

Contains unfinished documentation, experiments, future ideas, discarded approaches, and other private development material.

Draft material is not considered authoritative project documentation and is excluded from the public repository.

## Development Flow

The general development flow is:

```text
Feature / Fix
    ↓
Development Branch
    ↓
Testing
    ↓
Pull Request
    ↓
Development
    ↓
Release Preparation
    ↓
Main
    ↓
Version Tag
    ↓
GitHub Release
```

The project structure may evolve as gameplay systems become more established.
