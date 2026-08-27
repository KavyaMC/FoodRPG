# Architecture

## Overview

FoodRPG uses a layered, screen-based application architecture designed around keyboard-first and screen-reader-accessible interaction.

The project separates application lifecycle management, shared state, services, screens, controllers, controls, models, and gameplay systems. Each layer has a focused responsibility so that new features can be added without making individual screens or controllers responsible for the entire application.

The architecture is intentionally lightweight because FoodRPG is still a prototype. Completing the playable product takes priority over premature abstraction and large-scale refactoring.

## Application Lifecycle

`Game` owns the application lifecycle and main loop.

It is responsible for initializing the application, starting the initial screen flow, processing events, and keeping the application running until the game exits.

Application-level transitions that affect the complete screen flow are handled at this level.

## Shared State

`GameState` contains shared application and gameplay state.

It provides access to the active session and application services that need to be shared between screens, controllers, and gameplay systems.

Gameplay state is represented by models such as `Player` and `Session`.

## Services

Services provide reusable application-level functionality.

Examples include:

- `ScreenManager` for screen-stack navigation.
- Speech services for accessible output.
- Settings services for application configuration.
- Save/load services for persistent game data.
- Path services for application resources and documentation.

Services should contain reusable application functionality rather than screen-specific behavior.

## Screen Management

`ScreenManager` owns the screen stack.

It provides operations for:

- Pushing a screen.
- Popping the current screen.
- Replacing the current screen.
- Clearing the screen stack.
- Dispatching input to the current screen.

The screen stack supports nested flows such as settings, save-slot selection, gameplay menus, and other temporary interfaces.

Application-level transitions that replace the entire current flow should rebuild the stack with a valid root screen rather than leaving the application without an active screen.

## Screens

Screens provide the player-facing interface.

A screen is responsible for:

- Presenting controls.
- Presenting information.
- Handling screen-level input.
- Connecting controls to appropriate actions.

Screens should not directly implement persistence formats, application lifecycle management, or reusable application services.

`ControlScreen` provides common behavior for keyboard-navigable screens containing controls.

## Controllers

Controllers coordinate actions between screens, state, and services.

They are responsible for operations such as:

- Validating input.
- Updating application or gameplay state.
- Calling services.
- Triggering notifications and announcements.
- Initiating screen transitions.

Controllers should not duplicate functionality that already belongs to controls or services.

Dependencies between controllers and screens should remain directional. Circular imports should be avoided by keeping responsibilities separated rather than introducing unnecessary abstractions.

## Controls

Controls provide reusable interaction behavior.

Examples include:

- `Button`
- `TextField`
- `ComboBox`
- `LabelField`

Controls handle interaction details appropriate to their type, including focus, activation, editing, and announcements.

## Keyboard Input

Shared keyboard behavior is centralized through the keybinding system.

This keeps common navigation and activation behavior consistent across screens.

Control-specific input remains within the control when it forms part of that control's interaction model.

## Accessibility

Accessibility is an architectural requirement rather than an additional feature applied later.

FoodRPG is designed around:

- Keyboard-first interaction.
- Screen-reader-compatible announcements.
- Predictable focus.
- Explicit control announcements.
- Accessible status information.
- Configurable speech verbosity.

Reusable accessibility behavior should be implemented in shared controls and services where practical instead of being duplicated across individual screens.

## Models and Persistence

Models represent gameplay and persistent data.

`Player` represents player and business information.

`Session` represents the active gameplay session, including player information, game time, location, objectives, tasks, activities, tutorial state, and other gameplay state.

Models provide serialization and deserialization so that screens and controllers do not need to understand the underlying save-file structure.

Persistent models include save-version information to support future changes to stored data.

## Gameplay

Gameplay-specific behavior belongs in gameplay systems and gameplay-level controllers rather than in generic UI infrastructure.

The gameplay screen provides access to gameplay actions and session information while remaining separate from generic screen-management responsibilities.

## Prototype Philosophy

FoodRPG is currently a prototype.

Development therefore prioritizes:

1. Completing the playable product.
2. Establishing working gameplay systems.
3. Maintaining accessibility.
4. Keeping responsibilities understandable.
5. Avoiding unnecessary abstractions.

Refactoring, optimization, and architectural cleanup remain important but should not unnecessarily delay prototype completion.

The architecture described here reflects the current implementation and may evolve as gameplay requirements become clearer.
