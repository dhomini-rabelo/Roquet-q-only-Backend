let subLinks = document.querySelectorAll('.sub-link')

document.addEventListener('DOMContentLoaded', focusForSubTitles)
subLinks.forEach(
    (link) => link.addEventListener('click', () => setTimeout(focusForSubTitles, 200))
)
    
function focusForSubTitles() {
    let url = document.URL
    let focus = url.substring(url.indexOf('#')+1)
    if (focus === url){
        subLinks[0].classList.add('sub-title-active')
        return
    }
    subLinks.forEach((link) => {
        if (link.getAttribute('focus') === focus) {
            link.classList.add('sub-title-active')
        } else{
            link.classList.remove('sub-title-active')
        }
    })
}

