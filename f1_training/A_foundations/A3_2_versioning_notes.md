# Versioning Notes

## Commit Message Audit

| Original | Should Have Been | Reason |
|---|---|---|
| `A3.1 Updating DB connection` | `fix(A3.1): update SQLite connection path to relative directory` | Missing type prefix, no scope, describes nothing about what actually changed or why |
| `A2.1: TP fixes — correct assertions, iloc/loc clarification, inspection methods` | `fix(A2.1): correct speed assertion threshold, add reset_index demo, fix inspection methods` | Good structure but the second fix commit repeats the same scope as the one before it — both should have been one commit since they fixed the same lesson |
| `init: pitwall — F1 data engineering program structure` | ✅ Good | Clear, scoped, describes exactly what the commit contains |
| `A2.2: TP complete — cleaning pipeline, pit flag, dtype coercion, rename, mychron cleaner` | ✅ Good | Detailed, specific, covers all changes in one line |
| `A3.1: SQLite schema, inserts, queries, FK enforcement, pandas round trip` | ✅ Good | Precise and complete |

## Rules I am applying going forward

Every commit must be atomic; one logical change per commit, not one file and not one session.

The message format is `type(scope): short description` where type is one of feat, fix, docs, refactor, test or chore.

A commit message that could describe any other commit in any other repo is not specific enough.

Never commit broken code to main. Every commit on main must work without fails. 