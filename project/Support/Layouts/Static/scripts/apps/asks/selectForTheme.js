let selectsMain = document.querySelectorAll('.select-main')


selectsMain.forEach((selectMain) => {
    selectMain.addEventListener('change', showThemeQuestion)
})



function showThemeQuestion() {
    let questions = document.querySelectorAll('div.app.select.visible  .my-questions')
    let currentMainTheme = this.selectedOptions[0].innerHTML
    questions.forEach((question) => {
        let questionTheme = question.getAttribute('theme')

        if (questionTheme === currentMainTheme){
            if(!question.classList.contains('visible')){
                question.classList.add('visible')
            }
        } else {
            if(question.classList.contains('visible')){    
                question.classList.remove('visible')
            }
        }
    })    
}