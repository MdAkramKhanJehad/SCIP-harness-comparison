# s4/batching.py — shared-session partition

Executable. LARGE units are appended after grouped non-LARGE units when size > 1.

```sudo
// Source: vvaharness/pipeline/stages/s4/batching.py:22-31
fn _overlap(a, b) { size of intersection of distinct a.files and b.files }
fn _best_partner(seed, pool) {
  seed_files = union of files in seed
  Select minimum pool member by [-size(seed_files intersection member.files), member.risk_rank, member.id].
}

// Source: vvaharness/pipeline/stages/s4/batching.py:34-48
fn plan_batches(units, size) {
  if (size <= 1) { yield singleton batches in input order and end this call }
  ordered = sort units by [risk_rank, id]
  large = singleton batches from ordered where size == UnitSize.LARGE
  pool = ordered members where size != UnitSize.LARGE
  batches = []
  while (pool is nonempty) {
    batch = [remove first member of pool]
    while (pool is nonempty && len(batch) < size) {
      Append and remove _best_partner(batch, pool).
    }
    Append batch to batches.
  }
  yield batches + large
}
```
