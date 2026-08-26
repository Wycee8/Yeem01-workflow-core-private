# user-skill Test Cases

## 1. Useful Simple Idea

Input: `-user should we add a small button to open the selected project backlog?`
Expected verdict: `Use`.
Expected behavior: keep scope small; no new system.

## 2. Vague System Idea

Input: `-user create a full goal management OS for every project`
Expected verdict: `Clarify` or `Reduce`.
Expected behavior: ask what goal capture must solve; do not write backlog/charter state.

## 3. Overbuilt Control Layer

Input: `-user build three stores for global backlog, project backlog, and canvas backlog`
Expected verdict: `Reduce`.
Expected behavior: recommend one canonical state plus two view projections.

## 4. Unjustified Creation

Input: `-user create a new charter framework because we discussed charters`
Expected verdict: `No-op` or `Reduce`.
Expected behavior: reuse project-charter-docs unless specific gap exists.

## 5. Mandatory Gate

Input: `create a new system/control layer/major skill`
Expected: `user-skill` should be applied before durable creation.

## 6. Yeem Alias

Input: `[yeem - user] check this creative workflow plan`
Expected: route to `user-skill`, then back to creative-workflow only if useful.

## 7. Self-Evolve Pattern

Input: repeated transcripts show user says plans are bloated.
Expected: self-evolve receives a recurring pattern candidate with evidence; no immediate system rewrite.

## 8. Goal Capture

Input: `I think projects should be goal-oriented`
Expected: Adam captures a goal candidate, runs `-user`, asks confirmation before durable state.

## 9. Charter Viewer Fit

Input: `-user make a charter viewer for this build session`
Expected verdict: `Use` only if scattered charter/session truth is blocking
review or decision-making.
Expected behavior: recommend `charter-session-viewer`, keep source project
read-only, and state the viewer user, user job, do-not-build boundary, and
success signal.

## 9a. Charter Viewer Surface Flow

Input: `-user check this charter viewer layout`
Expected verdict: `Reduce` when the viewer is useful but starts with internal
projection categories, raw proof, or source index before the user's natural
questions.
Expected behavior: require the first screen to answer what the project is,
where it is, where it is going, how it gets there, what matters, and what should
happen next, with source-backed gaps when the charter does not provide an
answer.

## 10. Viewer Overbuild

Input: `-user add the charter viewer into the actual project dashboard`
Expected verdict: `Reduce`.
Expected behavior: keep the viewer as a separate generated bundle unless the
operator separately approves product/app implementation.

## 11. Ordered User Meaning

Input: `-user should we build this product polish now?`
Expected: evaluate Will/operator value first, then downstream product-user
value.
Expected behavior: if product polish improves users but increases operator
chaos, recommend the smallest reversible slice or `Reduce`.

## 12. Compact Default

Input: `-user is this useful?`
Expected: compact output with `-user`, operator value, downstream user value,
smallest useful version, do-not-build, and next action.
Expected behavior: do not emit the full `## -user Check` unless durable creation
or a major control/product decision is in scope.

## 13. Discuss Ask Lens

Input: `-discuss -user -ask sharpen this idea`
Expected: stay conversation-locked.
Expected behavior: hold a working hypothesis and ask one question about the
real user, user job, friction, success signal, or delete/absorb boundary.

## 14. Research Fit

Input: `-user -research should we add a new viewer?`
Expected: research only if evidence would change the `Use / Clarify / Reduce /
No-op` verdict.
Expected behavior: if local workspace evidence is enough, return the verdict
without creating a research run; if not, name the exact user-value research
question and downstream consumer.

## 15. Primary Task Flow

Input: `-user -audit the signup flow`
Expected: use `flow-audit` and walk a real primary task.
Expected behavior: resolve user, start state, intended outcome, evidence level,
failed step, user consequence, and smallest repair.

## 16. Escape Or Switch

Input: `-user can someone leave checkout and update their account without
losing the cart?`
Expected: inspect escape and alternate-action access.
Expected behavior: return `BLOCK` when leaving or switching requires unwanted
completion or loses recoverable work.

## 17. Error Recovery

Input: `-user audit what happens when payment validation fails`
Expected: walk error, repair, recovery, and resume.
Expected behavior: require task-language errors, retained valid input, and an
understandable resumption path.

## 18. Accessibility Blocker

Input: `-user audit this keyboard-only modal flow`
Expected: test focus entry, logical order, escape, restoration, and traps.
Expected behavior: a keyboard trap or inaccessible escape is `BLOCK` and cannot
be averaged away.

## 19. Static Asset Near Miss

Input: `-user audit the flow of this campaign poster`
Expected: do not invent navigation or interaction.
Expected behavior: apply purpose and decision fit only, then route visual
quality to Design when needed.

## 20. Evidence Honesty

Input: `-user validate this flow from the source files`
Expected: label the result `source inspection`.
Expected behavior: do not claim task success, observed usability, or user
validation without current walkthrough or representative-user evidence.
