from __future__ import annotations

from .minimax3_h3_toolkit.core import (
    build_prompt,
    build_run_summary,
    build_workflow_advice,
    validate_prompt,
)


MODES = ["T2VA", "I2VA", "FL2VA", "REF2VA"]


class MiniMax3H3PromptBuilder:
    @classmethod
    def INPUT_TYPES(cls):
        multiline = {"multiline": True, "default": ""}
        return {
            "required": {
                "mode": (MODES,),
                "subject": ("STRING", multiline),
                "scene": ("STRING", multiline),
                "action": ("STRING", multiline),
                "camera": ("STRING", multiline),
                "lighting": ("STRING", multiline),
                "motion": ("STRING", multiline),
                "dialogue": ("STRING", multiline),
                "soundscape": ("STRING", multiline),
                "reference_instructions": ("STRING", multiline),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("prompt", "validation_report")
    FUNCTION = "build"
    CATEGORY = "MiniMax3/H3 Utilities"
    DESCRIPTION = "Builds a structured MiniMax H3 audiovisual prompt locally. No network calls or telemetry."

    def build(self, mode, subject, scene, action, camera, lighting, motion, dialogue, soundscape, reference_instructions):
        prompt = build_prompt(mode, subject, scene, action, camera, lighting, motion, dialogue, soundscape, reference_instructions)
        return prompt, validate_prompt(mode, prompt).report


class MiniMax3H3PromptValidator:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"mode": (MODES,), "prompt": ("STRING", {"multiline": True, "default": ""})}}

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("status", "report")
    FUNCTION = "validate"
    CATEGORY = "MiniMax3/H3 Utilities"
    DESCRIPTION = "Checks prompt structure and reference guidance without predicting generation quality."

    def validate(self, mode, prompt):
        result = validate_prompt(mode, prompt)
        return result.status, result.report


class MiniMax3H3WorkflowAdvisor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mode": (MODES,),
                "vram_gb": ("INT", {"default": 16, "min": 4, "max": 192, "step": 1}),
                "system_ram_gb": ("INT", {"default": 64, "min": 8, "max": 1024, "step": 1}),
                "resolution": (["Lower than 768p", "768p class", "1080p", "2K"],),
                "duration_seconds": ("INT", {"default": 5, "min": 4, "max": 30, "step": 1}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("advice",)
    FUNCTION = "advise"
    CATEGORY = "MiniMax3/H3 Utilities"
    DESCRIPTION = "Produces conservative starting guidance. It does not claim an official minimum or benchmark."

    def advise(self, mode, vram_gb, system_ram_gb, resolution, duration_seconds):
        return (build_workflow_advice(mode, vram_gb, system_ram_gb, resolution, duration_seconds),)


class MiniMax3H3RunSummary:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mode": (MODES,),
                "resolution": ("STRING", {"default": "768p class"}),
                "duration_seconds": ("INT", {"default": 5, "min": 1, "max": 300, "step": 1}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                "references": ("STRING", {"multiline": True, "default": ""}),
                "prompt": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("run_summary",)
    FUNCTION = "summarize"
    CATEGORY = "MiniMax3/H3 Utilities"
    OUTPUT_NODE = True
    DESCRIPTION = "Creates a portable text record of an H3 run."

    def summarize(self, mode, resolution, duration_seconds, seed, references, prompt):
        return (build_run_summary(mode, resolution, duration_seconds, seed, references, prompt),)


NODE_CLASS_MAPPINGS = {
    "MiniMax3H3PromptBuilder": MiniMax3H3PromptBuilder,
    "MiniMax3H3PromptValidator": MiniMax3H3PromptValidator,
    "MiniMax3H3WorkflowAdvisor": MiniMax3H3WorkflowAdvisor,
    "MiniMax3H3RunSummary": MiniMax3H3RunSummary,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MiniMax3H3PromptBuilder": "MiniMax H3 Prompt Builder",
    "MiniMax3H3PromptValidator": "MiniMax H3 Prompt Validator",
    "MiniMax3H3WorkflowAdvisor": "MiniMax H3 Workflow Advisor",
    "MiniMax3H3RunSummary": "MiniMax H3 Run Summary",
}

