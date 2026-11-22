#!/usr/bin/env python3
"""
Refresh per-episode stats and the data table in LEARNINGS.md.

    python3 tools/learn.py --youtube /tmp/yt.json [--facebook /tmp/fb.json]

Each JSON file is the raw text returned by Zernio analytics_get_analytics
(an object with a "posts" list). Posts are matched to episodes through
episodes.json posted.<platform>.zernio_post == post.latePostId.

Writes episode["stats"][platform] = {views, likes, comments, shares, age_h, at}
and rewrites the block between the AUTO markers in LEARNINGS.md.
"""
import argparse, json, statistics
from datetime import datetime, timezone
from pathlib import Path

R = Path(__file__).resolve().parent.parent
NOW = datetime.now(timezone.utc)


def load_posts(path):
    if not path:
        return []
    raw = Path(path).read_text().strip()
    data = json.loads(raw)
    if isinstance(data, list) and data and isinstance(data[0], dict) and "text" in data[0]:
        data = json.loads(data[0]["text"])
    return data.get("posts", []) if isinstance(data, dict) else []


def age_hours(iso):
    try:
        t = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return round((NOW - t).total_seconds() / 3600, 1)
    except Exception:
        return None


def apply(eps, posts, platform):
    by_id = {}
    for p in posts:
        for k in (p.get("latePostId"), p.get("_id")):
            if k:
                by_id[k] = p
    n = 0
    for e in eps:
        post = (e.get("posted") or {}).get(platform) or {}
        p = by_id.get(post.get("zernio_post"))
        if not p:
            continue
        a = p.get("analytics") or {}
        views = a.get("views") or a.get("impressions") or a.get("reach") or 0
        e.setdefault("stats", {})[platform] = {
            "views": views, "likes": a.get("likes", 0), "comments": a.get("comments", 0),
            "shares": a.get("shares", 0), "avg_watch_s": round((a.get("igReelsAvgWatchTime") or 0) / 1000, 1), "age_h": age_hours(p.get("publishedAt", "")),
            "at": NOW.strftime("%Y-%m-%dT%H:%MZ"),
        }
        n += 1
    return n


def table(eps):
    rows = []
    def yt(e):
        return ((e.get("stats") or {}).get("youtube") or {})
    def fb(e):
        return ((e.get("stats") or {}).get("facebook") or {})
    mature = [e for e in eps if yt(e).get("age_h") and yt(e)["age_h"] >= 48]
    def grp(key, label, subset):
        out = {}
        for e in subset:
            k = e.get(key) or ("v1" if key == "v" else "?")
            out.setdefault(str(k), []).append(yt(e)["views"])
        if not out:
            return
        rows.append(f"\n**By {label}** (YouTube views, posts at least 48 h old)\n")
        rows.append("| " + label + " | videos | median views | best |")
        rows.append("|---|---|---|---|")
        for k, v in sorted(out.items(), key=lambda kv: -statistics.median(kv[1])):
            rows.append(f"| {k} | {len(v)} | {int(statistics.median(v))} | {max(v)} |")
    grp("v", "version", mature)
    v2 = [e for e in mature if e.get("v") == 2]
    for key, label in (("lane", "lane"), ("shape", "shape"), ("ending", "ending"), ("length_bucket", "length")):
        grp(key, label, v2)
    rows.append("\n**Every episode with YouTube stats** (newest first)\n")
    rows.append("| EP | title | v | lane | shape | length | YT views | likes | comments | FB views | FB avg watch | age h |")
    rows.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for e in sorted(eps, key=lambda e: -e["ep"]):
        s = yt(e)
        if not s:
            continue
        rows.append(f"| {e['ep']} | {e['title']} | {e.get('v', 1)} | {e.get('lane', '')} | {e.get('shape', '')} | "
                    f"{round(e.get('duration_s') or 0)} s | {s['views']} | {s['likes']} | {s['comments']} | "
                    f"{fb(e).get('views', '')} | {str(fb(e).get('avg_watch_s', '')) + ' s' if fb(e) else ''} | {s['age_h']} |")
    return "\n".join(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--youtube")
    ap.add_argument("--facebook")
    a = ap.parse_args()
    ep_path = R / "episodes.json"
    eps = json.loads(ep_path.read_text())
    for e in eps:
        d = e.get("duration_s") or 0
        if d:
            e["length_bucket"] = "under 60 s" if d < 60 else ("60-99 s" if d < 100 else "100 s+")
    ny = apply(eps, load_posts(a.youtube), "youtube")
    nf = apply(eps, load_posts(a.facebook), "facebook")
    ep_path.write_text(json.dumps(eps, indent=1, ensure_ascii=False) + "\n")
    lp = R / "LEARNINGS.md"
    txt = lp.read_text()
    s, e = "<!-- AUTO:START -->", "<!-- AUTO:END -->"
    block = f"{s}\n_Updated {NOW.strftime('%Y-%m-%d %H:%M UTC')}_\n{table(eps)}\n{e}"
    txt = txt[: txt.index(s)] + block + txt[txt.index(e) + len(e):]
    lp.write_text(txt)
    print(f"stats updated: youtube {ny}, facebook {nf}")


if __name__ == "__main__":
    main()
