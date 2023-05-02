let renderUser = async () => {
    let response = await fetch('http://127.0.0.1:8000/api-blog/')
    let userData = await response.json()
    let html = ''
    // now data.author.image is working fine bcz after deleting old users those who don't have profile page
    // now need to add condition that if content image is not set than no need to show it
    userData.slice().reverse().forEach(data => {
        let htmlSegment = `<article class="media content-section">
                                <div class="media d-flex">
                                    <img class="rounded-circle account-img" src="${ data.author_profile.image }">
                                    <div class="media-body">
                                        <div class="article-metadata">
                                            <a class="mr-2" href="#">Author : ${ data.author }</a>
                                            <small class="text-muted">Date : ${ data.date_blog }</small>
                                        </div>
                                        <h2><a class="article-title" href="http://127.0.0.1:8000/blog/${ data.id }">Blog Title : ${ data.title }</a></h2>
                                        <p class="article-content">Description : ${ data.des }</p>
                                        <p class="article-content">Content : ${ data.content }</p>
                                        <p><img class="rounded-circle account-img" src="${ data.image }"></p>
                                        <p>All tags :
                                            ${data.tags.map(tag => `<span class="me-2">${ tag.tag }</span>`).join('')}
                                        </p>
                                    </div>
                                </div>
                            </article>`;
    
        html += htmlSegment;
    });

    let users = document.querySelector("#users");
    users.innerHTML = html;
}

renderUser();