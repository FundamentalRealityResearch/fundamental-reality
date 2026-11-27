# Research corrections and failed checks

## 2026-11-26 — Relational clock phase and verification audit

- Original Session 2: correct relative phase exp(-iωt) for H_S = -ħω Z/2, with evolution understood up to overall phase.
- Initial published checkpoint (commit 309012e374f3340fea7f95280418ea23eb61c673): erroneously reversed the sign and described the original as incorrect.
- Subsequent amendment (commit 1ef0d34600f77cd2068bd2d8a469445dfc497f57): restored the correct sign but the accompanying chat did not clearly distinguish the full vector from its phase-stripped representative. Earlier computational verification claims are not independently reproducible from retained artifacts.
- Current audit: actually executed [clock_check.py](checks/clock_check.py) using SymPy 1.14.0; [captured output](checks/clock_check.txt). For the full state the residual is zero; for the phase-stripped ray it is (ħω/2) times the ray; using H_S + ħω I/2 gives zero. The opposite relative phase has nonzero orthogonal residual for nonzero ω, so cannot be repaired by a scalar shift.
- Impact: original physical ray and Fubini–Study distance conclusion remain correct. No novel physics or new prediction. Classification 2: independent check of known physics.
- Strongest limitation: this is a two-level model with an assumed Hamiltonian and clock structure. It does not derive time or its arrow from first principles. The verification is a symbolic self-check, not independent experimental confirmation.

Future entries must record failed checks and retractions, relevant artifacts, and impact on dependent claims. No deletion of unfavorable results.

## 2026-11-26 — Documentation consistency and reproduction

- Removed the stale closing statement in the checkpoint denying any executed test, which contradicted section C.
- Retrieved the published clock script and output; executed the same code in SymPy 1.14.0 in the chat's Python environment. All printed residuals matched the archived output exactly. This is a self-reproduction, not independent peer review. No change to physical conclusions.

## 2026-11-27 — Session 3 archival recovery and Session 4
- Session 3 (Nov 26) completed analytical work but did not archive, update changelog, or conduct fresh literature audit. Reason for omitted writes was not recorded; cannot diagnose retrospectively. Archived on Nov 27 as [Session 3](2026-11-26-session-3.md), preserving original research date. This does not retroactively mark the original run complete.
- Session 4 replaces engineered global projector with known clock propagation construction. Exact symbolic checks all passed (SymPy 1.14.0, exact arithmetic; no tolerance). [Code](checks/2026-11-27-history_check.py), [stdout](checks/2026-11-27-history_check.txt), [report](2026-11-27-session-4.md). The proposed explanation of an intrinsic arrow from record writing alone is not established; the selected blank input at one endpoint is imposed. No novel physics or prediction.
- Retrospective audit: Sessions 1–2 full historical transcripts and original claimed computational artifacts not all available in this run. Clock sign correction and later self-reproduction documented above. Session 3 missing steps documented; original source audit not retroactively credited. Fresh audit of reported breakthroughs is source-level, not reproduction of proofs. VP/VNP specific claim and detailed proof audits outstanding. No failed current symbolic assertion; no fabricated completion.
