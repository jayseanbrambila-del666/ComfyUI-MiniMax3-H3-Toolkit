# MiniMax H3 Workflow Toolkit for ComfyUI

A small, dependency-free set of local utilities for MiniMax H3 workflows:

- build structured audiovisual prompts;
- flag missing temporal, camera, audio, or reference guidance;
- produce conservative workflow-starting advice from a hardware profile;
- save a portable text summary of a generation run.

The nodes do not call MiniMax3.org or any other network service. They contain no telemetry, tracking, account login, model download, or paid feature.

## Nodes

### MiniMax H3 Prompt Builder

Combines subject, scene, action over time, camera, lighting, motion, dialogue, soundscape, and reference instructions into one readable prompt. The output can be connected to the text input used by a native H3 conditioning workflow.

### MiniMax H3 Prompt Validator

Checks basic structure. It does not score aesthetics or predict output quality.

### MiniMax H3 Workflow Advisor

Produces cautious starting guidance based on workflow family, VRAM, system RAM, requested resolution, and duration. Its output is not an official hardware minimum or benchmark.

### MiniMax H3 Run Summary

Creates a portable record containing mode, resolution, duration, seed, references, and prompt.

## Install for development

Copy this directory into `ComfyUI/custom_nodes/`, restart ComfyUI, then search for `MiniMax H3` in the node library.

## Example workflows

Import the JSON files from `example_workflows/`. They demonstrate the toolkit nodes only and do not bundle or download MiniMax H3 model files.

## Documentation

For current native workflow links, model placement, VRAM caveats, and troubleshooting, see:

https://minimax3.org/minimax-h3-comfyui?utm_source=github&utm_medium=readme&utm_campaign=h3_toolkit

## Publishing checklist

1. Confirm the `minimax3-org` publisher at `registry.comfy.org`.
2. Confirm `PublisherId = "minimax3-org"` in `pyproject.toml`.
3. Confirm the repository URL under `[project.urls]`.
4. Run the tests and load all example workflows in a current ComfyUI build.
5. Publish with the official Comfy CLI or Registry GitHub Action.

## Independence

This community utility is independently maintained. It is not affiliated with, endorsed by, or operated by MiniMax or Comfy Org. MiniMax H3 and ComfyUI names may be trademarks of their respective owners.
