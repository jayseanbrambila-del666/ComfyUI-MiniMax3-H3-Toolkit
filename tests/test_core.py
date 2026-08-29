import unittest

from minimax3_h3_toolkit.core import (
    build_prompt,
    build_run_summary,
    build_workflow_advice,
    validate_prompt,
)


class ToolkitCoreTests(unittest.TestCase):
    def test_prompt_builder_includes_reference_instruction_for_ref_mode(self):
        prompt = build_prompt(
            "REF2VA",
            "A ceramic robot",
            "A quiet workshop",
            "The robot turns toward the window over five seconds",
            "Slow tracking shot",
            "Warm afternoon light",
            "Continuous natural motion",
            "",
            "Soft motors and distant rain ambience",
            "Use <Picture 1> for identity and <Audio 1> for rhythm",
        )
        self.assertIn("task_mode: REF2VA", prompt)
        self.assertIn("reference_instructions:", prompt)
        self.assertIn("overall_soundscape:", prompt)

    def test_validator_flags_short_prompt(self):
        result = validate_prompt("T2VA", "A robot")
        self.assertEqual(result.status, "REVIEW")
        self.assertIn("very short", result.report)

    def test_validator_accepts_structured_prompt(self):
        prompt = (
            "subject: a dancer. scene: a theater. action_over_time: the dancer turns and walks forward. "
            "camera: slow tracking shot. lighting: warm spotlight. motion_and_continuity: continuous movement. "
            "overall_soundscape: footsteps and quiet audience ambience."
        )
        result = validate_prompt("T2VA", prompt)
        self.assertEqual(result.status, "PASS")

    def test_advisor_disclaims_hardware_minimum(self):
        advice = build_workflow_advice("I2VA", 12, 32, "768p class", 5)
        self.assertIn("not an official hardware minimum", advice)
        self.assertIn("experimental", advice)

    def test_run_summary_is_portable_text(self):
        summary = build_run_summary("T2VA", "768p class", 5, 42, "None", "A camera pans left")
        self.assertIn("Seed: 42", summary)
        self.assertIn("A camera pans left", summary)


if __name__ == "__main__":
    unittest.main()

