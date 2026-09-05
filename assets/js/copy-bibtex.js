function copyBibTeX(button) {
  const encodedBib = button.getAttribute('data-bibtex');
  if (!encodedBib) return;
  const parser = new DOMParser();
  const doc = parser.parseFromString(encodedBib, 'text/html');
  const bibtex = doc.documentElement.textContent;
  const textLabel = button.querySelector('.cite-text');
  
  navigator.clipboard.writeText(bibtex).then(() => {
    const originalText = textLabel.textContent;
    textLabel.textContent = 'COPIED!';
    button.classList.add('text-emerald-600', 'dark:text-emerald-400');
    setTimeout(() => { 
      textLabel.textContent = originalText; 
      button.classList.remove('text-emerald-600', 'dark:text-emerald-400');
    }, 2000);
  }).catch(err => { console.error('Clipboard copy failed: ', err); });
}