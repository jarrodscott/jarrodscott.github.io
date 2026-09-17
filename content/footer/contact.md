---
title: "Contact Form"
layout: "simple"
menu: "footer"
weight: 10
---


<!-- Parent layout -->
<div class="flex flex-col lg:flex-row gap-4 w-full items-start">

  <!-- 1/3 Left Column -->
  <div class="w-full" style="flex: 1;">
    <h2 class="text-3xl font-bold mb-4">Get in touch</h2>
    <p class="text-neutral-600 dark:text-neutral-400">I would love to hear from you. Please fill out the form and I will get back to you as soon as possible.</p>

  </div>

  <!-- 2/3 Right Column -->
  <div class="w-full" style="flex: 2;">
    {{< contact-form key="607b3c0a-1f34-4c09-b449-648d7f010c09" redirect="thank-you/" description="Have a question or want to work together? Drop me a line and I'll get back to you within **24 hours**." >}}
  </div>

</div>

{{< contact-form key="607b3c0a-1f34-4c09-b449-648d7f010c09" redirect="thank-you/" description="Have a question or want to work together? Drop me a line and I'll get back to you within **24 hours**." >}}
