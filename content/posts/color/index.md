---
title: "Accessible Color Palettes for Data Visualization"
summary: "High-contrast color palettes that help make figures accessible to all types of people."
description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
categories: ["Post","Blog",]
#tags: ["post","lorem","ipsum"]
#externalUrl: ""
showSummary: true
#date: 2026-07-02
draft: false
showHero: true
heroStyle: background # basic, big, background, thumbAndBackground. Effective only if article.showHero = true.
layoutBackgroundBlur: true
layout: mod-single
weight: -20
---

I spend a lot of time thinking about color and how I can use color to convey a message. For example, if you use too many colors in a figure you force your reader to continually go back and forth from the chart to the legend. This can be confusing and ultimately may detract from the meaning of the figure {{< cite "liptoninformationdesign2007 rolandiBriefGuideDesigning2011" "p" >}}.  

Another point to consider is that many of us have different abilities to **perceive** color and/or **detect** differences in color {{< cite "deebMolecularBasisVariation2005" "p" >}}. Color blindness, also known as **color vision deficiency**, is the decreased ability to see color or differences in color. When designing figures, it is important to use **a**) a relatively small color palette and **b**) a palette that is friendly to a variety of people. If you want to test yourself for color blindness, search for  **Ishihara Test**--there are many sites that offer interactive tests. 

For more information on the topic, I recommend reading Bang Wong’s Nature Methods paper, [Points of view: Color blindness](http://dx.doi.org/10.1038/nmeth.1618). Wong proposes a color-blind friendly color palette that uses contrasting colors that can be distinguished by a range of people {{< cite "wongPointsViewColor2011" "p" >}}. Consider that roughly 8% of people (mostly males) are color blind. So, what do you think? Do you want Keanu Reeves to understand your figures or not? If so, consider a color scheme that is friendly to all vision types

## Wong's 8-color palette

{{< swatches "#000000" "#0072B2" "#56B4E9" "#CC79A7" "#009E73" "#D55E00" "#E69F00" "#F0E442" >}}

Wong’s scheme is conservative---there are only 8 colors. Limited color palettes like these force us to be more careful when deciding what information to target or how many groups to display. 


{{< palette-table colors=`[
  {"name": "Black", "hex": "#000000", "rgb": "rgb(0, 0, 0)"},
  {"name": "Blue", "hex": "#0072B2", "rgb": "rgb(0, 114, 178)"},
  {"name": "Sky Blue", "hex": "#56B4E9", "rgb": "rgb(0, 114, 178)"},
  {"name": "Reddish Purple", "hex": "#CC79A7", "rgb": "rgb(204, 121, 167)"},
  {"name": "Bluish Green", "hex": "#009E73", "rgb": "rgb(0, 158, 115)"},
  {"name": "Vermillion", "hex": "#D55E00", "rgb": "rgb(213, 94, 0)"},
  {"name": "Orange", "hex": "#E69F00", "rgb": "rgb(230, 159, 0)"},
  {"name": "Yellow", "hex": "#F0E442", "rgb": "rgb(240, 228, 66)"}
]` >}}

## Wong's 8-color palette (Krzywinski modified)

In addition to an incredible talent for data visualization, [Martin Krzywinski](https://mk.bcgsc.ca) has an excellent post on [designing color blind friendly palettes](https://mk.bcgsc.ca/colorblind/). This post provides an in-depth explanation of on the physics and physiology behind color blindness, plus provides code for several different palette options, including a [modified version of Wong's palette](https://mk.bcgsc.ca/colorblind/palettes.mhtml#conservative-8-color-palette-for-colorbliness). 

{{< tabs >}}

  {{< tab label="Primary Palette" md=false >}}
  </br>
{{< swatches "#000000" "#2271B2" "#3DB7E9" "#F748A5" "#359B73" "#D55E00" "#E69F00" "#F0E442" >}}

{{< palette-table colors=`[
  {"name": "Black", "hex": "#000000", "rgb": "rgb(0, 0, 0)"},
  {"name": "Sapphire Blue", "hex": "#2271B2", "rgb": "rgb(34, 113, 178)"},
  {"name": "Cyan", "hex": "#3DB7E9", "rgb": "rgb(61, 183, 233)"},
  {"name": "Magenta", "hex": "#F748A5", "rgb": "rgb(247, 72, 165)"},
  {"name": "Sea  Green/Viridian", "hex": "#359B73", "rgb": "rgb(53, 155, 115)"},
  {"name": "Burnt Orange", "hex": "#D55E00", "rgb": "rgb(213, 94, 0)"},
  {"name": "Marigold", "hex": "#E69F00", "rgb": "rgb(230, 159, 0)"},
  {"name": "Lemon Yellow", "hex": "#F0E442", "rgb": "rgb(240, 228, 66)"}
]` >}}
  {{< /tab >}}

  {{< tab label="Secondary Palette" md=false >}}
  </br>
{{< swatches "#000000" "#AA0DB4" "#FF54ED" "#00B19F" "#EB057A" "#F8071D" "#FF8D1A" "#9EFF37" >}}  
{{< palette-table colors=`[
  {"name": "Black", "hex": "#000000", "rgb": "rgb(0, 0, 0)"},
  {"name": "Strong Magenta", "hex": "#AA0DB4", "rgb": "rgb(170, 13, 180)"},
  {"name": "Violet Pink", "hex": "#FF54ED", "rgb": "rgb(255, 84, 237)"},
  {"name": "Persian Green", "hex": "#00B19F", "rgb": "rgb(0, 177, 159)"},
  {"name": "Mexican Pink", "hex": "#EB057A", "rgb": "rgb(235, 5, 122)"},
  {"name": "ku Crimson", "hex": "#F8071D", "rgb": "rgb(248, 7, 29)"},
  {"name": "Tangerine", "hex": "#FF8D1A", "rgb": "rgb(255, 141, 26)"},
  {"name": "French Lime", "hex": "#9EFF37", "rgb": "rgb(158, 255, 55)"}
]` >}}
  {{< /tab >}}
{{< /tabs >}}

## Krzywinski's 12-Color Palette

[Martin Krzywinski](http://mkweb.bcgsc.ca/) also provides [a 12 color palette](https://mk.bcgsc.ca/colorblind/palettes.mhtml#12-color-palette-for-colorbliness) that offer more options than Wong's palette. Just be careful—-figures with too many colors can inhibit our ability to discern patterns. 

{{< tabs >}}
  {{< tab label="Primary Palette" md=false >}}
  </br>
{{< swatches "#9F0162" "#009F81" "#FF5AAF" "#00FCCF" "#8400CD" "#008DF9"  >}}
</br> 
{{< swatches  "#00C2F9" "#FFB2FD" "#A40122" "#E20134" "#FF6E3A" "#FFC33B" >}}  

{{< palette-table colors=`[
  {"name": "Jazzberry Jam", "hex": "#9F0162", "rgb": "rgb(159, 1, 98)"},
  {"name": "Jungle Green", "hex": "#009F81", "rgb": "rgb(0, 159, 129)"},
  {"name": "Brilliant Rose", "hex": "#FF5AAF", "rgb": "rgb(255, 90, 175)"},
  {"name": "Aqua Marine", "hex": "#00FCCF", "rgb": "rgb(0, 252, 207)"},
  {"name": "Blue Violet", "hex": "#8400CD", "rgb": "rgb(132, 0, 205)"},
  {"name": "Dodger Blue", "hex": "#008DF9", "rgb": "rgb(0, 141, 249)"},
  {"name": "Deep Sky Blue", "hex": "#00C2F9", "rgb": "rgb(0, 194, 249)"},
  {"name": "Plum", "hex": "#FFB2FD", "rgb": "rgb(255, 178, 253)"},
  {"name": "Scarlett", "hex": "#A40122", "rgb": "rgb(164, 1, 34)"},
  {"name": "Imperial Red", "hex": "#E20134", "rgb": "rgb(226, 1, 52)"},
  {"name": "Pinkish Orange", "hex": "#FF6E3A", "rgb": "rgb(255, 110, 58)"},
  {"name": "Goldenrod", "hex": "#FFC33B", "rgb": "rgb(255, 195, 59)"}      
]` >}}
  {{< /tab >}}

  {{< tab label="Secondary Palette" md=false >}}
  </br>
{{< swatches "#006A5E" "#ED0D88" "#00BDA9" "#FFC4D4" "#0058CC" "#D208FB" >}}
</br>  
{{< swatches "#FF66FD" "#00EFF9" "#156D03" "#009719" "#00C61B" "#00FB1D" >}}  

{{< palette-table colors=`[
  {"name": "Teal Green", "hex": "#006A5E", "rgb": "rgb(0, 106, 94)"},
  {"name": "Mexican Pink", "hex": "#ED0D88", "rgb": "rgb(237, 13, 136)"},
  {"name": "Turquoise", "hex": "#00BDA9", "rgb": "rgb(0, 189, 169)"},
  {"name": "Pale Crimson", "hex": "#FFC4D4", "rgb": "rgb(255, 196, 212)"},
  {"name": "Cerulean Blue", "hex": "#0058CC", "rgb": "rgb(0, 88, 204)"},
  {"name": "Electric Purple", "hex": "#D208FB", "rgb": "rgb(210, 8, 251)"},
  {"name": "Violet Pink", "hex": "#FF66FD", "rgb": "rgb(255, 102, 253)"},
  {"name": "Cyan", "hex": "#00EFF9", "rgb": "rgb(0, 239, 249)"},
  {"name": "Japanese Laurel", "hex": "#156D03", "rgb": "rgb(21, 109, 3)"},
  {"name": "Islamic Green", "hex": "#009719", "rgb": "rgb(0, 151, 25)"},
  {"name": "Vivid Malachite ", "hex": "#00C61B", "rgb": "rgb(0, 198, 27)"},
  {"name": "Radioactive Green", "hex": "#00FB1D", "rgb": "rgb(0, 251, 29)"}      
]` >}}
  {{< /tab >}}
{{< /tabs >}}
    
## Krzywinski's 15-Color Palette

And finally again from Martin Krzywinski, [a 15 color palette](https://mk.bcgsc.ca/colorblind/palettes.mhtml#15-color-palette-for-colorbliness). 


{{< tabs >}}
  {{< tab label="Primary Palette" md=false >}}
  </br>
{{< swatches "#68023F" "#008169" "#EF0096" "#00DCB5" "#FFCFE2" "#003C86" "#9400E6" "#009FFA" >}}
</br>  
{{< swatches "#FF71FD" "#7CFFFA" "#6A0213" "#008607" "#F60239" "#00E307" "#FFDC3D" >}}  

{{< palette-table colors=`[
  {"name": "Mulberry", "hex": "#68023F", "rgb": "rgb(104, 2, 63)"},
  {"name": "Deep Sea", "hex": "#008169", "rgb": "rgb(0, 129, 105)"},
  {"name": "Persian Rose", "hex": "#EF0096", "rgb": "rgb(239, 0, 150)"},
  {"name": "Aquamarine", "hex": "#00DCB5", "rgb": "rgb(0, 220, 181)"},
  {"name": "Azalea", "hex": "#FFCFE2", "rgb": "rgb(255, 207, 226)"},
  {"name": "Royal Blue", "hex": "#003C86", "rgb": "rgb(0, 60, 134)"},
  {"name": "Vivid Purple", "hex": "#9400E6", "rgb": "rgb(148, 0, 230)"},
  {"name": "Azure", "hex": "#009FFA", "rgb": "rgb(0, 159, 250)"},
  {"name": "Blush Pink", "hex": "#FF71FD", "rgb": "rgb(255, 113, 253)"},
  {"name": "Electric Blue", "hex": "#7CFFFA", "rgb": "rgb(124, 255, 250)"},
  {"name": "Burnt Crimson", "hex": "#6A0213", "rgb": "rgb(106, 2, 19)"},
  {"name": "India Green", "hex": "#008607", "rgb": "rgb(0, 134, 7)"},
  {"name": "Electric Crimson", "hex": "#F60239", "rgb": "rgb(246, 2, 57)"},
  {"name": "Radioactive Green", "hex": "#00E307", "rgb": "rgb(0, 227, 7)"},
  {"name": "Bright Sun", "hex": "#FFDC3D", "rgb": "rgb(255, 220, 61)"}   
]` >}}
  {{< /tab >}}

  {{< tab label="Secondary Palette" md=false >}}
  </br>
{{< swatches "#00463C" "#C00B6F" "#00A090" "#FF95BA" "#5FFFDE" "#590A87" "#0063E5" "#ED0DFD" >}}
</br>  
{{< swatches "#00C7F9" "#FFD5FD" "#3D3C04" "#C80B2A" "#00A51C" "#FFA035" "#9BFF2D" >}}  

{{< palette-table colors=`[
  {"name": "Aqua Deep", "hex": "#00463C", "rgb": "rgb(0, 70, 60)"},
  {"name": "Magenta", "hex": "#C00B6F", "rgb": "rgb(192, 11, 111)"},
  {"name": "Manganese Blue", "hex": "#00A090", "rgb": "rgb(0, 160, 144)"},
  {"name": "Tickle Me Pink", "hex": "#FF95BA", "rgb": "rgb(255, 149, 186)"},
  {"name": "Brilliant Turquoise", "hex": "#5FFFDE", "rgb": "rgb(95, 255, 222)"},
  {"name": "Indigo", "hex": "#590A87", "rgb": "rgb(89, 10, 135)"},
  {"name": "Cerulean Blue", "hex": "#0063E5", "rgb": "rgb(0, 99, 229)"},
  {"name": "Fuchsia", "hex": "#ED0DFD", "rgb": "rgb(237, 13, 253)"},
  {"name": "Deep Sky Blue", "hex": "#00C7F9", "rgb": "rgb(0, 199, 249)"},
  {"name": "Pale Lavender", "hex": "#FFD5FD", "rgb": "rgb(255, 213, 253)"},
  {"name": "Bronzetone", "hex": "#3D3C04", "rgb": "rgb(61, 60, 4)"},
  {"name": "Fire Engine Red", "hex": "#C80B2A", "rgb": "rgb(200, 11, 42)"},
  {"name": "Islamic Green", "hex": "#00A51C", "rgb": "rgb(0, 165, 28)"},
  {"name": "Sunshade", "hex": "#FFA035", "rgb": "rgb(255, 160, 53)"},
  {"name": "Acid Green", "hex": "#9BFF2D", "rgb": "rgb(155, 255, 45)"}
]` >}}
  {{< /tab >}}
{{< /tabs >}}

{{< bibliography >}}