# Release checklist

## Blocking identity fields

- [x] Confirm the Comfy Registry Publisher ID: `minimax3-org`.
- [ ] Confirm the GitHub organization or account.
- [ ] Create the repository and replace the placeholder publisher value.
- [ ] Add the confirmed repository URL to `pyproject.toml`.

## Technical verification

- [ ] Run `python -m unittest discover -s tests -v`.
- [ ] Copy the package into a clean current ComfyUI `custom_nodes` directory.
- [ ] Confirm all four nodes load without errors.
- [ ] Import all JSON files in `example_workflows`.
- [ ] Connect the Prompt Builder output to the active native H3 workflow text input.
- [ ] Confirm no network calls or telemetry occur.

## Registry release

- [x] Create the Registry publisher: `https://registry.comfy.org/publishers/minimax3-org`.
- [ ] Create the publishing key only after explicit confirmation; store it securely and never commit it.
- [x] Add the official GitHub Actions publishing workflow using `REGISTRY_ACCESS_TOKEN`.
- [x] Add the GitHub repository URL to `pyproject.toml`: `jayseanbrambila-del666/ComfyUI-MiniMax3-H3-Toolkit`.
- [ ] Run Registry validation or the current Comfy CLI checks.
- [ ] Publish version `0.1.0` only after the clean-install test passes.
- [ ] Capture the exact Registry acknowledgment and public node URL.
- [ ] Replace website-module placeholders only after the public URLs exist.

## Gallery

- [ ] Generate the proposed showcase in a documented ComfyUI workflow.
- [ ] Confirm rights for all reference media and audio.
- [ ] Submit through the official Comfy Gallery form.
- [ ] Do not claim acceptance until Comfy publishes the work.
