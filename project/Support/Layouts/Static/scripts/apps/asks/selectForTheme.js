let selectMain = document.querySelector('.select-main')
let questions = document.querySelectorAll('div.app.select > .my-questions')

selectMain.addEventListener('change', showThemeQuestion)


function showThemeQuestion() {
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