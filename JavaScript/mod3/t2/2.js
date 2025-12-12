const targetElement = document.getElementById('target');
const itemContents = ["First item", "Second item", "Third item"];

for (let i = 0; i < itemContents.length; i++) {
    const listItem = document.createElement('li');
    listItem.textContent = itemContents[i];

    if (i === 1) {
        listItem.classList.add('my-item');
    }

    targetElement.appendChild(listItem);
}