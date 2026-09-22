from __future__ import annotations
def invoice(lines, round_to=1):
    out = []
    total = 0
    for name, amt in lines:
        v = int(amt)
        if round_to:
            v = (v // round_to) * round_to
        total += v
        out.append(f"{name}:{v}")
    if round_to and total % round_to:
        total = (total // round_to) * round_to
    out.append(f"TOTAL:{total}")
    return "\n".join(out)
