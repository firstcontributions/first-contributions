const searchInput = document.getElementById('search');
const contributors = document.querySelectorAll('.contributor');
const count = document.getElementById('count');

function updateCount() {
  count.textContent = contributors.length;
}

// Show total contributors on page load
updateCount();

searchInput.addEventListener('keyup', () => {
  const query = searchInput.value.toLowerCase();
  contributors.forEach(item => {
    if (item.textContent.toLowerCase().includes(query)) {
      item.style.display = 'list-item';
    } else {
      item.style.display = 'none';
    }
  });
});
