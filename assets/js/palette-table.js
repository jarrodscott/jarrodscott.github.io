function copyColorText(text, element) {
  navigator.clipboard.writeText(text).then(() => {
    const textSpan = element.querySelector('.btn-text');
    if (textSpan) {
      const originalText = textSpan.innerText;
      textSpan.innerText = "Copied!";
      element.classList.add("!border-green-500", "text-green-600", "dark:text-green-400");
      setTimeout(() => {
        textSpan.innerText = originalText;
        element.classList.remove("!border-green-500", "text-green-600", "dark:text-green-400");
      }, 1500);
    } else {
      const originalText = element.innerText;
      element.innerText = "✓";
      element.classList.add("text-green-500");
      setTimeout(() => {
        element.innerText = originalText;
        element.classList.remove("text-green-500");
      }, 1500);
    }
  }).catch((err) => {
    console.error('Could not copy color list: ', err);
  });
}
