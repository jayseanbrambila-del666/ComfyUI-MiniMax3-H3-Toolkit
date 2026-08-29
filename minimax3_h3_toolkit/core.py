from __future__ import annotations

from dataclasses import dataclass


MODE_LABELS = {
    "T2VA": "text-to-video with audio",
    "I2VA": "image-to-video with audio",
    "FL2VA": "first-and-last-frame video with audio",
    "REF2VA": "reference-guided video with audio",
}


def _clean(value: str) -> str:
    return " ".join((value or "").strip().split())


def _section(label: str, value: str) -> str | None:
    cleaned = _clean(value)
    return f"{label}: {cleaned}" if cleaned else None


def build_prompt(
    mode: str,
    subject: str,
    scene: str,
    action: str,
    camera: str,
    lighting: str,
    motion: str,
    dialogue: str,
    soundscape: str,
    reference_instructions: str,
) -> str:
    """Build a readable H3 audiovisual prompt without calling a network service."""
    mode = mode if mode in MODE_LABELS else "T2VA"
    sections = [
        f"task_mode: {mode} ({MODE_LABELS[mode]})",
        _section("subject", subject),
        _section("scene", scene),
        _section("action_over_time", action),
        _section("camera", camera),
        _section("lighting", lighting),
        _section("motion_and_continuity", motion),
        _section("dialogue", dialogue),
        _section("overall_soundscape", soundscape),
    ]
    if mode in {"I2VA", "FL2VA", "REF2VA"}:
        sections.append(_section("reference_instructions", reference_instructions))
    return "\n".join(section for section in sections if section)


@dataclass(frozen=True)
class ValidationResult:
    status: str
    report: str


def validate_prompt(mode: str, prompt: str) -> ValidationResult:
    cleaned = _clean(prompt)
    lowered = cleaned.lower()
    issues: list[str] = []
    suggestions: list[str] = []

    if len(cleaned) < 80:
        issues.append("Prompt is very short for a multimodal video task.")
    if not any(token in lowered for token in ("action", "moves", "walks", "turns", "changes", "over time")):
        issues.append("No clear temporal action was detected.")
    if not any(token in lowered for token in ("camera", "shot", "pan", "dolly", "tracking", "close-up", "wide")):
        suggestions.append("Add camera framing or movement.")
    if not any(token in lowered for token in ("sound", "audio", "dialogue", "music", "ambience", "voice")):
        suggestions.append("Add dialogue, ambience, music, or another sound intention.")

    if mode in {"I2VA", "FL2VA", "REF2VA"} and not any(
        token in lowered for token in ("picture", "image", "frame", "reference", "video", "audio")
    ):
        issues.append(f"{mode} should explain how its input or reference media is used.")
    if mode == "FL2VA" and not ("first" in lowered and "last" in lowered):
        suggestions.append("Describe both the first-frame state and the last-frame state.")
    if mode == "REF2VA" and not any(token in lowered for token in ("<picture", "<video", "<audio", "reference")):
        suggestions.append("Name each reference role clearly and keep numbering consistent with the workflow.")

    status = "PASS" if not issues else "REVIEW"
    lines = [f"status: {status}"]
    lines.extend(f"issue: {item}" for item in issues)
    lines.extend(f"suggestion: {item}" for item in suggestions)
    if not issues and not suggestions:
        lines.append("No basic structure problems detected. Review the final prompt against the active workflow and model version.")
    lines.append("This validator checks structure only; it does not predict output quality.")
    return ValidationResult(status=status, report="\n".join(lines))


def build_workflow_advice(
    mode: str,
    vram_gb: int,
    system_ram_gb: int,
    resolution: str,
    duration_seconds: int,
) -> str:
    mode = mode if mode in MODE_LABELS else "T2VA"
    notes = [
        f"workflow_family: {mode}",
        f"hardware_profile: {vram_gb} GB VRAM / {system_ram_gb} GB system RAM",
        f"requested_output: {resolution}, {duration_seconds}s",
        "recommendation_basis: practical starting guidance, not an official hardware minimum",
    ]

    if vram_gb <= 12:
        notes.append("start: use a conservative resolution and short duration; expect aggressive offloading or an optimized community workflow")
        notes.append("risk: this configuration should be treated as experimental until reproduced on the exact GPU and software stack")
    elif vram_gb <= 16:
        notes.append("start: validate a short lower-resolution run before increasing duration or resolution")
        notes.append("risk: text encoder and VAE decode can exceed available memory even when sampling begins successfully")
    elif vram_gb <= 24:
        notes.append("start: use the native workflow and validate memory headroom before increasing output size")
    else:
        notes.append("start: use the current native workflow, then benchmark one variable at a time")

    if system_ram_gb < 32:
        notes.append("system_ram_warning: CPU offloading may be constrained")
    elif system_ram_gb < 64:
        notes.append("system_ram_note: avoid assuming that free RAM equals usable offload capacity")

    if resolution == "2K":
        notes.append("2k_note: verify whether the selected workflow is a true supported 2K path or an upscale; do not infer this from output dimensions alone")
    if duration_seconds > 10:
        notes.append("duration_note: test a shorter clip first because memory use and generation time can rise materially")

    notes.append("fallback: if setup or tuning costs more time than the job is worth, compare with a browser-based run")
    return "\n".join(notes)


def build_run_summary(
    mode: str,
    resolution: str,
    duration_seconds: int,
    seed: int,
    references: str,
    prompt: str,
) -> str:
    return "\n".join(
        [
            f"Mode: {mode}",
            f"Resolution: {resolution}",
            f"Duration: {duration_seconds}s",
            f"Seed: {seed}",
            f"References: {_clean(references) or 'None recorded'}",
            "Prompt:",
            (prompt or "").strip(),
        ]
    )

