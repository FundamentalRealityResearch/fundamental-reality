# Initial research checkpoint — 2026-11-26

Status: analytical demonstrations and limitations, not verified novel discoveries. This record restates the mathematical portions of earlier reports. Reported numerical tests and current breakthrough news have not been independently reproduced or audited here and are excluded.

## A. Entanglement spectra do not specify all state information

For a multipartite pure state in a fixed product basis, complex conjugation sends each reduced density operator to its complex conjugate. Its eigenvalues are real and unchanged, so all subsystem von Neumann entropies agree. Nevertheless, expectation values of purely imaginary Hermitian operators can change sign. Example: the one-qubit states (|0> ± i|1>)/sqrt(2) have opposite Pauli-Y expectations. Entropy data alone do not recover every observable. This is established quantum mechanics.

## B. Abstract geometry and scale ambiguity

The Fubini–Study distance between normalized pure-state rays is d = arccos(|<a|b>|). For states cos(nθ)|0> + sin(nθ)|1>, d = |n-m| |θ| when the angular difference is at most π/2. This abstract dimensionless metric does not establish physical spatial distance or relativistic geometry.

For U = exp(-i H Δt/ħ), rescaling H by λ > 0 and Δt by 1/λ leaves U invariant. The transformation alone does not independently fix energy and time scales.

## C. Relational clock and recurrence

Let |Ψ> = (|00> + |11>)/sqrt(2), H_C = ħω Z/2 and H_S = -ħω Z/2 acting on distinct factors. The total Hamiltonian annihilates |Ψ>.

Conditioning on the clock ray (|0> + exp(-iωt)|1>)/sqrt(2) yields the normalized system ray (|0> + exp(iωt)|1>)/sqrt(2), which evolves under H_S up to an overall phase. The earlier report used the opposite clock phase and incorrectly identified the resulting generator as H_S rather than -H_S. This sign correction leaves the following distance calculation intact.

The Fubini–Study distance is arccos(|cos(ωΔt/2)|). For |ωΔt| ≤ π, it equals ΔE |Δt|/ħ, where ΔE = ħ|ω|/2. This restricted example of established quantum evolution geometry returns to zero after full cycles and does not uniquely count elapsed cycles.

Foundational references (bibliographic starting points, not freshly audited here):
- Page and Wootters, Phys. Rev. D 27, 2885 (1983), https://doi.org/10.1103/PhysRevD.27.2885
- Anandan and Aharonov, Phys. Rev. Lett. 65, 1697 (1990), https://doi.org/10.1103/PhysRevLett.65.1697
- Moreva et al., Phys. Rev. A 89, 052122 (2014), https://doi.org/10.1103/PhysRevA.89.052122

## Next test

Construct a finite clock–system–record model with a stationary history state. Compare forward and reversed conditional histories; distinguish imposed boundary conditions from a derived arrow of time. Test whether record correlations select a direction, check recurrence, and distinguish clock labels from physical duration. Do not presume abstract quantum geometry equals physical spacetime.

Audit reported AI-assisted breakthroughs against primary sources before using them as premises. No verified novel result yet; no executed computational test is claimed in this checkpoint.
