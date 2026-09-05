function filterPublications() {
  const selectedType = document.getElementById('typeFilter').value;
  const selectedTag = document.getElementById('tagFilter').value;
  const publicationItems = document.querySelectorAll('.publication-item');
  const yearGroups = document.querySelectorAll('.year-group');
  const noPubsMessage = document.getElementById('noPubsMessage');
  
  let totalVisibleCount = 0;

  publicationItems.forEach(item => {
    const itemType = item.getAttribute('data-pubtype');
    const rawTags = item.getAttribute('data-tags') || '';
    const itemTags = rawTags.trim().split(/\s+/);

    const matchType = (selectedType === 'all' || itemType === selectedType);
    const matchTag = (selectedTag === 'all' || itemTags.includes(selectedTag));

    if (matchType && matchTag) {
      item.style.display = 'block';
      totalVisibleCount++;
    } else {
      item.style.display = 'none';
    }
  });

  yearGroups.forEach(group => {
    const allItemsInGroup = group.querySelectorAll('.publication-item');
    let visibleInGroup = 0;
    
    allItemsInGroup.forEach(item => {
      if (item.style.display !== 'none') {
        visibleInGroup++;
      }
    });

    if (visibleInGroup === 0) {
      group.style.display = 'none';
    } else {
      group.style.display = 'block';
    }
  });

  if (totalVisibleCount === 0) {
    noPubsMessage.classList.remove('hidden');
  } else {
    noPubsMessage.classList.add('hidden');
  }
}

