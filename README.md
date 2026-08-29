# MiniMax H3 Workflow Toolkit for ComfyUI

![MiniMax H3 Workflow Toolkit](docs/minimax-h3-toolkit-banner.png)

[![Comfy Registry](https://img.shields.io/badge/Comfy_Registry-v0.1.1-6f42c1)](https://registry.comfy.org/publishers/minimax3-org/nodes/comfyui-minimax3-h3-toolkit)
[![Documentation](https://img.shields.io/badge/Guide-minimax3.org-1683ff)](https://minimax3.org/minimax-h3-comfyui?utm_source=github&utm_medium=readme_badge&utm_campaign=h3_toolkit)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A small, dependency-free MiniMax H3 ComfyUI toolkit for building clearer local video workflows:

- build structured audiovisual prompts;
- flag missing temporal, camera, audio, or reference guidance;
- produce conservative workflow-starting advice from a hardware profile;
- save a portable text summary of a generation run.

The nodes do not call MiniMax3.org or any other network service. They contain no telemetry, tracking, account login, model download, or paid feature.

## Quick start

1. Open ComfyUI Manager and search for `MiniMax H3 Workflow Toolkit`, or install this repository in `ComfyUI/custom_nodes/`.
2. Restart ComfyUI and search the node library for `MiniMax H3`.
3. Import a workflow from `example_workflows/` and connect its text output to your H3 conditioning workflow.
4. Follow the [MiniMax H3 ComfyUI guide](https://minimax3.org/minimax-h3-comfyui?utm_source=github&utm_medium=quick_start&utm_campaign=h3_toolkit) for current model placement, native workflow links, and troubleshooting.

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

Import the JSON files from [`example_workflows/`](example_workflows/). They demonstrate the toolkit nodes only and do not bundle or download MiniMax H3 model files.

- [Prompt Builder for T2VA](example_workflows/h3_prompt_builder_t2va.json)
- [Reference Prompt Validator](example_workflows/h3_reference_prompt_validator.json)
- [Local Workflow Advisor](example_workflows/h3_local_workflow_advisor.json)

## Documentation

For current native workflow links, model placement, VRAM caveats, and troubleshooting, use the maintained guide:

**[Open the MiniMax H3 ComfyUI setup guide →](https://minimax3.org/minimax-h3-comfyui?utm_source=github&utm_medium=documentation_cta&utm_campaign=h3_toolkit)**

The website guide contains optional supplementary information. The custom nodes themselves remain local, dependency-free, and usable without visiting the website.

## Publishing checklist

1. Confirm the `minimax3-org` publisher at `registry.comfy.org`.
2. Confirm `PublisherId = "minimax3-org"` in `pyproject.toml`.
3. Confirm the repository URL under `[project.urls]`.
4. Run the tests and load all example workflows in a current ComfyUI build.
5. Publish with the official Comfy CLI or Registry GitHub Action.

## Independence

This community utility is independently maintained. It is not affiliated with, endorsed by, or operated by MiniMax or Comfy Org. MiniMax H3 and ComfyUI names may be trademarks of their respective owners.
