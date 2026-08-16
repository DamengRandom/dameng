# Dameng — build brief

The prompt this site was built from. Reusable as a technique brief for anyone building a
similar scroll-driven, cinematic single-page site — the *pattern* is generic, the theme,
copy, code, and generated art here are original to this project and are not licensed for
reuse as-is.

## 0. Brief

> Build a scroll-driven, cinematic CV/portfolio site for an AI agent engineer, rendered
> live in Three.js: a fixed WebGL canvas driven by scroll position, layered with
> generated cinematic background stills and alpha-cutout foreground props for depth,
> under editorial monospace/sans typography. No framework, no build step — a single
> static HTML file deployable as-is to GitHub Pages. Six chapters, each pairing one
> beat of CV content with one beat of the 3D scene.

## 1. World concept

**"Deploy"** — a night orchestration space. A dark landscape built from a glowing
grid-of-cells terrain (visually reads as a GitHub contribution graph), populated with
node clusters (servers/tools/business systems) connected by traveling light-pulses — a
literal visualization of an agent calling tools and returning results. A rotating
icosphere "orchestration orb" anchors the scene as the gravitational center of the
composition. Camera moves through the space on scroll.

## 2. Site structure

Six chapters, each one beat of CV content paired with one beat of the live 3D scene:

| # | Chapter | CV content | Live 3D | Generated assets |
|---|---|---|---|---|
| 1 | Boot (hero) | Name / role identity | Camera opens on the orb, title types in, scroll cue | none — live render |
| 2 | Initialize | Positioning statement | Camera pulls back, full grid + pulses revealed | 1 background plate |
| 3 | Experience | Work history, one node-cluster per role (max 3 roles) | Camera travels to a new node per role | 1 background plate (recropped per role) + foreground props |
| 4 | Projects | Agent projects — LangChain/Claude Code SDK work (max 3) | Distinct pulse/node per project | 1 background plate + foreground props |
| 5 | Signal (skills) | Tech stack as a constellation/rail of tool nodes | Mostly live geometry + type, no images needed | none |
| 6 | Afterlight (contact/footer) | Contact links, closing statement | Camera pulls back/ascends, grid dims | 1 background plate |

## 3. Visual style

**Palette** (GitHub-green-on-black, cool/warm nominal-vs-active pair):
- Base: `#050607`
- Primary (structure/nominal): GitHub green ramp `#0e4429` → `#26a641` → `#39d353`
- Secondary (active/in-flight accent): warm amber `#d29922` — mirrors CI status colors
  (green = pass, amber = running)
- Text: `#e6edf3`

**Typography**: monospace display font (JetBrains Mono / IBM Plex Mono territory) for
oversized headings; clean sans for body copy. Small monospace atmosphere text
(commit-hash-style codes, `● ACTIVE` status strings, timestamps) serves as the
decorative technical accent.

**Generated-image prompt template** (10 images total, style-prefixed for cohesion):

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

Note: raw generated output won't have clean alpha — foreground cutouts need a
background-removal pass after generation.

**Mark**: the nav/favicon logomark reuses the same motif as the hero object — an orb
ring in the green ramp with a single amber pulse dot on the rim — so the brand mark
literally reads as a miniature of the live scene.

## 4. Technical architecture

**Structure**: single `index.html` (structure + CSS + scene code + choreography) +
vendored `three.module.js`. No framework, no build step, no npm — static files,
deployable to GitHub Pages as-is. `assets/generated/` for background plates,
`assets/foreground/` for alpha cutouts.

**Scene composition**:
- Terrain: grid-of-cells plane, cell brightness/height evokes a contribution graph
- Hero object: rotating icosphere-with-edges "orchestration orb"
- Node clusters: emissive geometry, one per chapter (role/project)
- Light pulses: emissive particles on Catmull-Rom spline paths between nodes
- Camera rig: scroll position → damped progress (`damp(cur, to, rate, dt)` exponential
  decay, framerate-independent) → position on a spline
- Post-processing: start with plain CSS `#grain`/`#vignette` overlay divs (the cheaper
  layer); only build a custom combined shader pass if that's insufficient
- Foreground layers: `<img>` alpha cutouts + per-section `IntersectionObserver`
  choosing whichever section has the highest visibility ratio, toggling
  `fg-active`/`fg-retiring` classes for pin/fade

**Build order**:
1. Static HTML scaffold — sections, type system, palette, placeholder blocks
2. Live world — grid terrain + orb + scroll-damped camera (get one chapter right first)
3. Node clusters/pulses per chapter + foreground `IntersectionObserver` wiring
   (placeholder art)
4. Generate the 10 images, swap in
5. Polish — grain/vignette/bloom, reduced-motion, mobile responsive, a11y labels
6. Real CV copy replaces placeholders

**Quality bar**: verify desktop and ~390×844 mobile, no 404s on any asset, clean
browser console, one full scroll/nav interaction tested end to end, reduced-motion
preserves the complete reading experience, semantic landmarks and accessible labels,
custom cursor only on fine-pointer devices.
