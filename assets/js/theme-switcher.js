(() => {
  const initPicker = () => {
    const desktopPicker = document.getElementById("theme-picker-select");
    const mobilePicker = document.getElementById("theme-picker-select-mobile");
    if (!desktopPicker && !mobilePicker) return;

    const schemeRegistry = {};
    document.querySelectorAll(".raw-scheme-data").forEach((el) => {
      const name = el.getAttribute("data-scheme").trim();
      const cssText = el.getAttribute("data-css") || "";
      const variables = {};
      const regex = /(--color-[a-zA-Z0-9-]+)\s*:\s*([^;}\n]+)/g;
      let match;
      while ((match = regex.exec(cssText)) !== null) {
        variables[match[1].trim()] = match[2].trim();
      }
      schemeRegistry[name] = variables;
    });

    let styleTag = document.getElementById("runtime-theme-picker-override");
    if (!styleTag) {
      styleTag = document.createElement("style");
      styleTag.id = "runtime-theme-picker-override";
      document.head.appendChild(styleTag);
    }

    function apply(name) {
      if (!name || name === "default" || !schemeRegistry[name]) {
        styleTag.textContent = "";
        localStorage.removeItem("custom-color-scheme");
        return;
      }
      let cssString = "";
      for (const [k, v] of Object.entries(schemeRegistry[name])) {
        cssString += `${k}: ${v} !important;\n`;
      }
      styleTag.textContent = `:root, html, body, html.dark :root, html:not(.dark) :root { ${cssString} }`;
      localStorage.setItem("custom-color-scheme", name);
    }

    const saved = localStorage.getItem("custom-color-scheme") || "default";
    if (desktopPicker) desktopPicker.value = saved;
    if (mobilePicker) mobilePicker.value = saved;
    apply(saved);

    const sync = (e) => {
      const val = e.target.value;
      if (desktopPicker) desktopPicker.value = val;
      if (mobilePicker) mobilePicker.value = val;
      apply(val);
    };

    if (desktopPicker) desktopPicker.addEventListener("change", sync);
    if (mobilePicker) mobilePicker.addEventListener("change", sync);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initPicker);
  } else {
    initPicker();
  }
})();
