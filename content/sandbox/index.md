---
title: "Sandbox"
description: "A place to play."
showHero: true
heroStyle: background # basic, big, background, thumbAndBackground. Effective only if article.showHero = true.
layoutBackgroundBlur: true
draft: true
showPagination: false
---

{{< katex >}}

## feature-grid

{{< feature-grid columns="3" >}}
{{< feature icon="wand-magic-sparkles" title="Make it yours" url="/docs/configuration/" >}}
Start from a thoughtful default, then adjust every meaningful detail.
{{< /feature >}}
{{< feature icon="file-lines" title="Publish faster" url="/docs/shortcodes/" label="Browse shortcodes" >}}
Compose rich content with small, reusable building blocks.
{{< /feature >}}
{{< feature icon="heart" title="Built for people" >}}
Accessible defaults, responsive layouts, and dark mode included.
{{< /feature >}}
{{< /feature-grid >}}

## Stats

{{< stats >}}
{{< stat value="40+" label="Shortcodes" >}}Compose pages without bespoke templates.{{< /stat >}}
{{< stat value="100%" label="Portable" >}}Keep your content in Markdown.{{< /stat >}}
{{< stat value="0" label="Required plugins" >}}Start with Hugo and Blowfish.{{< /stat >}}
{{< /stats >}}

## Steps

{{< steps >}}
{{< step number="1" title="Configure the theme" >}}Choose a colour scheme and homepage layout.{{< /step >}}
{{< step number="2" title="Write your content" >}}Use standard Markdown and shortcodes.{{< /step >}}
{{< /steps >}}

## Lead

{{< lead >}}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in eleifend justo, vestibulum congue lacus. Quisque est libero, lacinia sed placerat ac, interdum id urna. Nulla venenatis volutpat libero, in laoreet leo fringilla eget. Etiam consequat sed nisi sit amet interdum. Pellentesque ullamcorper at turpis in ultrices. Pellentesque et elit mauris. Aenean eu augue sit amet nunc interdum ultricies. Aenean eleifend consectetur sapien vitae consectetur. Donec risus mauris, finibus at condimentum at, lacinia sit amet neque. Nulla facilisi. Suspendisse sollicitudin dolor quis eros tempor, a tempus ex varius.
{{< /lead >}}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in eleifend justo, vestibulum congue lacus. Quisque est libero, lacinia sed placerat ac, interdum id urna. Nulla venenatis volutpat libero, in laoreet leo fringilla eget. Etiam consequat sed nisi sit amet interdum. Pellentesque ullamcorper at turpis in ultrices. Pellentesque et elit mauris. Aenean eu augue sit amet nunc interdum ultricies. Aenean eleifend consectetur sapien vitae consectetur. Donec risus mauris, finibus at condimentum at, lacinia sit amet neque. Nulla facilisi. Suspendisse sollicitudin dolor quis eros tempor, a tempus ex varius.


## CTA

{{< cta url="/docs/installation/" label="Start building" >}}
{{< cta url="/docs/configuration/" label="Explore configuration" style="outline" >}}


{{< button href="#button" target="_self" >}}
Call to action
{{< /button >}}



## mermaid mind map

{{< mermaid >}}
mindmap
  root((**Guanine**))
    (Guanine)
      Guanine
      Cytosine
      Adenine
      Uracil
    (Cytosine)
      Guanine
      Cytosine
      Adenine
      Uracil
    (Adenine)
      Guanine
      Cytosine
      Adenine
      Uracil
    (Uracil)
      Guanine
      Cytosine
      Adenine
      Uracil
{{< /mermaid >}}

## Rendering Chemistry & Math equations

### Math

https://katex.org/docs/supported.html

Inline equation: $\varphi = \\frac{1+\\sqrt{5}}{2}$

Block equation:
$$ f(a,b,c) = (a^2+b^2+c^2)^3 $$

$$
e^{x} = \sum_{n=0}^{\infty} \frac{x^n}{n!}
$$

Fibonacci primes:  233, 1597, 28657, 514229, 433494437, 2971215073, ....

### Chemistry

https://mhchem.github.io/MathJax-mhchem/

block chemistry 

$$\ce{C6H12O6 + 6O2 -> 6CO2 + 6H2O}$$

Inline chemistry: $\ce{H2O}$.

Physical Units: Use $\pu{274.15 K}$ or $\pu{--10 kJmol-1}$ via the `\pu` command.

## Fetching structures

python scripts/generate_structures.py --cids 190 597 135398634 1135 1174 --output_dir content/posts/codons/nucleotides/

python scripts/generate_structures.py --cids 5950 6322 6267 5960 5862 33032 5961 750 6274 6306 6106 5962 6137 6140 145742 5951 6288 6305 6057 6287 --output_dir content/posts/codons/amino_acids/

Standard Amino Acids and PubChem CIDs    
Alanine (Ala / A): CID 5950    
Arginine (Arg / R): CID 6322    
Asparagine (Asn / N): CID 6267    
Asparatic Acid (Asp / D): CID 5960    
Cysteine (Cys / C): CID 5862    
Glutamic Acid (Glu / E): CID 33032    
Glutamine (Gln / Q): CID 5961    
Glycine (Gly / G): CID 750    
Histidine (His / H): CID 6274    
Isoleucine (Ile / I): CID 6306    
Leucine (Leu / L): CID 6106    
Lysine (Lys / K): CID 5962    
Methionine (Met / M): CID 6137    
Phenylalanine (Phe / F): CID 6140    
Proline (Pro / P): CID 145742    
Serine (Ser / S): CID 5951    
Threonine (Thr / T): CID 6288    
Tryptophan (Trp / W): CID 6305    
Tyrosine (Tyr / Y): CID 6057    
Valine (Val / V): CID 6287    
    
    
python scripts/generate_structures.py --cids  6089 4980 10624 1832 10257 6090 15429212 9991554 --output_dir content/posts/hallucinogens/typtamines/

Tryptamine  (2-(3-indolyl)ethylamine): PubChem CID 1150    
Serotonin (5-hydroxytryptamine (5-HT)):  PubChem CID 5202    

DMT (N,N-Dimethyltryptamine): PubChem CID 6089    
Psilocin (4-HO-DMT): PubChem CID 4980    
Psilocybin (4-PO-DMT): PubChem CID 10624    
5-MeO-DMT (5-Methoxy-N,N-dimethyltryptamine): PubChem CID 1832    
Bufotenin (5-HO-DMT): PubChem CID 10257    
DET (N,N-Diethyltryptamine): PubChem CID 6090    
4-AcO-DMT (O-Acetylpsilocin): PubChem CID 15429212    
4-HO-DET (Ethocin): PubChem CID 9991554    

## Adding citations & bibliography

Recent findings show that code automation increases site speed {{< cite "anandPatternProcessMechanism1994" "p" >}}. However, alternative views suggest otherwise {{< cite "balchAncientDivergenceBacteria1977" "n" >}}.

I believe for this to work you need a file called `data/references.json`

{{< bibliography >}}

[{{< gallery >}}
  {{< molecule cid="6089" name="DMT" size="200" >}}
  {{< molecule cid="996" name="phenol" size="200" >}}
  {{< molecule cid="2244" name="asperin" size="200" >}}
  {{< molecule cid="2244" name="asperin" size="200" >}}
  {{< molecule cid="2244" name="asperin" size="200" >}}
  {{< molecule cid="2244" name="asperin" size="200" >}}
  {{< molecule cid="2244" name="asperin" size="200" >}}
{{< /gallery >}}]: # 

## My Photo Gallery

### 4-Column Layout (Manual Control)

{{< gallery >}}
  {{< lightbox src="gallery/banner1.jpg" gallery="vacation" caption="Wide view"  ratio="2/3" >}}
  {{< lightbox src="gallery/mindmap.jpg" gallery="vacation" caption="Map zoom" >}}
  {{< lightbox src="gallery/old_garden_01.jpg" gallery="vacation" caption="Detail 1" >}}
  {{< lightbox src="gallery/some_bar.jpg" gallery="vacation" caption="Photo by Jane Doe">}}
{{< /gallery >}}


{{< gallery >}}
  {{< lightbox src="gallery/DSC2464.jpg" gallery="vacation" caption="Wide view" ratio="16/9" >}}
  {{< lightbox src="gallery/mindmap.jpg" gallery="vacation" caption="Square zoom" ratio="1/1" >}}
  {{< lightbox src="gallery/old_garden_01.jpg" gallery="vacation" caption="Classic view" ratio="4/3" >}}
  {{< lightbox src="gallery/some_bar.jpg" gallery="vacation" caption="Tall portrait" ratio="2/3" >}}
{{< /gallery >}}

###  (Automated Folder Dump)
{{< gallery-folder dir="gallery" name="panoramas" title="Panoramic Landscapes" >}}

</br>
{{< lightbox src="gallery/some_bar.jpg" gallery="standard" caption="[Codon chart](https://en.wikipedia.org/wiki/File:GeneticCode21.svg)" >}}

## Footnotes

This is a footnote[^1]. 
[^1]: This is the text of the footnote that will appear at the bottom of the page.


## Creative commons

get more icons here https://creativecommons.org/mission/downloads/

- {{< cc "by-nc-sa" >}}

- {{< cc "by" >}}
Attribution Only Allows: Sharing, remixing, and commercial use.

- {{< cc "by-sa" >}}
Attribution-Share Alike Allows: Remixes must use the exact same license terms.

- {{< cc "by-nc" >}}
Attribution-NonCommercial Allows: Reuse, but no one can profit off your work.

{{< cc "by-nc-sa" >}}
Attribution-NonCommercial-Share Alike Allows: Non-commercial reuse with matching license terms.

{{< cc "by-nd" >}}
Attribution-No Derivatives Allows: Distribution, but no one can edit or remix your work.

{{< cc "by-nc-nd" >}}
Attribution-NonCommercial-No Derivatives Allows: Most restrictive option. Only allows downloads and basic sharing.

{{< cc "cc0" >}}
Public Domain DedicationAllows: Waives all worldwide copyright protections completely

{{< button pageRef="/research-portfolio/publications" >}}
Complete list of my publications
{{< /button >}}

<!--
Please see →  {{< link url="/research-portfolio/publications" text="this link for a complete list of my publications" >}}.

{{< alert "link" >}}
Use this → link so see all of [my publications](/research-portfolio/publications).
{{< /alert >}}

Code like so {{< link url="http://doi.org/10.37807/GBMF5603" text="SOME TEXT" >}}

> [!note]
> Use this → link so see all of [my publications](/research-portfolio/publications).

-->

## auto bibliography from BibBase

<script src="https://bibbase.org/show?bib=https%3A%2F%2Fbibbase.org%2Fnetwork%2Ffiles%2FJg2yAnnyYmxQdGzEF&noBootstrap=1&jsonp=1"></script>

