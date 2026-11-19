# Experiment 10 – Git Branching & Merge Conflict

Use two branches to create a controlled conflict in the same README line.

```bash
git switch -c conflict-branch-a
# Edit the target line, then:
git add README.md
git commit -m "Change README from branch A"

git switch main
git switch -c conflict-branch-b
# Change the same line differently, then:
git add README.md
git commit -m "Change README from branch B"

git merge conflict-branch-a
# Resolve conflict markers, then:
git add README.md
git commit -m "Resolve README merge conflict"
```

Perform this in a disposable clone or test repository. No conflict is fabricated in the existing main branch.
