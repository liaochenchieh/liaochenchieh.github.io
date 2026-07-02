---
layout: page
title: Motion Style Slider
description: Continuous style-intensity control for human motion diffusion.
img: assets/img/motion-style-slider/teaser.png
importance: 1
category: research
permalink: /projects/motion-style-slider/
_styles: |
  .post-header {
    display: none;
  }

  .mss-page {
    --mss-ink: #15211c;
    --mss-muted: #5f6d66;
    --mss-accent: #cf513f;
    --mss-accent-dark: #9f3327;
    --mss-paper: #f5f0e7;
    color: var(--mss-ink);
    margin: -1.5rem auto 4rem;
    max-width: 1120px;
  }

  .mss-hero {
    background:
      radial-gradient(circle at 84% 16%, rgba(207, 81, 63, 0.18), transparent 32%),
      linear-gradient(135deg, #f7f2e9 0%, #edf2ec 100%);
    border: 1px solid rgba(21, 33, 28, 0.1);
    border-radius: 2rem;
    overflow: hidden;
    padding: clamp(2rem, 6vw, 5rem) clamp(1.25rem, 5vw, 4.5rem) 0;
  }

  .mss-kicker {
    color: var(--mss-accent-dark);
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    margin-bottom: 1rem;
    text-transform: uppercase;
  }

  .mss-title {
    color: var(--mss-ink);
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(2.35rem, 6vw, 5.4rem);
    font-weight: 600;
    letter-spacing: -0.045em;
    line-height: 0.98;
    margin: 0 auto 1.25rem;
    max-width: 950px;
  }

  .mss-subtitle {
    color: var(--mss-muted);
    font-size: clamp(1.05rem, 2vw, 1.35rem);
    line-height: 1.55;
    margin: 0 0 1.35rem;
    max-width: 790px;
  }

  .mss-authors {
    font-size: 1rem;
    line-height: 1.7;
    margin-bottom: 0.8rem;
  }

  .mss-affiliations {
    color: var(--mss-muted);
    font-size: 0.94rem;
    line-height: 1.65;
    margin-bottom: 0.75rem;
  }

  .mss-note {
    color: var(--mss-muted);
    font-size: 0.88rem;
    margin-bottom: 1.5rem;
  }

  .mss-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
    margin-bottom: 2.5rem;
  }

  .mss-button {
    align-items: center;
    background: var(--mss-ink);
    border: 1px solid var(--mss-ink);
    border-radius: 999px;
    color: #fff !important;
    display: inline-flex;
    font-weight: 650;
    gap: 0.45rem;
    padding: 0.7rem 1.15rem;
    text-decoration: none !important;
    transition: transform 160ms ease, background 160ms ease;
  }

  .mss-button:hover {
    background: var(--mss-accent-dark);
    border-color: var(--mss-accent-dark);
    transform: translateY(-2px);
  }

  .mss-teaser {
    background: #fff;
    border-radius: 1.25rem 1.25rem 0 0;
    box-shadow: 0 18px 50px rgba(21, 33, 28, 0.12);
    display: block;
    width: 100%;
  }

  .mss-section {
    margin: clamp(3.5rem, 8vw, 7rem) auto 0;
    max-width: 940px;
  }

  .mss-section h2 {
    color: var(--mss-ink);
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(2rem, 4vw, 3.2rem);
    letter-spacing: -0.03em;
    margin-bottom: 1.25rem;
  }

  .mss-section p {
    color: var(--mss-muted);
    font-size: 1.08rem;
    line-height: 1.8;
  }

  .mss-figure {
    background: #fff;
    border: 1px solid rgba(21, 33, 28, 0.1);
    border-radius: 1.2rem;
    box-shadow: 0 16px 45px rgba(21, 33, 28, 0.08);
    margin: 2rem 0 0;
    overflow: hidden;
    padding: clamp(0.45rem, 2vw, 1.25rem);
  }

  .mss-figure img {
    display: block;
    width: 100%;
  }

  .mss-figure figcaption {
    color: var(--mss-muted);
    font-size: 0.9rem;
    line-height: 1.55;
    padding: 0.8rem 0.45rem 0.2rem;
  }

  .mss-points {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(3, 1fr);
    margin-top: 2rem;
  }

  .mss-point {
    background: var(--mss-paper);
    border-radius: 1rem;
    padding: 1.35rem;
  }

  .mss-point strong {
    color: var(--mss-accent-dark);
    display: block;
    font-size: 0.78rem;
    letter-spacing: 0.1em;
    margin-bottom: 0.55rem;
    text-transform: uppercase;
  }

  .mss-point span {
    color: var(--mss-ink);
    line-height: 1.55;
  }

  .mss-citation {
    background: #17221d;
    border-radius: 1.25rem;
    color: #e8eee9;
    overflow-x: auto;
    padding: 1.35rem;
  }

  .mss-citation code {
    color: inherit;
    white-space: pre-wrap;
  }

  @media (max-width: 767px) {
    .mss-page {
      margin-top: -0.5rem;
    }

    .mss-hero {
      border-radius: 1.25rem;
    }

    .mss-points {
      grid-template-columns: 1fr;
    }
  }
---

<div class="mss-page">
  <section class="mss-hero">
    <div class="mss-kicker">ECCV 2026</div>
    <h1 class="mss-title">Motion Style Slider</h1>
    <p class="mss-subtitle">Endpoint-Supervised Continuous Style Control for Human Motion Diffusion</p>
    <p class="mss-authors">
      <a href="https://liaochenchieh.com/" target="_blank" rel="noopener"><strong>Chen-Chieh Liao</strong></a><sup>1,3,*</sup>,
      <a href="https://puckikk1202.github.io/" target="_blank" rel="noopener">Yichen Peng</a><sup>1</sup>,
      Yiyi Cai<sup>2</sup>,
      <a href="https://orcid.org/0000-0002-8243-7753" target="_blank" rel="noopener">Yûi Ono</a><sup>3</sup>,
      <a href="https://orcid.org/0000-0001-8286-5013" target="_blank" rel="noopener">Hiroki Hanaoka</a><sup>3</sup>,
      <a href="https://erwinwu.com/" target="_blank" rel="noopener">Erwin Wu</a><sup>1</sup>,
      <a href="https://www.vogue.cs.titech.ac.jp/koike" target="_blank" rel="noopener">Hideki Koike</a><sup>1</sup>,
      and
      <a href="https://orcid.org/0000-0001-5967-7727" target="_blank" rel="noopener">Shuichi Kurabayashi</a><sup>3</sup>
    </p>
    <p class="mss-affiliations">
      <sup>1</sup>Institute of Science Tokyo &nbsp;&nbsp;
      <sup>2</sup>The University of Tokyo &nbsp;&nbsp;
      <sup>3</sup>Cygames, Inc.
    </p>
    <p class="mss-note">
      <sup>*</sup>The work was partially done during an internship at Cygames, Inc.
    </p>
    <img
      class="mss-teaser"
      src="{{ '/assets/img/motion-style-slider/teaser.png' | relative_url }}"
      alt="Motion Style Slider changes a human motion smoothly from neutral to stylized and beyond the observed endpoint."
    >
  </section>

  <section class="mss-section">
    <h2>A slider for motion style</h2>
    <p>
      Motion Style Slider is a motion-to-motion diffusion framework for fine-grained control of style intensity.
      Given a content motion and a stylized endpoint, the model generates a continuous family of motions controlled
      by a scalar value, from neutral behavior through the target style and into stronger out-of-range reactions.
      The control is relative and monotonic, matching the way artists and directors naturally ask for a motion to be
      “a little more” or “a little less” expressive.
    </p>

    <div class="mss-points">
      <div class="mss-point">
        <strong>Continuous</strong>
        <span>One scalar controls smooth style intensity instead of selecting only discrete labels.</span>
      </div>
      <div class="mss-point">
        <strong>Endpoint-supervised</strong>
        <span>Training does not require ground-truth motions at every intermediate intensity.</span>
      </div>
      <div class="mss-point">
        <strong>Extrapolatable</strong>
        <span>The model supports controlled over-reaction beyond the observed style endpoint.</span>
      </div>
    </div>
  </section>

  <section class="mss-section">
    <h2>How it works</h2>
    <p>
      We represent the change from content motion to style motion as a direction in a learned motion-style embedding
      space. Moving along that direction with intensity \(\alpha\) creates the style condition for a pretrained motion
      diffusion denoiser. Diffusion training is combined with latent intensity regularization to encourage smooth,
      ordered changes while preserving the original action.
    </p>

    <figure class="mss-figure">
      <img
        src="{{ '/assets/img/motion-style-slider/method.png' | relative_url }}"
        alt="Motion Style Slider method pipeline."
        loading="lazy"
      >
      <figcaption>
        The model builds a style direction from endpoint motions, samples an intensity, and conditions the diffusion
        denoiser with separate content and style signals.
      </figcaption>
    </figure>
  </section>

  <section class="mss-section">
    <h2>Qualitative results</h2>
    <p>
      Across several motion-style datasets, the method aims to preserve the source action while changing expression
      predictably as the slider moves. Evaluation covers realism, content preservation, monotonicity, interpolation,
      and extrapolation to newly captured over-reaction targets.
    </p>

    <figure class="mss-figure">
      <img
        src="{{ '/assets/img/motion-style-slider/results.png' | relative_url }}"
        alt="Qualitative comparison of Motion Style Slider with motion style transfer baselines."
        loading="lazy"
      >
      <figcaption>
        Qualitative comparisons with representative motion-style transfer baselines at multiple style intensities.
      </figcaption>
    </figure>

    <figure class="mss-figure">
      <img
        src="{{ '/assets/img/motion-style-slider/cross-content.png' | relative_url }}"
        alt="Cross-content qualitative results for Motion Style Slider."
        loading="lazy"
      >
      <figcaption>
        Cross-content stylization examples showing the same style-control mechanism across different source motions.
      </figcaption>
    </figure>
  </section>

  <section class="mss-section">
    <h2>Citation</h2>
    <pre class="mss-citation"><code>@inproceedings{liao2026motionstyleslider,
  title     = {Motion Style Slider: Endpoint-Supervised Continuous
               Style Control for Human Motion Diffusion},
  author    = {Liao, Chen-Chieh and Peng, Yichen and Cai, Yiyi and
               Ono, Yûi and Hanaoka, Hiroki and Wu, Erwin and
               Koike, Hideki and Kurabayashi, Shuichi},
  booktitle = {European Conference on Computer Vision (ECCV)},
  year      = {2026}
}</code></pre>
  </section>
</div>
