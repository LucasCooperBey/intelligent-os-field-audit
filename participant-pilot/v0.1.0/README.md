# Private peer-night harness exercise, v0.1.0

Prepared October 11, 2026 for Lucas's participant-preparation request. This is a local pilot, not an adopted replacement for frozen Field Audit method-v1, a published leaderboard, or an admission requirement.

Bring one existing piece of work, one difficulty and one result you can explain. You may use this exercise, bring a redacted result from the existing audit, or use an equivalent artifact walkthrough. Choosing the walkthrough or withholding private evidence is not failure. Your invitation is based on a useful peer exchange, not a numerical cutoff.

## What this measures

The existing twelve-dimension audit inventories a whole operating setup and includes model-assisted grading. This exercise adds small observable tasks. Neither isolates the harness from its model automatically. A comparison must hold the model, task version, tools, permissions, resource limits and starting state constant, or label the result as a comparison of whole configurations. Your own before/after test uses the same method and fixtures.

The historical Hermes, OpenClaw and G-Brain scores remain dated July 22. The separate reference manifest records freshly checked release identities, without assigning new scores from release notes. A version number or documented feature is not a measured outcome.

## Safe preparation

1. Use a new disposable directory and the supplied synthetic fixtures. Keep personal archives, credentials and client data outside it. No production systems or messaging tools are needed.
2. Use an already available plan or local model. Do not buy credits or invoke a metered model API without your own explicit spending decision.
3. Record the model and version, harness commit, prompt, task and fixture versions, tool permissions, run date, elapsed time, interventions and observed resource use. Unknown cost/tokens stay unknown.
4. Ask your harness to complete the five tasks in `tasks.json`. Save the result as `result.json` in the shape of `example-result.json`. The example is a public smoke-test answer, not a secret test or a credible competitive score. For a comparison, reserve alternate task instances before runs and keep their expected answers outside the agent's workspace.
5. Run `python3 verify.py result.json`. It validates submitted claims and artifact fields. It does not prove a model produced them, enforce read-only behavior or prove the harness was safe. A human or independent observer checks the saved trajectory and before/after fixture hashes.
6. Share only a sanitized summary if you choose. Local file paths, private documents and transcripts are not required. Public ledger submission is a separate choice.

## Record outcomes separately

- Valid success: a task meets its acceptance conditions and its evidence is inspectable.
- Task failure: the task was attempted under valid conditions and did not meet them.
- Could not evaluate: permissions, setup, missing inputs or infrastructure prevented a valid trial. Do not turn this into a zero competence score.
- Not attempted or declined: no technical conclusion.
- Not applicable: explain why the task is outside the setup's intended purpose; exclude it from a success-rate denominator.

For the pilot, report task-level observations and the smallest useful improvement. No pass mark, percentile or auto-invitation rule is calibrated. Repeatability can be explored with three comparable runs if the participant wants and resources permit; no run is launched by this packet. Keep individual run outcomes rather than selecting the best attempt.

## Change policy

Freeze each before/after pair. A change to tasks, inputs, available tools or resource budget requires a new run. A verifier-only correction can regrade saved artifacts when the required evidence exists. A wording-only correction may preserve results if it changes no behavior or interpretation. Keep original results, corrected result records and reasons. Do not silently lower or inflate old scores.

The design borrows versioning, task maintenance and independent verification ideas from [Terminal-Bench continuous benchmarks](https://www.tbench.ai/news/continuous-benchmarks) and its [4.0 resource/task revision](https://www.tbench.ai/news/terminal-bench-4-0). [SWE-bench](https://www.swebench.com/SWE-bench/) is useful for task-specific acceptance tests; [tau2-bench](https://github.com/sierra-research/tau2-bench) is useful for examining tool, user and environment interactions. These references do not validate this pilot or supply comparable scores.

## Peer-night use

Every guest gets four minutes to show existing work, one observation and one question. Two volunteered examples get deeper inspection. The group selects one next test or improvement for each participant. A missing audit does not remove the sharing slot. Education is offered by interest, with explicit permission for later program updates. A future paid-event discount needs its own actual terms; no discount is promised by this exercise.
