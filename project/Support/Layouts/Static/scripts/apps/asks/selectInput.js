let inputTheme = document.querySelector('input#id_theme')
let selectTheme = document.querySelector('select')


selectTheme.addEventListener('change', updateInputTheme)


function updateInputTheme(event) {
    let themeSelected = this.selectedOptions[0]
    inputTheme.value = themeSelected.innerHTML
}