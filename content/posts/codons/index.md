---
title: "The Codon Map"
summary: "Which codons specify particular amino acids? To help memorize the codon to amino acid assignment, I created a new way of visualizing these relationships."
categories: ["Post","Blog",]
#tags: ["post","lorem","ipsum"]
#externalUrl: ""
showSummary: true
date: 2026-07-04
draft: false
showHero: true
heroStyle: background # basic, big, background, thumbAndBackground. Effective only if article.showHero = true.
layoutBackgroundBlur: true
layout: mod-single
---

{{< katex >}}

## Nucleotide Bases

The genetic code is the set of rules used by cells to translate nucleotide sequences into proteins. The code relies on the specific ordering of nitrogen-containing molecules called nucleotide bases. In DNA, these bases comprise Adenine (**$\ce{A}$**), Thymine (**$\ce{T}$**), Guanine (**$\ce{G}$**), and Cytosine (**$\ce{C}$**). Adenine and Guanine are both **purines** (a pyrimidine and an imidazole) while Cytosine and Thymine are both **pyrimidines**. 

{{< gallery title="Structure of nucleotide bases" >}}
  {{< lightbox src="nucleotides/190.png" gallery="nucleotide" caption="**A**denine" showCaptionBelow="true" >}}
  {{< lightbox src="nucleotides/1135.png" gallery="nucleotide" caption="**T**hymine (DNA)" showCaptionBelow="true" >}}
  {{< lightbox src="nucleotides/135398634.png" gallery="nucleotide" caption="**G**uanine" showCaptionBelow="true" >}}
  {{< lightbox src="nucleotides/597.png" gallery="nucleotide" caption="**C**ytosine" showCaptionBelow="true" >}}
  {{< lightbox src="nucleotides/1174.png" gallery="nucleotide" caption="**U**racil (RNA)" showCaptionBelow="true" >}}
{{< /gallery >}}

## Codons & Amino Acids

Hydrogen bonding between purines and pyrimidines form the standard base pairs **$\ce{A=T}$** (double bond) and **$\ce{G#C}$** (triple bond). During the process of transcription, DNA serves as the template to synthesize messenger RNA (mRNA), where Uracil (**$\ce{U}$**) replaces Thymine to pair with Adenine. The linear sequence of these bases is read sequentially by cellular machinery in discrete, non-overlapping *triplets* known as **codons**. 

{{< steps >}}
{{< step number="1" title="DNA to RNA (Transcription)" >}}RNA polymerase reads a specific gene on the DNA strand and builds a matching single-stranded copy called messenger RNA (mRNA). During this step, the RNA base uracil (U) replaces the DNA base thymine (T). The mRNA then leaves the nucleus and goes into the cytoplasm.{{< /step >}}

{{< step number="2" title="RNA to Amino Acids (Translation)" >}}The ribosome reads the mRNA code in groups of three bases called codons. Another molecule called transfer RNA (tRNA) brings the matching amino acids to the ribosome one by one. Each codon matches a specific amino acid.{{< /step >}}

{{< step number="3" title="Amino Acids to Proteins (Folding)" >}}The ribosome joins the amino acids together with peptide bonds into a long chain called a polypeptide. Once the chain is complete, it twists and folds into a complex, three-dimensional shape based on the traits of its amino acids. This finished shape becomes a working, functional protein.{{< /step >}}

{{< /steps >}}


{{< lightbox src="gallery/translate.png" gallery="rna" caption="Example sequence showing messenger RNA (mRNA) codons translated to amino acids." showCaptionBelow="true" size="300">}}

Replication: DNA makes exact copies of itself so cells can divide and pass instructions to new cells.Transcription: The cell copies a section of DNA into a messenger RNA (mRNA) molecule inside the nucleus. Translation: Ribosomes read the mRNA code to link amino acids together and build a functional protein.

Because there are four distinct bases (**$\ce{A}$**, **$\ce{T}$**, **$\ce{G}$**, and **$\ce{C}$**), three-base combinations yield **$4^3 = 64$** possible codons, where specific codons code for particular amino acids (or one of three stop codons). Since there are only **$20$** amino acids[^1], we say there is redundancy, or **degeneracy**, in the genetic code. In other words, multiple codons can map to a single amino acid. 

For example, **Glutamine (Gln)** is coded by $\ce{CAG}$ and $\ce{CAA}$ while **Histidine (His)** is coded by $\ce{CAC}$ and $\ce{CAU}$. In fact only methionine and tryptophan are specified by a single codon. The remaining amino acids are coded by at least two, and up to six, codons. Below is a lookup table that describes the relationship between codons and amino acids. 

{{< alert "link" >}}
Use this → link for [more detailed information about each amino acid](/posts/amino-acids).
{{< /alert >}}

{{< codon-table >}}

> [!note]
> Though the genetic code is degenerate (i.e., multiple codons may map to a single amino acid) the code **is not ambiguous**. In other words, a given codon always maps to exactly one amino acid

## Degeneracy & Nucleotide Ambiguity Codes 

To represent nucleotide degeneracy, or positions with more than one possible base in a codon, the [IUPAC](https://iupac.org/) (International Union of Pure & Applied Chemistry) defines single-letter nucleic acid ambiguity codes. Below is the complete list of the IUPAC nucleic acid ambiguity codes. 

```
    IUPAC Nucleic Acid Ambiguity Codes
    ------------------------------------
    R (Purines): A or G 
    Y (Pyrimidines): C or T/U 
    M (Amino): A or C 
    K (Keto): G or T/U 
    S (Strong): G or C 
    W (Weak): A or T/U 
    ------------------------------------
    H (not G): A, C, or T/U 
    B (not A): C, G, or T/U 
    V (not T/U): A, C, or G 
    D (not C): A, G, or T/U 
    ------------------------------------
    N (Any base): A, C, G, or T/U
```       

{{< alert >}}
Don't get confused here. The single letter nucleic acid ambiguity codes are not the same as single letter abbreviations for amino acids. 
{{< /alert >}}

Returning to the examples above, Glutamine (Gln) is coded by $\ce{CAG}$ and $\ce{CAA}$. Note that the third position of both codons is a **purine** ($\ce{G}$ or $\ce{A}$). Looking at the  nucleic acid ambiguity table above we see that the code for purines is $\ce{R}$. So we can say the Glutamine is coded by **$\ce{CAR}$**. Similarly, Histidine (His), which is coded by $\ce{CAC}$ and $\ce{CAU}$, can be rewritten as **$\ce{CAY}$**, where $\ce{Y}$ is a **pyrimidine**. If instead we reference the codon lookup table we see that Serine (Ser) is coded for by 6 different codons: $\ce{UCA}$, $\ce{UCG}$, $\ce{UCC}$, $\ce{UCU}$, $\ce{AGU}$, and $\ce{AGC}$. Applying the ambiguity codes, we say that Serine (Ser) is coded by **$\ce{UCN}$** and **$\ce{AGY}$**, where $\ce{N}$ stands for **any base** and $\ce{Y}$ corresponds to pyrimidine.

## Mapping Codons to Amino Acids

In addition to codon tables, other methods have been developed to show the mapping between codons and their cooresponding amino acids. Memorizing codon to amino acid assignments is not a mandatory skill but it can significantly speed up data analysis, enable quick error detection in sequences, and generally deepen your understanding of sequence analysis, all without constantly relying on reference charts or tables. 

Below are a few examples of different tools to show the relationship between codons and amino acids. The codon wheel for example is a circular chart where the inner ring is the first base of the three-letter codon. The middle ring is the second base, and the outer ring in the third base. The codon chart works similarly but also overlays additional information like amino acid properties (e.g., acidic, basic, etc.) and chemical structures. 

{{< gallery title="Popular methods to map codons to amino acids" >}}
  {{< lightbox src="gallery/codon_table.png" gallery="standard" caption="[Codon table](https://commons.wikimedia.org/wiki/File:Amino_Acid_Codon_Table.svg)" showCaptionBelow="true" size="160" >}}
  {{< lightbox src="gallery/codon_wheel.png" gallery="standard" caption="[Codon wheel](https://commons.wikimedia.org/wiki/File:Aminoacids_table.svg)" showCaptionBelow="true" size="160" >}}
  {{< lightbox src="gallery/codon_chart.png" gallery="standard" caption="[Codon chart](https://en.wikipedia.org/wiki/File:GeneticCode21.svg)" showCaptionBelow="true" size="160" >}}
  {{< lightbox src="gallery/codon_3d.jpg" gallery="standard" caption="[Codon 3D](https://commons.wikimedia.org/wiki/File:3D_Genetic_Code.jpg)" showCaptionBelow="true" size="160" >}}
{{< /gallery >}}

## A Better Map? 

{{< mermaid >}}
flowchart LR
    A(Cytosine) --> B(Adenine)
    
    %% 1. Subgraph Layout with Markdown Titles
    subgraph 1st_base ["`**1st base**`"]
      A("`**C**
       Cytosine`")
    end
    subgraph 2nd_base ["`**2nd base**`"]
      B("`**A**
       Adenine`")
    end
    subgraph 3rd_base ["`**3rd base**`"]
      C(Guanine)
      D(Adenine)
      E(Cytosine)
      F(Uracil)
    end
    
    B --> C("`**G**
     Guanine`")
    B --> D("`**A**
     Adenine`")
    B --> E("`**C**
     Cytosine`")
    B --> F("`**U**
     Uracil`")
    
    subgraph Amino_Acids ["`**Amino Acids**`"]
      C -- "`**R**`" --> G((("`**Gln**
      Glutamine`")))
      D -- "`**R**`" --> G
      E -- "`**Y**`" --> H((("`**His**
      Histidine`"))) 
      F -- "`**Y**`" --> H
    end 

    %% ==========================================
    %% NODE STYLING (REUSABLE CLASSES)
    %% ==========================================
    classDef largeFont font-size:22px;
    classDef mediumFont font-size:16px;
    
    class A,B,G,H largeFont;
    class C,D,E,F mediumFont;

    %% ==========================================
    %% SUBGRAPH BOX STYLING
    %% ==========================================
    %% Syntax: style [subgraph_id] CSS_properties
    style 1st_base fill:currentColor,fill-opacity:0.07,stroke:currentColor,stroke-opacity:0.3,stroke-width:1px;
    style 2nd_base fill:currentColor,fill-opacity:0.07,stroke:currentColor,stroke-opacity:0.3,stroke-width:1px;
    style 3rd_base fill:none,stroke:none;
    style Amino_Acids fill:currentColor,fill-opacity:0.12,stroke:currentColor,stroke-opacity:0.5,stroke-width:2px;

    %% ==========================================
    %% LINK & ARROW TEXT STYLING
    %% ==========================================
    %% Edges are numbered sequentially (0, 1, 2...) in order of code appearance.
    %% Edges 0 through 4 handle the top layout branching rules.
    %% Edges 5 through 8 map the R and L paths inside Amino Acids.
    
    linkStyle 5 font-size:24px,font-weight:bold,fill:none;
    linkStyle 6 font-size:24px,font-weight:bold,fill:none;
    linkStyle 7 font-size:24px,font-weight:bold,fill:none;
    linkStyle 8 font-size:24px,font-weight:bold,fill:none;
{{< /mermaid >}}


I tried forever to memorize codon assignments using the tools described above with little luck--it just wouldn't stick. If you are more of a visual learner like me, then tables are pretty useless. I tried the various wheel and chart representations but those didn't help either. 


{{< lightbox src="gallery/codons.png" gallery="codons" caption="Codon Trees" showCaptionBelow="false" size="650">}}


{{< gallery title="Conventional methods to map codons to amino acids" >}}
  {{< lightbox src="gallery/G.png" gallery="codons" caption="Codon Tree 5' G" showCaptionBelow="true"  size="140" >}}
  {{< lightbox src="gallery/C.png" gallery="codons" caption="Codon Tree 5' C" showCaptionBelow="true"  size="140" >}}
  {{< lightbox src="gallery/A.png" gallery="codons" caption="Codon Tree 5' A" showCaptionBelow="true"  size="140" >}}
  {{< lightbox src="gallery/U.png" gallery="codons" caption="Codon Tree 5' U" showCaptionBelow="true"  size="140" >}}
{{< /gallery >}}


[^1]: In this artcile I discuss the *standard genetic code* but it is important to note that there are [several variant translation systems](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi) used in certain organelles and microbes.  Alternative genetic codes are variant translation systems where specific codons are reassigned to encode different amino acids or stop signals. 

