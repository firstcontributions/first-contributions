function createCard(contributor) {
    const iframe = document.createElement('iframe');
    iframe.className = 'card col col-6-md col-3-lg bd-grey';
    iframe.src = `contributors/${contributor}`;
    iframe.title = contributor
    document.getElementById('contributor-cards').appendChild(iframe);
}

contributorFiles.forEach(contributor => createCard(contributor));
