# Dameng — CV/portfolio site design spec

Personal CV/portfolio website for an FDE-style software engineer (TypeScript/JavaScript,
builds AI agents with LangChain and the Claude Code SDK to solve business problems).
Technique reference: [MengTo/kage](https://github.com/MengTo/kage) — same architecture
pattern (fixed Three.js canvas, scroll-driven camera, generated-art depth layers,
editorial typography), original theme and code. No code or art is reused from Kage;
`PROMPT.md` in that repo is published as a reusable technique brief, not the license to
reuse assets — Kage's own license grants no reuse of its code/art.

## 1. World concept

**"Deploy"** — a night orchestration space instead of Kage's temple. A dark landscape
built from a glowing grid-of-cells terrain (visually reads as a GitHub contribution
graph), populated with node clusters (servers/tools/business systems) connected by
traveling light-pulses — a literal visualization of an agent calling tools and
returning results. A rotating icosphere "orchestration orb" anchors the scene the way
Kage's moon does. Camera moves through the space on scroll.

## 2. Site structure

| # | Chapter | CV content | Live 3D | Generated assets |
|---|---|---|---|---|
| 1 | Boot (hero) | Name / role identity | Camera opens on the orb, title types in, scroll cue | none — live render |
| 2 | Initialize | Positioning statement | Camera pulls back, full grid + pulses revealed | 1 background plate |
| 3 | Experience | Work history, one node-cluster per role (max 3 roles) | Camera travels to a new node per role | 1 background plate (recropped per role) + foreground props |
| 4 | Projects | Agent projects — LangChain/Claude Code SDK work (max 3) | Distinct pulse/node per project | 1 background plate + foreground props |
| 5 | Signal (skills) | Tech stack as a constellation/rail of tool nodes | Mostly live geometry + type, no images needed | none |
| 6 | Afterlight (contact/footer) | Contact links, closing statement | Camera pulls back/ascends, grid dims | 1 background plate |

Content readiness: real company/project names not final yet — use placeholder copy
styled after typical AI Solutions Engineer / SDE job descriptions; swap in real content
later without restructuring chapters.

## 3. Visual style

**Palette** (GitHub-green-on-black, cool/warm pair like Kage's blue-charcoal/amber):
- Base: `#050607`
- Primary (structure/nominal): GitHub green ramp `#0e4429` → `#26a641` → `#39d353`
- Secondary (active/in-flight accent): warm amber `#d29922` — mirrors CI status colors
  (green = pass, amber = running)
- Text: `#e6edf3`

**Typography**: monospace display font (JetBrains Mono / IBM Plex Mono territory) for
oversized headings; clean sans for body copy. Small monospace atmosphere text
(commit-hash-style codes, `● ACTIVE` status strings, timestamps) replaces Kage's
vertical Japanese type as the decorative technical accent.

**Leonardo shot list** (10 images total, style-prefixed for cohesion):

> Prompt prefix: *"Cinematic dark technical illustration, near-black background,
> glowing GitHub-green (#39d353) and warm amber accent lighting, volumetric fog,
> restrained bloom, subtle film grain, moody night atmosphere, high detail, [SUBJECT],
> no text, no watermark, 16:9"*

Background plates (4, full-bleed, reused/recropped across chapters):
1. Wide grid-terrain establishing shot with light pulses (Initialize)
2. Close-up glowing terminal/server node (Experience, recrop per role)
3. Light-pulse mid-transit between nodes, motion-blur trail (Projects)
4. Pulled-back wide shot of the grid fading to calm (Afterlight)

Foreground alpha-cutouts (6, transparent props, reused across chapters):
1. Terminal/monitor frame silhouette
2. Cable bundle / fiber trail
3. Isolated glowing connector node
4. Floating code-bracket glyph cluster
5. Jagged circuit-fragment silhouette
6. Flowing signal-wave ribbon

Note: Leonardo output won't have clean alpha — foreground cutouts need a
background-removal pass (e.g. remove.bg) after generation.

## 4. Technical architecture

**Structure**: single `index.html` (structure + CSS + scene code + choreography) +
vendored `three.min.js`. No framework, no build step, no npm — static files, deployable
to GitHub Pages as-is. `assets/generated/` for background plates, `assets/foreground/`
for alpha cutouts.

**Scene composition**:
- Terrain: grid-of-cells plane, cell brightness/height evokes a contribution graph
- Hero object: rotating icosphere-with-edges "orchestration orb"
- Node clusters: emissive geometry, one per chapter (role/project)
- Light pulses: emissive particles on Catmull-Rom spline paths between nodes
- Camera rig: scroll position → damped progress (`damp(cur, to, rate, dt)` exponential
  decay, framerate-independent) → position on a spline — same *technique* as Kage's
  RIG, original code
- Post-processing: start with plain CSS `#grain`/`#vignette` overlay divs (Kage's
  cheaper layer); only build a custom combined shader pass if that's insufficient
- Foreground layers: `<img>` alpha cutouts + per-section `IntersectionObserver`
  choosing whichever section has the highest visibility ratio, toggling
  `fg-active`/`fg-retiring` classes for pin/fade

**Build order**:
1. Static HTML scaffold — sections, type system, palette, placeholder blocks
2. Live world — grid terrain + orb + scroll-damped camera (get one chapter right first)
3. Node clusters/pulses per chapter + foreground `IntersectionObserver` wiring
   (placeholder art)
4. Generate the 10 Leonardo images, swap in
5. Polish — grain/vignette/bloom, reduced-motion, mobile responsive, a11y labels
6. Real CV copy replaces placeholders

**Quality bar** (mirrors Kage's own PROMPT.md checklist): verify desktop and
~390×844 mobile, no 404s on any asset, clean browser console, one full scroll/nav
interaction tested end to end, reduced-motion preserves the complete reading
experience, semantic landmarks and accessible labels, custom cursor only on
fine-pointer devices.
