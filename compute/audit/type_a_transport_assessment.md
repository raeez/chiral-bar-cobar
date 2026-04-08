# Assessment: conj:type-a-transport-to-transpose (#9 in survey)

## Conjecture statement

At generic level, the transport-closure of the hook vertices is all of
Par(N), and Koszul/bar-cobar duality intertwines every proved
reduction or inverse-reduction edge. Consequently,
(W^k(sl_N, f_lambda))^! = W^{k^v_lambda}(sl_N, f_{lambda^t}).

Source: subregular_hook_frontier.tex, line 297.
Status: \ClaimStatusConjectured.

## The conjecture has two components

**Component 1 (graph-theoretic): hook transport-closure = Par(N).**
This is TRUE and in fact TRIVIAL, given the three edge families in the
reduction graph Gamma_N:

1. Hook spine: (N-r,1^r) <-> (N-r-1,1^{r+1}), via Fehily (2022).
2. Two-row to hook: (a,b) <-> (a+b-1,1), via Genra-Juillard (2023).
3. Row-merge: (a,b,c,...) <-> (a+b,c,...), via Butson-Nair (2024).

Any partition with >= 3 parts connects to a partition with one fewer
part by merging the two largest parts (edge type 3). Iterating reduces
to a two-row partition, which connects to a hook (edge type 2). The
hook spine (edge type 1) then connects to all other hooks. The path
length is at most len(lambda) - 1 merges + 1 two-row-to-hook edge.

Computationally verified at N = 2, ..., 12 (100% coverage at every N).
This is a theorem, not a conjecture, assuming the three edge families
are available -- which they are at generic level by the cited literature.

**Component 2 (functorial): Koszul duality intertwines each edge.**
This is the REAL content of the conjecture. It requires DS-bar
compatibility at each transport edge: that the DS reduction functor
commutes with bar-cobar duality up to quasi-isomorphism. The manuscript
itself acknowledges (rem:hook-formality-mechanism, line 279) that
"the current manuscript does not yet contain a clean proof that the
required DS/bar compatibility holds uniformly across the whole hook
network." The partition (3,2) in sl_5 is identified as the first
explicit non-abelian audit surface (rem:abelian-nonabelian-nilradical).

## What fraction of Par(N) is hook-type?

Hook partitions (N-r, 1^r) for r = 0, ..., N-1: exactly N hooks.

| N  | |Par(N)| | hooks | hook fraction |
|----|---------|-------|---------------|
|  4 |       5 |     4 |        0.8000 |
|  5 |       7 |     5 |        0.7143 |
|  6 |      11 |     6 |        0.5455 |
|  8 |      22 |     8 |        0.3636 |
| 10 |      42 |    10 |        0.2381 |
| 12 |      77 |    12 |        0.1558 |
| 15 |     176 |    15 |        0.0852 |
| 20 |     627 |    20 |        0.0319 |

Asymptotically, |Par(N)| ~ exp(pi sqrt(2N/3)) / (4N sqrt(3)) while
hooks = N, so the hook fraction decays super-exponentially to 0. By
N = 20, hooks are already < 4% of Par(N).

## First partition NOT reachable by transport from hook-type seeds

**None.** Every partition is reachable for all N, given the three edge
families. The row-merge mechanism (Butson-Nair) is the structural
reason: it provides a monotone path from any partition to a two-row
partition, which then connects to the hook spine.

If we restrict to ONLY hook-spine + two-row edges (removing Butson-Nair
row-merge), then the first unreachable partition is (2,2) at N = 4.
At N = 8, only 11/22 partitions are reached without row-merge. The
missed partitions are exactly those with >= 3 parts and no two-row
reduction path: e.g. (3,3,2), (2,2,2,2), (4,2,2) at N = 8.

## Edge-type contribution analysis (N = 8)

| Edge family      | Undirected edges | Alone covers |
|------------------|-----------------|--------------|
| Hook spine       |               7 |  8/22 (36%)  |
| + Two-row-hook   |            +  3 | 11/22 (50%)  |
| + Row-merge      |            + 17 | 22/22 (100%) |

Row-merge edges dominate the edge count and are indispensable for
full coverage. Without them, half of Par(N) is unreachable.

## Assessment

The graph-theoretic component (transport-closure = Par(N)) is settled:
it is a trivial consequence of the row-merge edge family, which exists
at generic level by Butson-Nair (2024). The conjecture's real content
is the functorial component: DS-bar compatibility at each edge. This
reduces to proving that DS reduction commutes with bar-cobar duality
at generic level for each edge type:

1. Hook-spine edges: conditional on DS/bar compatibility along the
   hook network (thm:hook-transport-corridor). The abelian-n+ locus
   supports the filtration-formality mechanism case by case, but
   hook-wide uniformity is not yet proved.

2. Two-row-to-hook edges: reduction-by-stages (Genra-Juillard).
   DS-bar compatibility for this edge type follows from the same
   Kazhdan filtration argument as for hooks.

3. Row-merge edges: Butson-Nair geometric inverse HR. DS-bar
   compatibility for general row-merge is the least explored and
   the most critical missing piece. The partition (3,2) in sl_5
   is the first non-trivial test case.

**Bottom line**: the conjecture is best understood as a statement about
DS-bar compatibility, not about graph connectivity. The graph is
trivially connected. The obstacle is functorial, concentrated at the
row-merge edges for non-abelian nilradicals. The first genuine test
case is (3,2) in sl_5.
