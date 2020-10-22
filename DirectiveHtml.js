let DirectiveHtml = {

    template: `<div>
                <h1 v-text="text"></h1>
                <p v-html="message"></p>
                </div>`,
    data() {
        return {
            text: 'Directiva v-html',
            message: '<b>Hola desde directive v-html</b>'
        }
    }
  
}