const filters = document.querySelectorAll('.portfolio-filters li');

filters.forEach(filter => {
  filter.addEventListener('click', () => {
    const filterValue = filter.getAttribute('data-filter');

    // Active class to the selected filter
    filters.forEach(f => f.classList.remove('filter-active'));
    filter.classList.add('filter-active');

    // Filter portfolio items
    const items = document.querySelectorAll('.portfolio-item');
    items.forEach(item => {
      if (filterValue === '*' || item.classList.contains(filterValue.substring(1))) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  });
});